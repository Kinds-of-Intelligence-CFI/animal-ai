# Training Agents in Animal-AI

#### Table of Contents

1. [Introduction](#introduction)
2. [Agent Observations](#agent-observations)
3. [Python Low Level API: Braitenberg Agent Example](#python-low-level-api-braitenberg-agent-example)
4. [gymwrapper.py](#gymwrapperpy)
5. [trainaai.py](#trainaaipy)


## Introduction
We expect everyone will have a different setup for training agents. Here you can find two ways to wrap or use the environment as a standard reinforcement learning task. You can use a gym wrapper to wrap the environment for use with your favourite deep learning library. You can also use Unity ml-agents custom training scripts directly.


# Agent Observations

The agent currently has access to a Camera, Raycasts, and Extra Observations. You can disable either the camera or raycasts (or both). The enabled observations are ordered in an array with Camera first (if enabled), then raycasts (if enabled), then the extra observations.

The observation space is a vector of floats of length 3 * resolution * resolution (if camera is enabled) + 8 * (2*raysPerSide + 1) (if raycasts are enabled) + 7 (if extra observations are enabled).

## Camera Observations

With the camera enabled (via useCamera) the agent receives 1st-person pixel observations of its environment with configurable (square) resolution (via resolution parameter). Grayscale can be toggled on/off.

The camera is a standard Unity camera and so the observations are in the standard Unity format. The camera is set to render in the "RenderTexture" format. This is a 2D array of floats with values between 0 and 1. The array is of shape (resolution, resolution, 3) where the 3 channels are RGB. The array is flattened into a vector of length 3 * resolution * resolution. The first resolution * resolution elements are the red channel, the next resolution * resolution elements are the green channel, and the final resolution * resolution elements are the blue channel.


## Raycast observations

Raycasts are implemented to make it easier to work with a wide range of algorithms within AnimalAI. They are not designed to compete with pixel inputs as they naturally contain much less information about the environment. Nevertheless, they can be extremely useful for prototyping and for testing certain cognitive abilities or when analysing network dynamics compared to performance on many tasks. They can also be used as an auxilliary input or to help learn a more symbolic-like representation of the environment.

There are four relevant arguments to pass to the environment when using raycasts. See the lowLevelAPI.py script for examples.
* useCamera: set to false if you do not also want pixel observations
* useRayCasts: set to true to use raycast observations
* raysPerSide: sets the number of rays to cast to the left and right of the central one. e.g raysPerSide=2 means 5 rays total
* rayMaxDegrees: sets the maximum degrees for the left/right rays. e.g. 90 means the agent casts rays exactly to the left and right. other rays are spaced equally between the center and the max.

There are currently 6 types of objects that the rays report. This is intentional to keep the observation space down, but does limit the types of problem solvable. In order they are:
* arena: this is the outside of the arena and should usually be hit by a ray if it misses other objects (this is useful for the distance)
* Immovable: Inner Walls, Cylinders, ramps i.e. all the objects listed under immovable [here](definitionsOfObjects.md)
* Movable: Cardboxes and L/U objects i.e. all the objects listed as movable [here](definitionsOfObjects.md)
* goodGoal: A green goal
* goodGoalMulti: A yellow goal
* badGoal: Both red goals and death zones.

Note that this means that ramps and transparent objects are not distinguished from opaque walls, thus limiting the number of tasks it is possible for a raycast only agent to solve. This set may be extended in future versions.

For each ray:
* The first 6 elements of the returned observation are a one-hot vector for the type of object hit (ordered as above).
* The next element is 0 if the ray hit something (1 otherwise).
* The next element is the normalised distance to the object that was hit.

So the full observation space is of size 8 * (2*raysPerSide + 1)

Note that Unity implementation of rays orders the central ray first and then each ray (left or negative offset first) in increasing distance from the centre as follows:

```
  1 0 2
   \|/
3 --@-- 4
```

AnimalAI contains a [helper class](../../src/animalai/envs/raycastparser.py) as a starting point for manipulating raycasts. This class contains a function to convert the raycast observation into a more readable format. The class also contains a function to convert the raycast observation into a 2D array of floats. This can be useful for some algorithms that expect a 2D array of floats as input. The 2D array is of shape (2*raysPerSide + 1, 3) where the first raysPerSide rows are the left rays and the last raysPerSide rows are the right rays. The columns are the one-hot vector for the type of object hit, the hit flag, and the normalised distance to the object hit. The 2D array is flattened into a vector of length 8 * (2*raysPerSide + 1). The first 8 elements are the left rays, the next 8 elements are the right rays, and the final 8 elements are the central ray. The order of the elements within each ray is the same as the order in the 1D array. 

## Health, Velocity and Position

The agent also receives a vector of length 7 containing its health (1 float), velocity (x, y, z), and (global) position (x, y, z). The velocity and position are in the global coordinate system. The position is in the center of the agent. The velocity is in meters per second. The position is in meters. The health is a float between 0 and 1. The agent dies when its health reaches 0. The agent's health is reset to 1 at the start of each episode. The agent's velocity and position are reset to 0 at the start of each episode.

---
## gymwrapper.py

The example script `gymwrapper.py` shows a simple way to run an AnimalAI task using stable baselines 3. To run this you will also need to install stable-baselines3.

## trainaai.py

The example script `trainaai.py` shows how to run ml-agents training. Documentation for this can be found [here](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Training-ML-Agents.md). 

---
# Python Low Level API: Braitenberg Agent Example

AnimalAI is built with mlagents which provides a low level python API for interacting with agents. This tutorial shows how to run a hand-coded Braitenberg-style agent in AnimalAI using the low level API. This is intended mainly to show how the low level api works.

The low level API allows you to quickly setup a reward/observation loop for a particular configuration and to test or train agents.

For further documentation on the mlagents low level API see the Unithy docs [here](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Python-API.md).

## The lowlevelapi.py script.

You can find this script in the examples folder. If you run it, it will load a random competition configuration in agent mode and then run a Braitenberg agent through the configuration 3 times. The agent and environment are deterministic so you should find that the reward is the same all three times. 

The agent is pretty simple. It can solve quite a few tests in the competition by turning towards yellow and green objects and avoiding red ones. For example, it solves `01-05-01` (run `python lowlevelapi.py configs/competition/01-05-01.yaml`) very efficiently (Episode Reward: 0.91419995), but, of course, cannot solve any of the harder tasks in category 10 (those numbered `10-xx-0y`).

By default the screen size is set very small possible in agent mode. It is not needed by the agent (that instead works directly on the observations sent by the environment). Unfortunately, it is needed for unity to be able to render the environment so you cannot run it completely without this. If you really want to run headless and not use any camera observations it may be possible (see [here](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Executable.md)), but is not supported.

The first part of the lowlevelapi script sets up the environment:

```python
totalRays = 5
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
```

The Braitenberg agent uses the raycast sensor (see [here](observations.md) for a description). You can play around with the configuration, but if the rays are too far apart it will not be able to navigate successfully. 

The second part runs the episode and provides an initial example that can be used as a template for your own experiments:

```python
firststep = True
for _episode in range(3): #Run episodes with the Braitenberg-style agent
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
```
