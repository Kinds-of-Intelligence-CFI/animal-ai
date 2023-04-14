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
        probs = F.softmax(logits, dim=1)
        dist = Categorical(probs=probs)
        critic_output = self.critic_fc(x / 255.0)
        return dist, critic_output

class PPO:
    def __init__(self, env, actor_critic, learning_rate = 7e-4, n_epochs=4, tau = 0.95,
                gamma=0.99, mini_batches = 32, n_episodes = 200, gae_lambda=0.95, ent_coef=0.0 , vf_coef=0.5, 
                clip_coef = 0.2, max_grad_norm=0.5, linear_lr_decay = False):
        self.actor_critic_nn = actor_critic
        self.ent_coef = ent_coef
        self.vf_coef = vf_coef
        self.max_grad_norm = max_grad_norm
        self.gamma = gamma
        self.tau = tau
        self.gae_lambda = gae_lambda
        self.action_shape = env.action_space.n
        self.linear_lr_decay = linear_lr_decay
        self.mini_batches = mini_batches
        self.actor_critic_opt = optim.Adam(self.actor_critic_nn.parameters(), lr=learning_rate)
        self.n_epochs = n_epochs
        self.clip_coef = clip_coef
        self.env = env
        self.n_episodes = n_episodes

    def compute_gae(self, next_value, rewards, masks, values):
        values = values + [next_value]
        gae = 0
        returns = []
        for step in reversed(range(len(rewards))):
            delta = rewards[step] + self.gamma * values[step + 1] * masks[step] - values[step]
            gae = delta + self.gamma * self.tau * masks[step] * gae
            returns.insert(0, gae + values[step])
        return returns
    
    def ppo_iter(self, states, actions, log_probs, returns, advantage):
        batch_size = states.size(0)
        
        for _ in range(batch_size // self.mini_batches):
            rand_idx = np.random.randint(0, batch_size, self.mini_batches)
            yield states[rand_idx], actions[rand_idx], log_probs[rand_idx], returns[rand_idx], advantage[rand_idx]
        
    def ppo_update(self, states, actions, log_probs, returns, advantages):
        for _ in range(self.n_epochs):
            for state, action, old_log_probs, return_, advantage in self.ppo_iter(states, actions, log_probs, returns, advantages):
                dist, value = self.actor_critic_nn.forward(state)
                entropy = dist.entropy().mean()
                new_log_probs = dist.log_prob(action)

                ratio = (new_log_probs - old_log_probs).exp()
                surr1 = ratio * advantage
                surr2 = torch.clamp(ratio, 1.0 - self.clip_coef, 1.0 + self.clip_coef) * advantage

                actor_loss  = - torch.min(surr1, surr2).mean()
                critic_loss = (return_ - value).pow(2).mean()

                loss = self.vf_coef * critic_loss + actor_loss - self.ent_coef * entropy

                self.actor_critic_opt.zero_grad()
                loss.backward()
                self.actor_critic_opt.step()
    
    def train(self):
        state = torch.Tensor(self.env.reset())
        state = torch.reshape(torch.Tensor(state), (1, 3, 36, 36))
        rewards_list = []
        total_reward = 0

        # loop through number of episodes
        for episode in range(self.n_episodes):
            # print(f"start episode number: {episode}")
            self.env.reset()

            states = []
            actions = []
            logprobs = []
            rewards = []
            values = []
            masks = []

            next_done = False
            entropy = 0

            while not next_done: 
                state = torch.reshape(torch.Tensor(state), (1, 3, 36, 36))
                dist, value = self.actor_critic_nn.forward(state)
                action = dist.sample()
                next_state, reward, next_done, _ = self.env.step(action.item())
                total_reward += reward
                log_prob = dist.log_prob(action)
                entropy += dist.entropy().mean()

                logprobs.append(log_prob)
                values.append(value)
                rewards.append(reward)
                masks.append(1 - next_done)
                states.append(state)
                actions.append(action)

                state = next_state

            rewards_list.append(sum(rewards))
            returns = self.compute_gae(value, rewards, masks, values)
            wandb.log({'reward': sum(rewards), 'global_step': episode})

            returns   = torch.cat(returns).detach()
            logprobs = torch.cat(logprobs).detach()
            values    = torch.cat(values).detach()
            states    = torch.cat(states)
            actions   = torch.cat(actions)
            advantage = returns - values

            self.ppo_update(states, actions, logprobs, returns, advantage)

        avg_reward = sum(rewards_list) / len(rewards_list)
        return avg_reward
