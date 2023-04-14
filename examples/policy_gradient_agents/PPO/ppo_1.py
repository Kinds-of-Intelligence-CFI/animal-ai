import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.distributions.categorical import Categorical
import wandb
import numpy as np

def layer_init(layer, std=np.sqrt(2), bias_const=0.0):
    torch.nn.init.orthogonal_(layer.weight, std)
    torch.nn.init.constant_(layer.bias, bias_const)
    return layer

# Define the actor and critic networks
class actor_critic(nn.Module):
    def __init__(self, obs_dim, act_dim, hidden_size):
        super().__init__()
        self.cnn = nn.Sequential(
                layer_init(nn.Conv2d(obs_dim, hidden_size, 8, stride=4)),
                nn.ReLU(),
                layer_init(nn.Conv2d(hidden_size, 64, 4, stride=2)),
                nn.ReLU(),
                layer_init(nn.Conv2d(64, 32, 3, stride=1)),
                nn.ReLU(),
                nn.Flatten(),
                layer_init(nn.Linear(32,  512)),
                nn.ReLU(),
        )
        self.actor_fc =  layer_init(nn.Linear(512, act_dim), std=0.01)
        self.critic_fc = layer_init(nn.Linear(512, 1), std=1)


    def forward(self, obs):
        x = self.cnn(obs)
        x = x.view(x.size(0), -1) 
        logits = self.actor_fc(x)
        critic_output = self.critic_fc(x)
        return logits, critic_output

    def get_action_and_value(self, x, action = None):
        logits, critic_output = self.forward(x)
        probs = F.softmax(logits, dim=1)
        dist = Categorical(probs=probs)
        with torch.no_grad():
            action = dist.sample()
        return action, dist.log_prob(action), dist.entropy(), critic_output

    def get_value(self, x):
        _, critic_output = self.forward(x)
        return critic_output

class PPO:
    def __init__(self, env, actor_critic, learning_rate = 7e-4, n_epochs=4, tau = 0.95,
                gamma=0.99, mini_batches = 32, n_episodes = 200, gae_lambda=0.95, ent_coef=0.0 , vf_coef=0.5, 
                clip_coef = 0.2, max_grad_norm=0.5, linear_lr_decay = False, device = 'cpu'):
        self.actor_critic_nn = actor_critic
        self.device = device
        self.ent_coef = ent_coef
        self.vf_coef = vf_coef
        self.max_grad_norm = max_grad_norm
        self.gamma = gamma
        self.gae_lambda = gae_lambda
        self.action_shape = env.action_space.n
        self.mini_batches = mini_batches
        self.actor_critic_opt = optim.Adam(self.actor_critic_nn.parameters(), lr=learning_rate)
        self.n_epochs = n_epochs
        self.clip_coef = clip_coef
        self.env = env
    
    def train(self):
        num_episodes = 200
        
        # loop through number of episodes
        for episode in range(1, num_episodes + 1):
            step = 0

            observation = torch.zeros((500,) + (3, 36, 36))
            actions = torch.zeros((500,) + (self.action_shape,))
            logprobs = torch.zeros(500,)
            rewards = torch.zeros(500,)
            dones = torch.zeros(500,)
            values = torch.zeros(500,)

            obs = torch.Tensor(self.env.reset())
            obs = torch.reshape(torch.Tensor(obs), (1, 3, 36, 36))
            next_done = torch.zeros(1)

            while not next_done:
                observation[step] = obs # store observation and done boolean in tensor
                dones[step] = next_done

                # take action based on observation input
                with torch.no_grad():
                    action, logprob, _, value = self.actor_critic_nn.get_action_and_value(obs)
                    values[step] = value.flatten() # make 1D array
                actions[step] = action # store action and logprob in tensor
                logprobs[step] = logprob
                
                # execute game by taking action and return new state, reward, done boolean
                next_obs, reward, done, info = self.env.step(action.item())
                rewards[step] = torch.tensor(reward) # store reward in tensor
                next_obs, next_done = torch.reshape(torch.Tensor(next_obs), (1, 3, 36, 36)), done

                with torch.no_grad():
                    next_value = self.actor_critic_nn.get_value(next_obs).reshape(1, -1) 
                
                obs = next_obs
                step += 1

            # flatten the batch 
            b_obs = observation.reshape((-1,) + (3,36,36))
            print(b_obs.shape)

            # bootstrap value for GAE and coompute return
            advantages = torch.zeros_like(rewards)
            lastgaelam = 0 # hyperparameter can be 1

            for step in reversed(range(b_obs.shape[0])):
                if step == b_obs.shape[0] - 1:
                    nextnonterminal = 1.0 - next_done
                    nextvalues = next_value
                else:
                    nextnonterminal = 1.0 - dones[step + 1]
                    nextvalues = values[step + 1]
                
                delta = rewards[step] + self.gamma * nextvalues * nextnonterminal - values[step]
                advantages[step] = lastgaelam = delta + self.gamma * self.gae_lambda * nextnonterminal * lastgaelam
            returns = advantages + values

            b_logprobs = logprobs.reshape(-1)
            b_actions = actions.reshape((-1,) + (self.action_shape,))
            b_advantages = advantages.reshape(-1)
            b_returns = returns.reshape(-1)
            b_values = values.reshape(-1)
            
            #wandb.log({'reward': sum(rewards), 'global_step': episode})

            # Optimise policy and value network
            b_inds = np.arange(b_obs.shape[0]) # initliase array with buffer
            entropy_losses = []
            pg_losses, value_losses = [], []
                
            # run K epochs where you create minibatches of randomised batch individuals
            for epoch in range(self.n_epochs):
                np.random.shuffle(b_inds)

                # initialise mini batches
                for start in range(0, b_obs.shape[0], self.mini_batches): # for start in range(mb_size)
                    end = start + self.mini_batches
                    mb_inds = b_inds[start:end]
                    
                    # rollout data, compute values and log_probs
                    _, newlogprob, entropy, newvalue = self.actor_critic_nn.get_action_and_value(b_obs[mb_inds], b_actions.long()[mb_inds])
                    ratio = torch.exp(newlogprob - b_logprobs[mb_inds])

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
                    #>> print v_loss

                    # compute entropy loss
                    entropy_loss = -torch.mean(entropy)
                    entropy_losses.append(entropy_loss.item())
                    
                    # compute total loss
                    loss = pg_loss  +  0.5 * v_loss * self.vf_coef - self.ent_coef * entropy_loss
                    
                    self.actor_critic_opt.zero_grad()
                    loss.backward()
                    nn.utils.clip_grad_norm_(self.actor_critic_nn.parameters(), self.max_grad_norm)
                    self.actor_critic_opt.step()









