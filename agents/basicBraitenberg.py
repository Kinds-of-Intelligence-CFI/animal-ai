import argparse
import os
import random
import numpy as np

from animalai.envs.actions import AAIActions, AAIAction
from animalai.envs.environment import AnimalAIEnvironment
from animalai.envs.raycastparser import RayCastParser
from animalai.envs.raycastparser import RayCastObjects

class Braitenberg():
    """Implements a simple heuristic agent (Braitenberg Vehicle)
    It heads towards good goals and away from bad goals.
    It navigates around immoveable objects directly ahead 
    If it is stationary it turns around
    """
    def __init__(self, no_rays, max_degrees, verbose=False):
        self.verbose = verbose # do you want to see the observations and actions?
        self.no_rays = no_rays # how many rays should the agent have?
        assert(self.no_rays % 2 == 1), "Number of rays must be an odd number." 
        self.max_degrees = max_degrees # how many degrees do you want the rays spread over?
        """
        We specify six types of objects here. This set can be expanded to include more objects if you wish to design further rules.
        """
        self.listOfObjects = [RayCastObjects.ARENA, 
                              RayCastObjects.IMMOVABLE, 
                              RayCastObjects.MOVABLE, 
                              RayCastObjects.GOODGOAL, 
                              RayCastObjects.GOODGOALMULTI, 
                              RayCastObjects.BADGOAL]
        
        self.raycast_parser = RayCastParser(self.listOfObjects, self.no_rays) #initialize a class to parse raycasts for these objects
        self.actions = AAIActions() # initalise the action set
        self.prev_action = self.actions.NOOP # initialise the first action, chosen to be forwards 

    def prettyPrint(self, obs) -> str:
        """Prints the parsed observation"""
        return self.raycast_parser.prettyPrint(obs) #prettyprints the observation in a nice format
    
    def checkStationarity(self, raycast): #checks whether the agent is stationary by examining its velocities. If they are below 1 in all directions, it turns.
        vel_observations = raycast['velocity']
        if self.verbose:
            print("Velocity observations")
            print(vel_observations)
        bool_array = (vel_observations <= np.array([1,1,1]))
        if sum(bool_array) == 3:
            return True
        else:
            return False
    
    def get_action(self, observations) -> AAIAction: #select an action based on observations
        """Returns the action to take given the current parsed raycast observation and other observations"""
        obs = self.raycast_parser.parse(observations)
        if self.verbose:
            print("Raw Raycast Observations:")
            print(obs)
            print("Pretty Raycast Observations:")
            self.raycast_parser.prettyPrint(observations)

        newAction = self.actions.FORWARDS.action_tuple #initialise the new action to be no action

        """
        If the agent is stationary, and it hasn't previously gone forwardsleft or forwardsright, it must be the first step. So choose one of those actions at random (p(0.5))
        """
        if self.checkStationarity(observations) and self.prev_action != self.actions.FORWARDSLEFT and self.prev_action != self.actions.FORWARDSRIGHT:
            select_LR = random.randint(0,1)
            if select_LR == 0:
                newAction = self.actions.FORWARDSLEFT
            else:
                newAction = self.actions.FORWARDSRIGHT
        elif self.checkStationarity(observations) and self.prev_action == self.actions.FORWARDSLEFT: # otherwise if stationary, continue in the same direction (it must be stuck by an obstacle)
            newAction = self.actions.FORWARDSLEFT
        elif self.checkStationarity(observations) and self.prev_action == self.actions.FORWARDSRIGHT:
            newAction = self.actions.FORWARDSRIGHT
        elif self.ahead(obs, RayCastObjects.GOODGOALMULTI) and not self.checkStationarity(observations): #if it's not stationary and it sees a good goal ahead, go forwards
            newAction = self.actions.FORWARDS
        elif self.left(obs, RayCastObjects.GOODGOALMULTI) and not self.checkStationarity(observations): # if it's to the left, rotate left
            newAction = self.actions.LEFT
        elif self.right(obs, RayCastObjects.GOODGOALMULTI) and not self.checkStationarity(observations): # if it's to the right, rotate right
            newAction = self.actions.RIGHT
        elif self.ahead(obs, RayCastObjects.GOODGOAL) and not self.checkStationarity(observations): #as above for good goals
            newAction = self.actions.FORWARDS
        elif self.left(obs, RayCastObjects.GOODGOAL) and not self.checkStationarity(observations):
            newAction = self.actions.LEFT
        elif self.right(obs, RayCastObjects.GOODGOAL) and not self.checkStationarity(observations):
            newAction = self.actions.RIGHT
        elif self.ahead(obs, RayCastObjects.BADGOAL) and not self.checkStationarity(observations): #the opposite for bad goals
            newAction = self.actions.BACKWARDS
        elif self.left(obs, RayCastObjects.BADGOAL) and not self.checkStationarity(observations):
            newAction = self.actions.RIGHT
        elif self.right(obs, RayCastObjects.BADGOAL) and not self.checkStationarity(observations):
            newAction = self.actions.LEFT
        elif self.ahead(obs, RayCastObjects.IMMOVABLE) and not self.checkStationarity(observations): # if there is an obstacle ahead move forwardsleft or forwardsright randomly to start navigating around it
            select_LR = random.randint(0,1)
            if select_LR == 0:
                newAction = self.actions.FORWARDSLEFT
            else:
                newAction = self.actions.FORWARDSRIGHT
        # Otherwise, if there is an obstacle ahead and the previous action was forwardsleft OR if there is an obstacle to the left and nothing ahead and the agent is not stationary, continue forwardsleft to continue navigating around
        elif ((self.ahead(obs, RayCastObjects.IMMOVABLE) and self.prev_action == self.actions.FORWARDSLEFT) or (self.left(obs, RayCastObjects.IMMOVABLE) and not self.ahead(obs, RayCastObjects.IMMOVABLE))) and not self.checkStationarity(observations):
            newAction = self.actions.FORWARDSLEFT
        # vice versa for if the right side. This way the agent can navigate around obstacles
        elif ((self.ahead(obs, RayCastObjects.IMMOVABLE) and self.prev_action == self.actions.FORWARDSRIGHT) or (self.right(obs, RayCastObjects.IMMOVABLE) and not self.ahead(obs, RayCastObjects.IMMOVABLE))) and not self.checkStationarity(observations):
            newAction = self.actions.FORWARDSRIGHT
        else: #otherwise, continue the same action as before
            newAction = self.prev_action        
        self.prev_action = newAction
        
        if self.verbose:
            print("Action selected:")
            print(newAction.name)
        newActionTuple = newAction.action_tuple
        
        return newActionTuple
    
    def ahead(self, obs, object): #returns a true if the object is detected in the middle ray.
        """Returns true if the input object is ahead of the agent"""
        if(obs[self.listOfObjects.index(object)][int((self.no_rays-1)/2)] > 0):
            if self.verbose:
                print("found " + str(object) + " ahead")
            return True
        return False

    def left(self, obs, object): #returns a true if the object is in one of the left rays
        """Returns true if the input object is left of the agent"""
        for i in range(int((self.no_rays-1)/2)):
            if(obs[self.listOfObjects.index(object)][i] > 0):
                if self.verbose:
                    print("found " + str(object) + " left")
                return True
        return False

    def right(self, obs, object): #returns a true if the object is in one of the right rays
        """Returns true if the input object is right of the agent"""
        for i in range(int((self.no_rays-1)/2)):
            if(obs[self.listOfObjects.index(object)][i+int((self.no_rays-1)/2) + 1] > 0):
                if self.verbose:
                    print("found " + str(object) + " right")
                return True
        return False

