from typing import Any, Dict, Tuple

import gym
import numpy as np
import torch
from torch import Tensor, nn, optim
from torch.distributions import Categorical
import wandb

class TorchWrapper(gym.Wrapper):
    """
    Torch wrapper. Actions and observations are Tensors instead of arrays.
    """

    def step(self, action: Tensor) -> Tuple[Tensor, float, bool, Dict[str, Any]]:
        action = action.cpu().numpy()
        observation, reward, done, info = self.env.step(action)
        return torch.reshape(torch.Tensor(observation), (1, 3, 36, 36)), reward, done, info

    def reset(self) -> Tensor:
        observation = self.env.reset()
        return torch.reshape(torch.Tensor(observation), (1, 3, 36, 36))


def layer_init(layer, std=np.sqrt(2), bias_const=0.0):
    torch.nn.init.orthogonal_(layer.weight, std)
    torch.nn.init.constant_(layer.bias, bias_const)
    return layer

class ActorCritic(nn.Module):
    def __init__(self, env):
        super().__init__()
        self.actor = nn.Sequential(
            layer_init(nn.Conv2d(env.observation_space.shape[2], 32, 8, stride=4)),
            nn.ReLU(),
            layer_init(nn.Conv2d(32, 64, 4, stride=2)),
            nn.ReLU(),
            layer_init(nn.Conv2d(64, 64, 3, stride=1)),
            nn.ReLU(),
            nn.Flatten(),
            layer_init(nn.Linear(64, 512)),
            nn.ReLU(),
            layer_init(nn.Linear(512, env.action_space.n), std=0.01),
        )

        self.critic = nn.Sequential(
            layer_init(nn.Conv2d(env.observation_space.shape[2], 32, 8, stride=4)),
            nn.ReLU(),
            layer_init(nn.Conv2d(32, 64, 4, stride=2)),
            nn.ReLU(),
            layer_init(nn.Conv2d(64, 64, 3, stride=1)),
            nn.ReLU(),
            nn.Flatten(),
            layer_init(nn.Linear(64, 512)),
            nn.ReLU(),
            layer_init(nn.Linear(512, 1), std=1.0),
        )

    def get_value(self, observation):
        return self.critic(observation).squeeze(-1)

    def get_action_distribution(self, observation):
        logits = self.actor(observation)
        return Categorical(logits=logits)

    def get_action(self, observation):
        distribution = self.get_action_distribution(observation)
        action = distribution.sample()
        return action, distribution.log_prob(action)

