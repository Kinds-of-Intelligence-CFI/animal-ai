from ppo_copy import *
import torch as th
import random
import os, sys
import csv
import itertools
from gym_unity.envs import UnityToGymWrapper
from animalai.envs.environment import AnimalAIEnvironment

### Basic PPO agent + load config and watch.
def train_agent_single_config(configuration_file):
    '''
      Agent is trained in here with the configured hyper parameters & levels.
    '''
    resolution = 36

    aai_env = AnimalAIEnvironment(
        seed = 123,
        file_name="env\AnimalsAI",
        arenas_configurations=configuration_file,
        play=False,
        base_port=5000,
        inference= False, # if you turn off you can go faster
        useCamera=True,
        resolution=resolution,
        useRayCasts=False,
    )


    env = UnityToGymWrapper(aai_env, uint8_visual=True, allow_multiple_obs=False, flatten_branched=True)
    n_obs = env.observation_space.shape[2]
    n_act = env.action_space.n
    hidden_size = 32
    network = actor_critic(n_obs, n_act, hidden_size)

    # Define the hyperparameters to be searched
    learning_rate = [1e-3, 5e-4, 1e-4]
    n_epochs = [5, 10, 20]
    tau = [0.8, 0.9, 0.95]
    gamma = [0.9, 0.95, 0.99]
    mini_batches = [32, 64, 128]
    gae_lambda = [0.8, 0.9, 0.95]
    ent_coef = [0.0, 0.01, 0.1]
    vf_coef = [0.5, 0.8, 1.0]
    clip_coef = [0.1, 0.2, 0.3]
    max_grad_norm = [0.5, 1.0, 2.0]

    param_grid = [learning_rate, n_epochs, tau, gamma, mini_batches, gae_lambda, ent_coef, vf_coef, clip_coef, max_grad_norm]
    param_combinations = list(itertools.product(*param_grid))

    best_params = None
    best_reward = float('-inf')

    with open ('agents/PPO/avg_hp.csv', 'w') as f:
        writer = csv.writer(f)

        for _ in range(100):
            params = [random.choice(param_grid[i]) for i in range(len(param_grid))]
            # set the hyperparameters
            ppo = PPO(env, network, learning_rate=params[0], n_epochs=params[1], tau=params[2],
                    gamma=params[3], mini_batches=params[4], gae_lambda=params[5], ent_coef=params[6], vf_coef=params[7],
                    clip_coef=params[8], max_grad_norm=params[9])
            
            # train the agent with these hyperparameters
            avg_reward = ppo.train()
            writer.writerow([params, avg_reward])

                    # keep track of the best set of hyperparameters
            if avg_reward > best_reward:
                best_reward = avg_reward
                best_params = params

        print("Best params: ", best_params)
        print("Best reward: ", best_reward)

        writer.writerow([best_params, best_reward])
        f.close()

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

    train_agent_single_config(configuration_file="configs/basic/1g.yml")


