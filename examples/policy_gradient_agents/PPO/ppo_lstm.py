import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.distributions.categorical import Categorical
from torch.utils.data import Dataset, TensorDataset, DataLoader
import wandb
import numpy as np

class actor_critic(nn.Module):
    def __init__(self, obs_dim, act_dim, hidden_size):
        super(actor_critic, self).__init__()
        self.cnn = nn.Sequential(
            nn.Conv2d(obs_dim, hidden_size, kernel_size=8, stride=4, padding=0),
            nn.ReLU(),
            nn.Conv2d(hidden_size, 64, kernel_size=4, stride=2, padding=0),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=0), # new: added a new layer
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(64 * 7 * 7, 512) # new: adapted linear to match new layer
        )
        
         # new: it will have a data input and state (hidden, cell) and give the new lstm_state based on the input
         # new:  dimensions of output are (output_sequence_length,batch_size,hidden_size)
        self.lstm = nn.LSTM(512, 128) #
        self.actor_fc = nn.Linear(128, act_dim) # new: changed actor to have lstm input
        self.critic_fc = nn.Linear(128, 1) # new: changed critic to have lstm input

    def get_states(self, obs, lstm_state, done):
        '''
        x: input data, series of frames with shape number of frames, height, width, channel
        lstm_state: a tuple containing the current hidden state and cell state of the LSTM
        done: a boolean mask indicating which elements in the input data correspond to the end of a sequence
        '''
        x_hidden = self.cnn(obs) # new: get states, you can obs/ 255.0 this normalizes the input
        batch_size = lstm_state[0].shape[1] # new :  set to the second dimension of the hidden state tensor
        x_hidden = x_hidden.reshape((-1, batch_size, self.lstm.input_size)) # new
        done = done.reshape((-1, batch_size)) # new: done same shape as hidden

        new_hidden = []
        for h, d in zip(x_hidden, done):
            # loop iterated over the elements of hidden & done into a tuple
            # call LSTM with current hidden state and stored lstm to update the internal state of LSTM
            h, lstm_state = self.lstm(
                h.unsqueeze(0), # add dimension for h to have write LSTM shape
                (
                    # if input corresponds to the end of a sequence, the value of (1.0 - d) will be 0, for elements at the end of sequence it resets LSTM
                    (1.0 - d).view(1, -1, 1) * lstm_state[0], # reshape for mulitplication
                    (1.0 - d).view(1, -1, 1) * lstm_state[1],
                ),
            )
            new_hidden += [h]
        new_hidden = torch.flatten(torch.cat(new_hidden), 0, 1)
        return new_hidden, lstm_state
    
    def get_value(self, obs, lstm_state, done):
        hidden, _ = self.get_states(obs, lstm_state, done)
        return self.critic_fc(hidden)

    def get_action_and_value(self, x, lstm_state, done, action=None):
        hidden, lstm_state = self.get_states(x, lstm_state, done)
        logits = self.actor_fc(hidden)
        dist = Categorical(probs=logits)
        if action is None:
            action = dist.sample()
        return action, dist.log_prob(action), dist.entropy(), self.critic_fc(hidden), lstm_state

