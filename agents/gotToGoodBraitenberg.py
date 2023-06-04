from animalai.envs.actions import AAIActions, AAIAction
from animalai.envs.raycastparser import RayCastParser
from animalai.envs.raycastparser import RayCastObjects

class Braitenberg():
    """Implements a simple Braitenberg vehicle agent that heads towards food
    Can change the number of rays but only responds to GOODGOALs, GOODGOALMULTI and BADGOAL"""
    def __init__(self, no_rays):
        self.no_rays = no_rays
        assert(self.no_rays % 2 == 1), "Only supports odd number of rays (but environment should only allow odd number"
        self.listOfObjects = [RayCastObjects.GOODGOAL, RayCastObjects.GOODGOALMULTI, RayCastObjects.BADGOAL, RayCastObjects.IMMOVABLE, RayCastObjects.MOVABLE]
        self.raycast_parser = RayCastParser(self.listOfObjects, self.no_rays)
        self.actions = AAIActions()
        self.prev_action = self.actions.NOOP

    def prettyPrint(self, obs) -> str:
        """Prints the parsed observation"""
        return self.raycast_parser.prettyPrint(obs)
    
    def get_action(self, obs) -> AAIAction:
        """Returns the action to take given the current parsed raycast observation"""
        obs = self.raycast_parser.parse(obs)
        newAction = self.actions.NOOP
        if self.ahead(obs, RayCastObjects.GOODGOALMULTI):
            newAction = self.actions.FORWARDS
        elif self.left(obs, RayCastObjects.GOODGOALMULTI):
            newAction = self.actions.FORWARDSLEFT
        elif self.right(obs, RayCastObjects.GOODGOALMULTI):
            newAction = self.actions.FORWARDSRIGHT
        elif self.ahead(obs, RayCastObjects.GOODGOAL):
            newAction = self.actions.FORWARDS
        elif self.left(obs, RayCastObjects.GOODGOAL):
            newAction = self.actions.FORWARDSLEFT
        elif self.right(obs, RayCastObjects.GOODGOAL):
            newAction = self.actions.FORWARDSRIGHT
        elif self.ahead(obs, RayCastObjects.BADGOAL):
            newAction = self.actions.BACKWARDS
        elif self.left(obs, RayCastObjects.BADGOAL):
            newAction = self.actions.BACKWARDSLEFT
        elif self.right(obs, RayCastObjects.BADGOAL):
            newAction = self.actions.BACKWARDSRIGHT
        else:
            if self.prev_action == self.actions.NOOP or self.prev_action == self.actions.BACKWARDS:
                newAction = self.actions.LEFT
            else:
                newAction = self.prev_action    
        self.prev_action = newAction
        return newAction

    def ahead(self, obs, object):
        """Returns true if the input object is ahead of the agent"""
        if(obs[self.listOfObjects.index(object)][int((self.no_rays-1)/2)] > 0):
            # print("found " + str(object) + " ahead")
            return True
        return False

    def left(self, obs, object):
        """Returns true if the input object is left of the agent"""
        for i in range(int((self.no_rays-1)/2)):
            if(obs[self.listOfObjects.index(object)][i] > 0):
                # print("found " + str(object) + " left")
                return True
        return False

    def right(self, obs, object):
        """Returns true if the input object is right of the agent"""
        for i in range(int((self.no_rays-1)/2)):
            if(obs[self.listOfObjects.index(object)][i+int((self.no_rays-1)/2) + 1] > 0):
                # print("found " + str(object) + " right")
                return True
        return False