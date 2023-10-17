

# Arena Configuration Files

## TL;DR

From the `examples` folder, run `python play.py ../configs/competition/10-26-01.yaml` to get an understanding of how the `YAML` files configure the 
arenas for training. You will find a list of all objects you can add to an arena as well as the values for their parameters in [the definitions](definitionsOfObjects.md). You will find below all the technical details to create more complex training configurations.

## Intro
To configure training arenas you can use a simple **YAML file**. This makes training quite flexible and allows for the following:
- load and save configurations for reusability
- on the fly changes of configuration of one or more arenas between episodes, allowing for easy curriculum learning for example
- share and update configurations easily

We describe below the structure of the configuration files for an instance of the training environment, as well as all the parameters and the values they can take. 

## The Arenas

<p align="center">
  <img height="400" src="PrefabsPictures/Arena.png">
</p>

A single arena is as shown above, it comes with a single agent (spherical animal - currently hedgehog, pig, or panda), a floor and 
four walls. It is a square of size 40x40, the origin of the arena is `(0,0)`. You can provide coordinates for objects in the range `[0,40]x[0,40]` as floats.

Note that in Unity the **y** axis is the vertical axis. In the above picture with the agent on the ground in the center of the environment its coordinates are (20, 0, 20).

For each arena you can provide the following parameters and a list of objects to spawn:
- `t` an `int`, the length of an episode which can change from one episode to the other. A value of `0` means that the episode will 
not terminate until a reward has been collected (setting `t=0` and having no reward will lead to an infinite episode). This value is converted into a decay rate for the health of the agent. A `t` of 100 means that the agent's health will decay to 0, and the episode will end, after 100 time steps.
- 'pass_mark' an 'int', the reward threshold that should constitute a ‘pass’ in the enviroment. Leaving this parameter undefined leads to the default value of 0, whereby any reward value obtained by the Agent results in a pass. This parameter also determines the notifications that players receive at the end of an episode. If used, this parameter should be defined with consideration to the reward size that can feasibly be obtained by the Agent in each configuration file. 
- `blackouts` [see below](#blackouts)

## Objects

All objects can be configured in the same manner, using a set of parameters for each item:

- `name`: the name of the object you want to spawn.
- `positions`: a list of `Vector3` positions within the arena where you want to spawn items, if the list is empty the position will be sampled randomly in the arena. Any position dimension set to -1 will spawn randomly.
- `sizes`: a list of `Vector3` sizes, if the list is empty the size will be sampled randomly (within preset bounds for that particular object). You can set any size to -1 to spawn randomly along that dimension only.
- `rotations`: a list of `float` in the range `[0,360]`, if the list is empty the rotation is sampled randomly.
- `colors`: a list of `RGB` values (integers in the range `[0,255]`), if the list is empty the color is sampled randomly. Note that not all objects can have their colour changed and for those (e.g. transparent objects) this value will be ignored.

Any of these fields can be omitted in the configuration files, in which case the omitted fields are automatically randomized. Any Vector3 that contains a -1 for any of its dimensions will spawn that dimension randomly. This can be used to spawn, for example, multiple walls of a set width and height but random lengths. 

**All value ranges for the above fields can be found in [the definitions](definitionsOfObjects.md)**. If you go above or below the range for size it will automatically be set to the max or min respectively. If you try to spawn outside the arena (or overlapping with another object) then that object will not be spawned. Objects are placed in the order defined such that the second overlapping object is the one that does not spawn.

## Unique/Special Object Parameters
Some objects have unique/special parameters that only apply to them or a select few objects - they can be written in the configuration in exactly the same way as the 'standard' parameters, but will only be applied if assigned to a valid object:

- `skins`:
	- a list of animal names, denoting the 'skin' that is applied to the agent model.
	- **applies to:** `Agent` only
	- **defaults to:** `"random"` (is assigned any animal from the list)
	- **preset list:** `"panda"`, `"pig"`, `"hedgehog"`, `"random"` (more animals TBC)
- `delays`:
	- a list of `float` fixed-frame time delays before each object's special behaviour is initiated.
	- **applies to:** `DecayGoal`, `AntiDecayGoal`, `GrowGoal`, `ShrinkGoal`, `SpawnerTree`, `SpawnerDispenser`, `SpawnerContainer`
	- **defaults to:** `0`
- `initialValues`:
	- a list of `float` reward/size values used as a starting point where the reward/size changes over time.
	- **applies to:** `DecayGoal`, `AntiDecayGoal`, `GrowGoal`, `ShrinkGoal`, `SpawnerTree`
	- **defaults to:** `2.5` if decaying/shrinking goal; `0.5` if ripening/growing goal; `0.2` for initial size of fruit from tree spawners
- `finalValues`:
	- a list of `float` reward/size values used as an ending point where the reward/size changes over time.
	- **applies to:** `DecayGoal`, `AntiDecayGoal`, `GrowGoal`, `ShrinkGoal`, `SpawnerTree`
	- **defaults to:** `0.5` if decaying/shrinking goal; `2.5` if ripening/growing goal; `1.0` for size of ripened fruit from tree spawners
- `changeRates`:
	- a list of `float` rates of change at which an object's reward/size change occurs.
	- **applies to:** `DecayGoal`, `AntiDecayGoal`, `GrowGoal`, `ShrinkGoal`
	- **defaults to:** `0.005` (automatically adjusted to `-0.005` if decaying/shrinking)
- `spawnCounts`:
	- a list of `int` numbers of goals that will be spawned by each spawner.
	- **applies to:** `SpawnerTree`, `SpawnerDispenser`, `SpawnerContainer`
	- **defaults to:** `-1` (infinite number of goals will be spawned continuously)
- `spawnColors`:
	- a list of `RGB` values denoting the colour of spawned objects from each spawner.
	- **applies to:** `SpawnerTree`, `SpawnerDispenser`, `SpawnerContainer`
	- **defaults to:** *(varies according to which spawner is used)*
- `timesBetweenSpawns`:
	- a list of `float` time intervals (seconds) between which spawn events occur in each spawner.
	- **applies to:** `SpawnerTree`, `SpawnerDispenser`, `SpawnerContainer`
	- **defaults to:** `4.0` if spawner is a tree; `1.5` otherwise
- `ripenTimes`:
	- a list of `float` time durations (seconds) spawned goals will take to 'ripen' (grow in size) in a tree before falling to the ground - *(set to `0` for instant spawning, and for ripening without size growth, set initial/finalValues to be equal)*.
	- **applies to:** `SpawnerTree`
	- **defaults to:** `6.0`
- `doorDelays`:
	- a list of `float` time durations (seconds) for a dispenser/container-spawner's door to open, making spawned goals accessible.
	- **applies to:** `SpawnerDispenser`, `SpawnerContainer`
	- **defaults to:** `10.0`
- `timesBetweenDoorOpens`:
	- a list of `float` time intervals (seconds) for which a dispenser/container-spawner's door will open before closing again *(door closing after opening is calculated automatically)*.
	- **applies to:** `SpawnerDispenser`, `SpawnerContainer`
	- **defaults to:** `-1` (if `< 0` then, once opened, door stays open permanently)
- `symbolNames`:
	- a list of symbol names to be drawn on SignPosterboard objects. Can choose from a preset list, or specify a custom 'QR code'-style symbol (see [examples](#detailed-examples))
	- **applies to:** `SignPosterboard`
	- **defaults to:** `"default"` (if no name or invalid name given)
	- **preset list:** `"left-arrow"`, `"right-arrow"`, `"up-arrow"`, `"down-arrow"`, `"u-turn-arrow"`, `"letter-a"`, `"letter-b"`, `"letter-c"`, `"square"`, `"triangle"`, `"circle"`, `"star"`, `"tick"`, `"cross"`
- `frozenAgentDelays`:
	- a float that freezes the agent for the specified number of frames at the start of an episode. There is no reward decrement during the frozen period, and all other objects continue to move and interact.
	- **applies to:** `Agent` only
	- **defaults to:** `0`

## Blackouts

Blackouts are parameters you can pass to each arena, which define between which frames of an episode the lights are 
on or off. If omitted, this parameter automatically sets to have lights on for the entire episode. You can otherwise 
pass two types of arguments for this parameter:

- passing a list of frames `[5,10,15,20,25]` will start with the lights on, switch them off from frames 5 to 9 included, 
then back on from 15 to 19 included etc...
- passing a single negative argument `[-20]` will automatically switch lights on and off every 20 frames.

**Note**: for infinite episodes (where `t=0`), the first point above would leave the light off after frame `25` while the second point would keep switching the lights every `20` frames indefinitely.


## Rules and Notes
There are certain rules to follow when configuring an arena as well as some designs you should be aware of. If a 
configuration file does not behave as you expect make sure you're not breaking one of the following:

- Spawning objects:
    - **Objects can only spawn if they do not overlap with each other**. Attempting to spawn an object where another object already is will discard the latter.
    - The environment will attempt to spawn objects in the order they are provided in the file. In the case where any of the components is randomized we attempt to spawn the object **up to 20 times**. if no valid spawning spot is found the object is discarded.
    - Due to the above point, the first objects in the list are more likely to spawn than the last ones.
    - The `Agent` does not have to be provided in the configuration file, in which case it will spawn randomly.
    - If an `Agent` position is provided, be aware that the **agent spawns last** therefore it might cause problems if other objects randomly spawn where the agent should be.
    - In case an object is present where the `Agent` should spawn the arena resets and the process starts all over.
    - You can **spawn some objects on top of each others**, however be aware there is a `0.1` buffer automatically added to any height you provide (to make sure things fall on each other nicely). 

- Configuration file values:
    - Objects' `name` have to match one of the names provided in [the definitions](definitionsOfObjects.md), if the name provided is not found in this list, the object is ignored.
    - Any component of `positions`, `sizes` and `rotations` can be randomized by providing a value of `-1`.
    - Note that setting `positions.y = -1` will spawn the object at ground level.
    - Goals (except for the red zone) can only be scaled equally on all axes, therefore they will always remain spheres. If a `Vector3` is provided for the scale of a sphere goal only the `x` component is used to scale all axes equally.
