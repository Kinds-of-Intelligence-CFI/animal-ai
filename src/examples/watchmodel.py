from stable_baselines3 import PPO

from gym_unity.envs import UnityToGymWrapper
from animalai.envs.environment import AnimalAIEnvironment

def train_agent_single_config(configuration_file):
    
    base_port = 5000 if training else 5001

    # AnimalAI settings must be the same as used for training except with inference = true
    # best to load from a common config file
    aai_env = AnimalAIEnvironment( 
        inference=True, #Set true when watching the agent
        # seed = 123,
        # file_name="env/AnimalAI",
        # arenas_configurations=configuration_file,
        # play=False,
        # base_port=base_port,
        # useCamera=True,
        # resolution=36,
        # useRayCasts=True,
        # raysPerSide=1,
        # rayMaxDegrees = 30,
    )

    env = UnityToGymWrapper(aai_env, uint8_visual=False, allow_multiple_obs=True, flatten_branched=True)
    runname = "runname" #Assume you have your model saved in results/runname/
    model_no = "1234567890"

    model = PPO.load(F"results/{runname}/model_{model_no}")
    obs = env.reset()
    while True:
        action, _states = model.predict(obs, deterministic=True)
        obs, reward, done, info = env.step(action)
        # print(obs)
        env.render()
        if done:
            obs=env.reset()
    
if __name__ == "__main__":
    print("This is an example script that shows how you might load and watch a trained agent.")
    print("You will need to edit it for your needs.")

    # if len(sys.argv) > 1:
    #     configuration_file = sys.argv[1]
    # else:   
    #     competition_folder = "configs/competition/"
    #     configuration_files = os.listdir(competition_folder)
    #     configuration_random = random.randint(0, len(configuration_files))
    #     configuration_file = (
    #         competition_folder + configuration_files[configuration_random]
    #     )
    # train_agent_single_config(configuration_file=configuration_file)
