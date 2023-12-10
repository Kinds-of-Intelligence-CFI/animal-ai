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
