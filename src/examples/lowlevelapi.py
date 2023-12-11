import sys
import random
import os

from animalai.envs.environment import AnimalAIEnvironment
from animalai.envs.braitenberg import Braitenberg

def run_agent_single_config(configuration_file: str) -> None:
    """
    Loads a configuration file for a single arena and gives some example usage of mlagent python Low Level API
    See https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Python-API.md for details.
    For demo purposes uses a simple braitenberg vehicle-inspired agent that solves most tasks from category 1.
    """
    env_path = "../env/AnimalAI"
    
    configuration = configuration_file

    totalRays = 9
    env = AnimalAIEnvironment(
        file_name=env_path,
        arenas_configurations=configuration,
        seed = 0,
        play=False,
        useCamera=False, #The Braitenberg agent works with raycasts
        useRayCasts=True,
        raysPerSide=int((totalRays-1)/2),
        rayMaxDegrees = 30,
    )
    print("Environment Loaded")

    braitenbergAgent = Braitenberg(totalRays) #A simple BraitenBerg Agent that heads towards food items.
    behavior = list(env.behavior_specs.keys())[0] # by default should be AnimalAI?team=0
    
    firststep = True
    for _episode in range(2): #Run episodes with the Braitenberg-style agent
        if firststep:
            env.step() # Need to make a first step in order to get an observation.
            firstep = False
        dec, term = env.get_steps(behavior)
        done = False
        episodeReward = 0
        while not done:
            raycasts = env.get_obs_dict(dec.obs)["rays"] # Get the raycast data
            # print(braitenbergAgent.prettyPrint(raycasts)) #print raycasts in more readable format
            action = braitenbergAgent.get_action(raycasts)
            # print(action)
            env.set_actions(behavior, action.action_tuple)
            env.step()      
            dec, term = env.get_steps(behavior)
            if len(dec.reward) > 0:
                episodeReward += dec.reward
            if len(term) > 0: #Episode is over
                episodeReward += term.reward
                print(F"Episode Reward: {episodeReward}")
                done = True
                firststep = True

    env.close()
    print("Environment Closed")
       
# Loads a random competition configuration unless a link to a config is given as an argument.
if __name__ == "__main__":
    if len(sys.argv) > 1:
        configuration_file = sys.argv[1]
    else:
        competition_folder = "../configs/competition/"
        configuration_files = os.listdir(competition_folder)
        configuration_random = random.randint(0, len(configuration_files))
        configuration_file = (
            competition_folder + configuration_files[configuration_random]
        )
    run_agent_single_config(configuration_file=configuration_file)


# # # # # # # # # #
# # Observation examples
# obs = (env.get_steps(behavior)[0].obs)
# print(obs)
# o = env.getDict(obs)
# print(o["camera"])
# print(o["rays"])
# print("health: " + str(o["health"]))
# print("velocity: " + str(o["velocity"]))
# print("position: " + str(o["position"]))
# sys.exit()
# # # # # # # # # #

    