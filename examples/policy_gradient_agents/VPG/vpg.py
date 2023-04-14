import numpy as np
import torch
import statistics

def discount_rewards(rewards, gamma=0.99):
    r = np.array([gamma**i * rewards[i] 
                  for i in range(len(rewards))])
    # Reverse the array direction for cumsum and then
    # revert back to the original order
    r = r[::-1].cumsum()[::-1]
    return r - r.mean()

def vpg(env, policy_estimator, value_estimator, num_episodes=2000, batch_size=10, gamma=0.99, entropy_loss_weight = 0.001):

    # Set up lists to hold results
    total_rewards = []
    batch_rewards = []
    batch_actions = []
    batch_states = []
    batch_counter = 1
    
    for ep in range(num_episodes):
        s_0 = env.reset()
        states = []
        rewards = []
        actions = []
        entropies = []

        complete = False
        while complete == False:
            # Get actions and convert to numpy array
            action, entropy = policy_estimator.get_action(s_0)
            s_1, r, complete, _ = env.step(action)
            
            states.append(s_0)
            rewards.append(r)
            actions.append(action)
            entropies.append(entropy)
            s_0 = s_1
            
            # If complete, batch data
            if complete:
                batch_rewards.extend(discount_rewards(rewards, gamma))
                batch_states.extend(states)
                batch_actions.extend(actions)
                batch_counter += 1
                total_rewards.append(sum(rewards))
                
                # If batch is complete, update network
                if batch_counter == batch_size:
                    state_tensor = torch.FloatTensor(batch_states)
                    reward_tensor = torch.FloatTensor(batch_rewards)
                    # Actions are used as indices, must be LongTensor
                    action_tensor = torch.LongTensor(batch_actions)
                    
                    value_tensor = value_estimator.forward(state_tensor)

                    # Calculate loss
                    logprob = torch.log(policy_estimator.forward(state_tensor))
                    selected_logprobs = reward_tensor * logprob[np.arange(len(action_tensor)), action_tensor] 
                    entropy_loss = -(statistics.mean(entropies))
                    loss = torch.mean(-selected_logprobs * (reward_tensor - value_tensor) + (entropy_loss_weight * entropy_loss))

                    # Calculate gradients
                    policy_estimator.optimizer.zero_grad()
                    loss.backward()
                    policy_estimator.optimizer.step()
                    
                    # calculate vf loss
                    loss_fn = torch.nn.MSEloss()
                    v_loss = loss_fn(value_tensor, reward_tensor)
                    
                    # Calculate gradient for value network
                    value_estimator.optimizer.zero_grad()
                    v_loss.backward()
                    value_estimator.optimizer.step()

                    batch_rewards = []
                    batch_actions = []
                    batch_states = []
                    batch_counter = 1
                    
                # Print running average
                print("\rEp: {} Average of last 10: {:.2f}".format(
                    ep + 1, np.mean(total_rewards[-10:])), end="")
                
    return total_rewards
