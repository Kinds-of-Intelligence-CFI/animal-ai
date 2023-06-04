from stable_baselines3 import PPO
from stable_baselines3 import DQN
import torch as th
from wandb.integration.sb3 import WandbCallback
import sys
import random
import os
# from stable_baselines3.common.vec_env.dummy_vec_env import DummyVecEnv
from gym_unity.envs import UnityToGymWrapper
from animalai.envs.environment import AnimalAIEnvironment

import wandb
#wandb.init(project='AnimalAI Agent', sync_tensorboard=True)
#

### Basic PPO agent + load config and watch.

training = False

if training:
    wandb.init(project="AnimalAI Agents", entity="kindsofintelligence", sync_tensorboard=True) 
    ## This will write to the KoI Wandb page. You must be logged in to a KoI team account on wandb for this to work. 

def train_agent_single_config(configuration_file):

    aai_env = AnimalAIEnvironment(
        seed = 123,
        file_name="../env/AnimalAI",
        arenas_configurations=configuration_file,
        play=False,
        base_port=5000,
        inference=False,
        useCamera=True,
        resolution=72,
        useRayCasts=False,
        # raysPerSide=1,
        # rayMaxDegrees = 30,
    )

    # env = UnityToGymWrapper(aai_env, uint8_visual=False, allow_multiple_obs=True, flatten_branched=False)
    # def make_env():
    #     def _thunk():
    #         env = UnityToGymWrapper(aai_env, uint8_visual=False, allow_multiple_obs=True, flatten_branched=True)
    #         return env
    #     return _thunk
    # env = DummyVecEnv([make_env()])
    env = UnityToGymWrapper(aai_env, uint8_visual=True, allow_multiple_obs=False, flatten_branched=True)
    runname = "72Px"

    policy_kwargs = dict(activation_fn=th.nn.ReLU)
    model = PPO("CnnPolicy", env, policy_kwargs=policy_kwargs, verbose=1, tensorboard_log=("./ppo_tensorboard/" + runname))

    no_saves = 100
    no_steps = 1000000
    reset_num_timesteps = True
    for i in range(no_saves):
        model.learn(no_steps, reset_num_timesteps=reset_num_timesteps, callback=WandbCallback())
        model.save("results/" + runname + "/model_" + str( (i+1)*no_steps ))
        reset_num_timesteps = False
    env.close()


def watchModel(configuration_file):
    aai_env = AnimalAIEnvironment(
        seed = 123,
        file_name="../env/AnimalAI",
        arenas_configurations=configuration_file,
        play=False,
        base_port=5000,
        inference=True,
        useCamera=True,
        resolution=72,
        useRayCasts=False,
        # raysPerSide=1,
        # rayMaxDegrees = 30,
    )

    # env = UnityToGymWrapper(aai_env, uint8_visual=False, allow_multiple_obs=True, flatten_branched=False)
    # def make_env():
    #     def _thunk():
    #         env = UnityToGymWrapper(aai_env, uint8_visual=False, allow_multiple_obs=True, flatten_branched=True)
    #         return env
    #     return _thunk
    # env = DummyVecEnv([make_env()])
    env = UnityToGymWrapper(aai_env, uint8_visual=True, allow_multiple_obs=False, flatten_branched=True)
    runname = "Runs"

    policy_kwargs = dict(activation_fn=th.nn.ReLU)
    model =  PPO.load("results/72Px/model_6000000")
    for run in range(0, 100):
        obs = env.reset()
        done=False
        while not done:
            action, _states = model.predict(obs)
            obs, rewards, done, info = env.step(action)
            env.render()

    
# Loads a random competition configuration unless a link to a config is given as an argument.
if __name__ == "__main__":
    if len(sys.argv) > 1:
        configuration_file = sys.argv[1]
    else:   
        competition_folder = "../configs/basic/"
        configuration_files = os.listdir(competition_folder)
        configuration_random = random.randint(0, len(configuration_files))
        configuration_file = (
            competition_folder + "1g.yml"#configuration_files[configuration_random]
        )
    if training:
        train_agent_single_config(configuration_file=configuration_file)
    else:
        watchModel(configuration_file=configuration_file)
    wandb.finish()
