from ppo_3 import *
import torch as th
from wandb.integration.sb3 import WandbCallback
import sys
import random
import os
from gym_unity.envs import UnityToGymWrapper
from animalai.envs.environment import AnimalAIEnvironment
import wandb

#wandb.init(project="AnimalAI Agents", entity="kindsofintelligence", sync_tensorboard=True) 

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
        inference= False, # if you turn off you can go faster
        useCamera=True,
        resolution=resolution,
        useRayCasts=False,
        # raysPerSide=1,
        # rayMaxDegrees = 30,
    )

    # Env setup

    env = UnityToGymWrapper(aai_env, uint8_visual=True, allow_multiple_obs=False, flatten_branched=True)
    env = TorchWrapper(env)

    learning_rate = 2.5e-4

    # Agent setup
    agent = ActorCritic(env)
    optimizer = optim.Adam(agent.parameters(), lr=learning_rate, eps=1e-5)

    model = PPOTrainer(env, optimizer, agent)
    model.train()

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

    #wandb.finish()