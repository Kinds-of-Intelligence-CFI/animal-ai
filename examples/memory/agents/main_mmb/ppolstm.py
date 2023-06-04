from sb3_contrib import RecurrentPPO
import torch as th
import random, os, sys
from gym_unity.envs import UnityToGymWrapper
from animalai.envs.environment import AnimalAIEnvironment
import numpy as np

#tensorboard --logdir lstm_tensorboard_MOVINGBALL_train

from stable_baselines3.common.env_util import make_vec_env
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
        )
    env = UnityToGymWrapper(aai_env, uint8_visual=True, allow_multiple_obs=False, flatten_branched=True)

    runname = "MMB_L"
    policy_kwargs = dict(activation_fn=th.nn.ReLU, enable_critic_lstm=False, lstm_hidden_size=32)
    model = RecurrentPPO("CnnLstmPolicy", env, policy_kwargs=policy_kwargs, verbose=1, tensorboard_log=("./lstm_tensorboard_MOVINGBALL_train/" + runname), n_steps=512, batch_size=128, gamma=0.999, gae_lambda=0.94,learning_rate=1e-5)

    no_saves = 10
    no_steps = 250000
    reset_num_timesteps = False

    results_path = "results_MMB_lstm"
    if not os.path.exists(results_path):
        os.makedirs(results_path)

    for i in range(no_saves):
        model.learn(no_steps, reset_num_timesteps=False)
        save_path = os.path.join(results_path, "model_" + str((i+1)*no_steps))
        model.save(save_path)
        reset_num_timesteps = False
    env.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        configuration_file = sys.argv[1]
    else:   
        competition_folder = "../configs/basic/memory/"
        configuration_files = os.listdir(competition_folder)
        configuration_random = random.randint(0, len(configuration_files))
        configuration_file = (
            competition_folder + "movingball.yml" 
        )

        train_agent_single_config(configuration_file=configuration_file)
        print("Done with Training file")