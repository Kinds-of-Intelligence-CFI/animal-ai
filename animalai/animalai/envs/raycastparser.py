import enum
import numpy as np
"""Parses the raycast observations from AnimalAI and returns a shortened version with only relevant objects"""


class RayCastObjects(enum.Enum):
    """Enum for the parsed objects from the raycast. The order must match the order in the Unity environment."""
    ARENA = 0
    IMMOVABLE = 1
    MOVABLE = 2
    GOODGOAL = 3
    GOODGOALMULTI = 4
    BADGOAL = 5
    GOALSPAWNER = 6
    INNERWALL = 7
    OUTERWALL = 8
    DEATHZONE = 9
    HOTZONE = 10
    RAMP = 11
    PILLAR_BUTTON = 12


class RayCastParser():
    numberDetectableObjects = 13  # This is defined in the Unity environment
    """Parses the raycast observations from AnimalAI and returns a shortened version with only relevant objects
    replaces the one-hot vector with the distance to the object (if any were hit) 
    listOfObjects is an array of all the objects that you care about (as RayCAstObjects enum)
    also reorders the array so that it is read from left to right"""

    def __init__(self, listOfObjects, numberOfRays):
        """Initialize the parser"""
        self.numberOfRays = numberOfRays
        self.listOfObjects = listOfObjects
        self.listofObjectVals = [x.value for x in listOfObjects]
        self.numberOfObjects = len(listOfObjects)

    def parse(self, raycast) -> np.ndarray:
        """Parse the raycast
        input: the raycast direct from Unity
        output: a shortened version with only the object in listOfObjects
        output is an array with one row for every element of listOfObjects
        reordered to read fro left to right"""

        print(f"Initial raycast: {raycast}")
        print(f"List of Objects: {self.listOfObjects}")

        assert (len(raycast) == self.numberOfRays *
                (self.numberDetectableObjects+2))
        parsedRaycast = np.zeros((len(self.listOfObjects), self.numberOfRays))
        print(parsedRaycast)
        for i in range(self.numberOfRays):
            for j in range(self.numberDetectableObjects):
                if j in self.listofObjectVals:
                    if raycast[i * (self.numberDetectableObjects + 2) + j] == 1:
                        parsedRaycast[self.listofObjectVals.index(j)][i] = (
                            raycast[i * (self.numberDetectableObjects + 2) + self.numberDetectableObjects + 1])
                        print(
                            f"Detected object {j} at ray {i} with distance {raycast[i * (self.numberDetectableObjects + 2) + self.numberDetectableObjects + 1]}")
        # Change flattened array into matrix with one row per object in listOfObjects
        parsedRaycast = np.reshape(
            parsedRaycast, (len(self.listOfObjects), self.numberOfRays))
        reordered = np.zeros_like(parsedRaycast)
        for i in range(parsedRaycast.shape[0]):
            reordered[i] = self.reorderRow(parsedRaycast[i])

        print(f"parsedRaycast after parsing: {parsedRaycast}")
        print(f"Reordered Raycast: {reordered}")
        return reordered

    def reorderRow(self, row):
        """Reorders the row so instead of labelling from middle, lables from left to right"""
        newRow = np.zeros_like(row)
        midIndex = int((self.numberOfRays-1)/2)
        newRow[midIndex] = row[0]
        for i in range(midIndex):
            newRow[i+1+midIndex] = row[self.numberOfRays-2*(i+1)]
            newRow[i] = row[2*(i+1)]
        return newRow

    def prettyPrint(self, raycast) -> str:
        """Parses the raycast and outputs a human readable version"""
        parsedRaycast = self.parse(raycast)
        for i in range(parsedRaycast.shape[0]):
            print(self.listOfObjects[i].name, ":", parsedRaycast[i])


if __name__ == "__main__":
    """Test the parsing works
    Only a few sanity checks"""
    rayParser = RayCastParser(
        [RayCastObjects.GOODGOAL, RayCastObjects.IMMOVABLE], 5)
    parsedRaycast = rayParser.parse([1, 1, 1, 1, 1, 1, 0, 0.1,
                                     1, 1, 1, 1, 1, 1, 0, 0.2,
                                     1, 1, 1, 1, 1, 1, 1, 0.3,
                                     1, 1, 1, 1, 1, 1, 1, 0.4,
                                     1, 1, 1, 1, 1, 1, 1, 0.5])
    assert (np.array_equal(parsedRaycast, np.array(
        [[0.4, 0.2, 0.1, 0.3, 0.5], [0.4, 0.2, 0.1, 0.3, 0.5]])))
    rayParser = RayCastParser(
        [RayCastObjects.GOODGOAL, RayCastObjects.IMMOVABLE, RayCastObjects.BADGOAL], 3)
    parsedRaycast = rayParser.parse([0, 0, 0, 0, 0, 0, 0, 0.1,
                                     0, 0, 0, 0, 0, 0, 0, 0.2,
                                     0, 0, 0, 0, 0, 0, 1, 0.3])
    assert (np.array_equal(parsedRaycast, np.array(
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]])))
    rayParser = RayCastParser(
        [RayCastObjects.ARENA, RayCastObjects.MOVABLE, RayCastObjects.GOODGOALMULTI], 7)
    parsedRaycast = rayParser.parse([1, 0, 0, 0, 0, 0, 0, 0.1,
                                     0, 1, 0, 0, 0, 0, 0, 0.2,
                                     0, 0, 1, 0, 0, 0, 1, 0.3,
                                     0, 0, 0, 1, 0, 0, 1, 0.4,
                                     0, 0, 0, 0, 1, 0, 1, 0.5,
                                     0, 0, 0, 0, 0, 1, 1, 0.6,
                                     0, 0, 0, 0, 0, 0, 0, 0])
    assert (np.array_equal(parsedRaycast, np.array(
        [[0, 0, 0, 0.1, 0, 0, 0], [0, 0, 0, 0, 0.3, 0, 0], [0, 0, 0, 0, 0, 0.5, 0]])))
    rayParser = RayCastParser(
        [RayCastObjects.GOODGOAL, RayCastObjects.IMMOVABLE, RayCastObjects.GOALSPAWNER], 5)
    parsedRaycast = rayParser.parse([1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0.1,
                                     1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0.2,
                                     1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0.3,
                                     1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0.4,
                                     1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0.5])
    print(parsedRaycast)
    assert (np.array_equal(parsedRaycast, np.array([[0.4, 0.2, 0.1, 0.3, 0.5], [
            0.4, 0.2, 0.1, 0.3, 0.5], [0.4, 0.2, 0.1, 0.3, 0.5]])))
    rayParser = RayCastParser(
        [RayCastObjects.GOODGOAL, RayCastObjects.IMMOVABLE, RayCastObjects.PILLAR_BUTTON], 5)
    parsedRaycast = rayParser.parse([1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0.1,
                                     1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0.2,
                                     1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0.3,
                                     1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0.4,
                                     1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0.5])
    print(parsedRaycast)
