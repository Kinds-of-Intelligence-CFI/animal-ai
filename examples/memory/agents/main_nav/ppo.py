from stable_baselines3 import PPO
import torch as th
import sys, random, os, csv
from gym_unity.envs import UnityToGymWrapper
from animalai.envs.environment import AnimalAIEnvironment

### Basic PPO agent + load config and watch.
# tensorboard --logdir ppo_tensorboard_OCC_train
training = False

def train_agent_single_config(configuration_file):

    aai_env = AnimalAIEnvironment(
        seed = 123,
        file_name="env/AnimalAI",
        arenas_configurations=configuration_file,
        play=False,
        base_port=5000,
        inference=False,
        useCamera=True,
        resolution=72,
        useRayCasts=False,
    )

    env = UnityToGymWrapper(aai_env, uint8_visual=True, allow_multiple_obs=False, flatten_branched=True)
    
    runname = "OCC"
    policy_kwargs = dict(activation_fn=th.nn.ReLU)
    model = PPO("CnnPolicy", env, policy_kwargs=policy_kwargs, verbose=1, tensorboard_log=("./ppo_tensorboard_OCC_train/" + runname))

    no_saves = 10
    no_steps = 250000
    reset_num_timesteps = False

    results_path = "results_OCC_ppo"
    if not os.path.exists(results_path):
        os.makedirs(results_path)

    for i in range(no_saves):
        model.learn(no_steps, reset_num_timesteps=False)
        save_path = os.path.join(results_path, "model_" + str((i+1)*no_steps))
        model.save(save_path)
        reset_num_timesteps = False
    env.close()

def watchModel(configuration_file):
    aai_env = AnimalAIEnvironment(
        seed = 123,
        file_name="env/AnimalAI",
        arenas_configurations=configuration_file,
        play=False,
        base_port=5000,
        inference=False,
        useCamera=True,
        resolution=72,
        useRayCasts=False,
    )

    env = UnityToGymWrapper(aai_env, uint8_visual=True, allow_multiple_obs=False, flatten_branched=True)

    rewards_list = []
    model =  PPO.load("saved_model/results_MMB_ppo/model_2500000")

    for run in range(0, 100):
        obs = env.reset()
        done=False
        sum_rewards = 0
        
        while not done:
            action, _states = model.predict(obs)
            obs, rewards, done, info = env.step(action.item())
            sum_rewards += rewards
            env.render()
        rewards_list.append(sum_rewards)  

    return rewards_list  

# Loads a random competition configuration unless a link to a config is given as an argument.
if __name__ == "__main__":
    if len(sys.argv) > 1:
        configuration_file = sys.argv[1]
    else:   
        competition_folder = "configs/basic/occlusion/"
        configuration_files = os.listdir(competition_folder)
        configuration_random = random.randint(0, len(configuration_files))
        configuration_file = (
            competition_folder + "arena-train.yml" 
        )
    
    if training:
        train_agent_single_config(configuration_file= configuration_file)
        print("Done with Training file")
    else:
        folder = "configs/basic/occlusion/arena-train.yml"
        file_name = folder.split("/")[-1].split(".")[0] + "_PPOresults.csv"

        returns = watchModel(configuration_file=folder)  
        
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['returns'])
            writer.writerow([returns])
        csvfile.close()
        
        print("Done with yaml file")