class PPOTrainer():
    def __init__(self, env, optimizer, network, total_timesteps = 20000, num_steps = 128, lr = 2.5e-4, gamma = 0.99, 
        gae_lambda = 0.95, n_update = 4, clip_coef = 0.2, max_grad_norm = 0.5, ent_coef = 0.01, vf_coef = 0.95):
        self.agent = network
        self.env = env
        self.optimizer = optimizer
        self.learning_rate = lr
        self.total_timesteps = total_timesteps
        self.num_steps = num_steps
        self.num_updates = self.total_timesteps // self.num_steps
        self.learning_rate = lr
        self.gamma = gamma
        self.gae_lambda = gae_lambda
        self.minibatch_size = num_steps // 4
        self.num_updates = n_update
        self.max_grad_norm = max_grad_norm
        self.clip_coef =clip_coef
        self.ent_coef = ent_coef
        self.vf_coef = vf_coef


    def train(self):
        # Storage setup (num_steps + 1 because we need the terminal values to compute the advantage)
        observations = torch.zeros((500,) + (3, 36, 36))
        actions = torch.zeros((500,) + (self.env.action_space.n,))
        log_probs = torch.zeros(500,)
        rewards = torch.zeros(500,)
        dones = torch.zeros(500,)
        values = torch.zeros(500,)

        # Init the env
        observation = self.env.reset()
        global_step = 0

        # Loop
        for update in range(self.num_updates):
            # Annealing the rate
            new_lr = (1.0 - update / self.num_updates) * self.learning_rate
            self.optimizer.param_groups[0]["lr"] = new_lr

            step = 0

            # Store initial
            observations[step] = observation
            with torch.no_grad():
                values[step] = self.agent.get_value(observation)

            while step < 500:
                # Compute action
                with torch.no_grad(): # not necessary
                    action, log_prob = self.agent.get_action(observations[step])

                # Store
                actions[step] = action
                log_probs[step] = log_prob

                # Step
                observation, reward, done, info = self.env.step(action)
                print(done)

                if done:
                    observation = self.env.reset()
                    print(f"global_step={global_step}, episodic_return={info['episode']['r']:.2f}")

                # Update count
                step += 1
                global_step += 1

                # Store
                observations[step] = observation
                with torch.no_grad():
                    values[step] = self.agent.get_value(observations[step])
                rewards[step] = reward
                dones[step] = done

            #wandb.log({'reward': sum(rewards), 'global_step': update})
            observations = observations[observations.sum(dim=2) != 0]
            actions = actions[actions.sum(dim=2) != 0]
            log_probs = log_probs[log_probs.sum(dim=2) != 0]
            rewards = rewards[rewards.sum(dim=2) != 0]
            values = values[values.sum(dim=2) != 0]
            tensor_length = observations.size(dim=1)
            print(tensor_length)
            dones = dones[dones.sum(dim=2) != 0]

            # Compute advanges and return
            advantages = torch.zeros_like(rewards)
            last_gae_lamda = 0
            for t in reversed(range(self.num_steps)):
                advantages[t] = (
                    rewards[t + 1] + self.gamma * (1.0 - dones[t + 1]) * (values[t + 1] + self.gae_lambda * last_gae_lamda) - values[t]
                )
                last_gae_lamda = advantages[t]
            returns = advantages + values

            # Optimizing the policy and value network
            for epoch in range(self.update_epochs):
                b_inds = np.random.permutation(self.num_steps)
                for start in range(0, self.num_steps, self.minibatch_size):
                    end = start + self.minibatch_size
                    mb_inds = b_inds[start:end]
                    b_observations = observations[mb_inds]
                    b_values = values[mb_inds]
                    b_actions = actions[mb_inds]
                    b_log_probs = log_probs[mb_inds]
                    b_returns = returns[mb_inds]
                    b_advantages = advantages[mb_inds]

                    action_distribution = self.agent.get_action_distribution(b_observations)

                    # Policy loss
                    b_advantages = (b_advantages - torch.mean(b_advantages)) / (torch.std(b_advantages) + 1e-8)  # norm advantages
                    new_log_probs = action_distribution.log_prob(b_actions)
                    ratio = torch.exp(new_log_probs - b_log_probs)
                    pg_loss1 = -b_advantages * ratio
                    pg_loss2 = -b_advantages * torch.clamp(ratio, 1 - self.clip_coef, 1 + self.clip_coef)
                    pg_loss = torch.mean(torch.max(pg_loss1, pg_loss2))

                    # Entropy loss
                    entropy_loss = torch.mean(action_distribution.entropy())

                    # Clip V-loss
                    new_values = self.agent.get_value(b_observations)
                    v_loss_unclipped = (new_values - b_returns) ** 2
                    v_clipped = b_values + torch.clamp(new_values - b_values, -self.clip_coef, self.clip_coef)
                    v_loss_clipped = (v_clipped - b_returns) ** 2
                    v_loss = 0.5 * torch.mean(torch.max(v_loss_unclipped, v_loss_clipped))

                    # Total loss
                    loss = pg_loss - self.ent_coef * entropy_loss + v_loss * self.vf_coef

                    self.optimizer.zero_grad() # before loss?
                    loss.backward()
                    nn.utils.clip_grad_norm_(self.agent.parameters(), self.max_grad_norm)
                    self.optimizer.step()

            var_y = torch.var(values)
            explained_var = torch.nan if var_y == 0 else 1 - torch.var(values - returns) / var_y

        self.env.close()