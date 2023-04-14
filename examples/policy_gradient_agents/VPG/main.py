from network import PolicyNetwork, ValueNetwork
import matplotlib.pyplot as plt
import sys, random, os
from gym_unity.envs import UnityToGymWrapper
from animalai.envs.environment import AnimalAIEnvironment
from vpg import vpg
import numpy as np

def train_agent_single_config(configuration_file):
    '''
      Agent is trained in here with the configured hyper parameters & levels.
    '''
    resolution = 36

    aai_env = AnimalAIEnvironment(
        seed = 123,
        file_name="env\AnimalAI",
        arenas_configurations=configuration_file,
        play=False,
        base_port=5000,
        inference=True, # if you turn off you can go faster
        useCamera=True,
        resolution=resolution,
        useRayCasts=False,
        # raysPerSide=1,
        # rayMaxDegrees = 30,
    )

    env = UnityToGymWrapper(aai_env, uint8_visual=True, allow_multiple_obs=False, flatten_branched=True)
    n_obs = env.observation_space.shape
    n_state = (1, 3, 36, 36)
    n_action = env.action_space.n
    n_hidden = 256
    val_hidden = 128
    lr = 0.003
    gamma = 0.8
    n_episode = 1000
    entropy_loss_weight = 0.001

    policy_net = PolicyNetwork(n_state, n_action, n_hidden, lr)
    value_net = ValueNetwork(n_state, val_hidden, lr)
    
    rewards = vpg(env, policy_net, value_net, n_episode, gamma, entropy_loss_weight)

    window = 10
    smoothed_rewards = [np.mean(rewards[i-window:i+1]) if i > window 
                    else np.mean(rewards[:i+1]) for i in range(len(rewards))]

    plt.figure(figsize=(12,8))
    plt.plot(rewards)
    plt.plot(smoothed_rewards)
    plt.ylabel('Total Rewards')
    plt.xlabel('Episodes')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        configuration_file = sys.argv[1]
    else:   
        competition_folder = "configs/competition/"
        configuration_files = os.listdir(competition_folder)
        configuration_random = random.randint(0, len(configuration_files))
        configuration_file = (
            competition_folder + configuration_files[configuration_random]
        )

    train_agent_single_config(configuration_file="configs/competition/01-01-02.yaml")