class PPO:
    def __init__(self, env, actor_critic, learning_rate = 3e-4, n_steps=2048, n_epochs=10, 
                gamma=0.99, mini_batches = 64, gae_lambda=0.95, clip_range=0.2, ent_coef=0.01, vf_coef=0.5,
                clip_coef = 0.1, max_grad_norm=0.5, device='cpu'):
        self.actor_critic_nn = actor_critic
        self.device = device
        self.ent_coef = ent_coef
        self.vf_coef = vf_coef
        self.max_grad_norm = max_grad_norm
        self.n_steps = n_steps
        self.gamma = gamma
        self.gae_lambda = gae_lambda
        self.clip_range = clip_range
        self.buffer = self.n_steps 
        self.action_shape = env.action_space.n
        self.mini_batches = mini_batches
        self.actor_critic_opt = optim.Adam(self.actor_critic_nn.parameters(), lr=learning_rate)
        self.mb_size = self.buffer // self.mini_batches # untruncated batches
        self.n_epochs = n_epochs
        self.clip_coef = clip_coef
        self.env = env
    
    def train(self):
        observation = torch.zeros((self.n_steps,) + (3, 36, 36))
        actions = torch.zeros((self.n_steps,) + (self.action_shape,))
        logprobs = torch.zeros(self.n_steps)
        rewards = torch.zeros(self.n_steps)
        dones = torch.zeros(self.n_steps)
        values = torch.zeros(self.n_steps)
        
        num_episodes = 1000
        
        # loop through number of episodes
        for episode in range(1, num_episodes + 1):
            rewards = torch.zeros(self.n_steps)
            next_obs = torch.Tensor(self.env.reset())
            next_obs = torch.reshape(torch.Tensor(next_obs), (1, 3, 36, 36))
            next_done = torch.zeros(1)
            next_lstm_state = ( # new
                torch.zeros(self.actor_critic_nn.num_layers, self.actor_critic_nn.lstm.hidden_size), # hidden state tensor
                torch.zeros(self.actor_critic_nn. lstm.num_layers, self.actor_critic_nn.lstm.hidden_size), # cell state tensor
            ) 
            initial_lstm_state = (next_lstm_state[0].clone(), next_lstm_state[1].clone()) # clone so any changes to initial_lstm will not affect next_lstm

            step = 0

            while not next_done and step < self.n_steps: 
                observation[step] = next_obs # store observation and done boolean in tensor
                dones[step] = next_done

                # take action based on observation input
                with torch.no_grad():
                    action, logprob, _, value, next_lstm_state = self.actor_critic_nn.get_action_and_value(next_obs, next_lstm_state, next_done)
                    values[step] = value.flatten() # make 1D array
                actions[step] = action # store action and logprob in tensor
                logprobs[step] = logprob
                
                # execute game by taking action and return new state, reward, done boolean
                next_obs, reward, done, info = self.env.step(action.item())
                rewards[step] = torch.tensor(reward) # store reward in tensor
                next_obs, next_done = torch.reshape(torch.Tensor(next_obs), (1, 3, 36, 36)), done

                with torch.no_grad():
                    next_value = self.actor_critic_nn.get_value(next_obs).reshape(1, -1) 
                step += 1
            self.env.reset()

            # bootstrap value for GAE and coompute return
            next_value = self.actor_critic_nn.get_value(next_obs,next_lstm_state,next_done,).reshape(1, -1)
            advantages = torch.zeros_like(rewards)
            lastgaelam = 0 # hyperparameter can be 1

            for step in reversed(range(self.n_steps)):
                if step == self.n_steps - 1:
                    nextnonterminal = 1.0 - next_done
                    nextvalues = next_value
                else:
                    nextnonterminal = 1.0 - dones[step + 1]
                    nextvalues = values[step + 1]
                
                delta = rewards[step] + self.gamma * nextvalues * nextnonterminal - values[step]
                advantages[step] = lastgaelam = delta + self.gamma * self.gae_lambda * nextnonterminal * lastgaelam
            returns = advantages + values

            wandb.log({'reward': sum(rewards), 'global_step': episode})

            # flatten the batch 
            b_obs = observation.reshape((-1,) + (3,36,36))
            b_logprobs = logprobs.reshape(-1)
            b_actions = actions.reshape((-1,) + (self.action_shape,))
            b_dones = dones.reshape(-1)
            b_advantages = advantages.reshape(-1)
            b_returns = returns.reshape(-1)
            b_values = values.reshape(-1)

            # Optimise policy and value network
            b_inds = np.arange(self.buffer) # initliase array with buffer
            entropy_losses = []
            pg_losses, value_losses = [], []
                
            # run K epochs where you create minibatches of randomised batch individuals, here minibatches means a batch of sequences
            for epoch in range(self.n_epochs):
                np.random.shuffle(b_inds)

                # initialise mini batches
                for start in range(0, self.buffer, self.mini_batches):
                    end = start + self.mini_batches
                    mb_inds = b_inds[start:end]
                    
                    # rollout data, compute values and log_probs
                    _, newlogprob, entropy, newvalue = self.actor_critic_nn.get_action_and_value(b_obs[mb_inds], (initial_lstm_state[0][:, mb_inds], initial_lstm_state[1][:, mb_inds]),
                    b_dones[mb_inds], b_actions.long()[mb_inds])
                    ratio = torch.exp(newlogprob - b_logprobs[mb_inds])
                    print(f"Ratio: {ratio}")

                    # compute minibatch advantages
                    mb_advantages = b_advantages[mb_inds]
                    mb_adv = (mb_advantages - mb_advantages.mean()) / (mb_advantages.std() + 1e-8)

                    # policy gradient losses >> clipped surrogate loss
                    pg_loss1 = mb_adv * ratio
                    pg_loss2 = mb_adv * torch.clamp(ratio, 1 - self.clip_coef, 1 + self.clip_coef)
                    pg_loss = -torch.min(pg_loss1, pg_loss2).mean() 
                    pg_losses.append(pg_loss.item())

                    # value loss
                    # v_loss = F.mse_loss(b_returns[mb_inds], newvalue.view(-1))

                    v_loss_unclipped = (newvalue.view(-1) - b_returns[mb_inds]) ** 2 # square difference between new value and expected returns of batch returns
                    v_clipped = b_values[mb_inds] + torch.clamp( newvalue - b_values[mb_inds], -self.clip_coef, self.clip_coef,) # clipped

                    v_loss_clipped = (v_clipped - b_returns[mb_inds]) ** 2 # square difference between clipped value and expected returns of batch returns
                    v_loss = 0.5 * torch.max(v_loss_unclipped, v_loss_clipped).mean()
                    value_losses.append(v_loss.item())

                    # compute entropy loss
                    entropy_loss = -torch.mean(entropy)
                    entropy_losses.append(entropy_loss.item())
                    
                    # compute total loss
                    loss = pg_loss - self.ent_coef * entropy_loss + v_loss * self.vf_coef

                    self.actor_critic_opt.zero_grad()
                    loss.backward()
                    nn.utils.clip_grad_norm_(self.actor_critic_nn.parameters(), self.max_grad_norm)
                    self.actor_critic_opt.step()