"""
A helper function to watch the agent on a single config.
You must run this config from the agents directory.
"""

def watch_braitenberg_agent_single_config(configuration_file: str, agent: Braitenberg):
    
    try:
        port = 4000 + random.randint(
            0, 1000
            )  # use a random port to avoid problems if a previous version exits slowly
        
        aai_env = AnimalAIEnvironment( 
        inference=True, #Set true when watching the agent
        seed = 123,
        worker_id=random.randint(0, 65500),
        file_name="../env/AnimalAI",
        arenas_configurations=configuration_file,
        base_port=port,
        useCamera=False,
        useRayCasts=True,
        raysPerSide = int((agent.no_rays)/2),
        rayMaxDegrees = agent.max_degrees
        )

        behavior = list(aai_env.behavior_specs.keys())[0] # by default should be AnimalAI?team=0

        done = False
        episodeReward = 0

        aai_env.step() # take first step to get an observation

        dec, term = aai_env.get_steps(behavior)
    
        while not done:

            observations = aai_env.get_obs_dict(dec.obs)

            action = agent.get_action(observations)

            aai_env.set_actions(behavior, action)

            aai_env.step()

            dec, term = aai_env.get_steps(behavior)
            
            if len(dec.reward) > 0 and len(term) <= 0:
                episodeReward += dec.reward

            elif len(term) > 0: #Episode is over
                episodeReward += term.reward
                print(f"Episode Reward: {episodeReward}")
                done = True
            
            else:
                pass

        aai_env.close()
    except:
        print("Try again. Looks like that port was busy. Sometimes it takes a while for the environment to close properly.")

        
    
        




if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--config_file", 
                        type=str, 
                        help="What config file should be run? Defaults to a random file from the competition folder.")
    
    parser.add_argument("--no_rays", 
                        type=int, 
                        help="How many rays should the raycaster produce? Must be an odd number. Defaults to 11.",
                        default = 11)
    parser.add_argument("--max_degrees", 
                        type=int, 
                        help = "Over how many degrees ought the raycasts be distributed? Defaults to 60.",
                        default = 60)
    parser.add_argument("--verbose", 
                        type=bool, 
                        help = "Do you want to print out observations and actions? Defaults to False.",
                        default = False)
    
    args = parser.parse_args()

    no_rays = args.no_rays 
    max_degrees = args.max_degrees
    verbose = args.verbose

    if args.config_file is not None:
        configuration_file = args.config_file
    else:
        config_folder = "../configs/competition/"
        configuration_files = os.listdir(config_folder)
        configuration_random = random.randint(0, len(configuration_files))
        configuration_file = config_folder + configuration_files[configuration_random]
        print(f"Using configuration file {configuration_file}")

    singleEpisodeVanillaBraitenberg = Braitenberg(no_rays=no_rays,
                                             max_degrees=max_degrees,
                                             verbose = verbose)
    
    watch_braitenberg_agent_single_config(configuration_file=configuration_file, agent = singleEpisodeVanillaBraitenberg)