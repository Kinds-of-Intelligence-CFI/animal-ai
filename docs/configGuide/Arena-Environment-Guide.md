# Arena Environment Guide

### Table of Contents
1. [TL;DR](#tldr)
2. [Introductions](#introductions)
3. [The Arena](#the-arena)
4. [Objects](#objects)
5. [Unique/Special Object Parameters](#uniquespecial-object-parameters)
6. [Blackouts](#blackouts)
7. [Rules and Notes for Arena Configuration](#rules-and-notes-for-arena-configuration)

## TL;DR

From the `examples` folder, run `python play.py ../configs/competition/10-26-01.yaml` to get an understanding of how the `YAML` files configure the arenas for training. You will find a list of all usable objects you can add to an arena as well as the default and optional values for their parameters in the [Arena Object Definitions](ArenaObjectDefinitions.md) guide. You will find below all the technical details to create more complex configurations. A background guide to using YAML is available [here](docs\Background-YAML.md).

## Introductions

To configure custom training arenas you can use a simple **YAML file**. This makes training quite flexible is user readable, and allows for the following:
- load and save configurations for reusability
- on the fly changes of configuration of one or more arenas between episodes, allowing for easy curriculum learning as an for example
- share and update configurations easily
- very easy to use and understand
- small file size

We describe below the structure of the configuration files for an instance of the training environment, as well as all the parameters and the values they can take. 

## The Arena

<p align="center">
  <img height="300" src="C:\Users\ia424\Desktop\animal-ai\docs\media\prefabs\DefaultArena.png">
</p>

A default arena instance is shown above, with just the arena and agent is spawned. Currently, any arena can only support a single agent (spherical animal skins - currently hedgehog, pig, or panda), a floor and four arena containing walls. It is currently a square of fixed size 40x40, with the origin of the arena is set to `(0,0)`. You can provide coordinates for objects in the range `[0,40]x[0,40]` as floats.

<p align="center">
  <img height="200" src="C:\Users\ia424\Desktop\animal-ai\docs\media\prefabs\Referential.png">
</p>

Note that in Unity the **y** axis is the vertical axis. In the above picture with the agent on the ground in the center of the environment its coordinates are `(20, 0, 20)`.

For each arena you can provide the following parameters (below configuration is an example of how each are used and their placement in the config file):

```YAML
!ArenaConfig
randomizeArenas: false # whether to randomize arenas from the beginning. Default is false.
showNotification: false # show/hide the notification box. Default is false.
canResetEpisode: true # allow the user to change the perspective. Default is true.
canChangePerspective: true # allow the user to change the perspective. Default is true.
arenas:
  0: !Arena
    pass_mark: 0
    t: 250
    items:
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 20, y: 0, z: 20}
      rotations: [0]
```

- `t` an `int`, defines the length of an episode which can change from one episode to the other. A value of `0` means that the episode will not terminate until a reward has been collected (setting `t=0` and having no reward will lead to an infinite episode). This value is converted into a decay rate for the health of the agent. A `t` of 100 means that the agent's health will decay to 0, and the episode will end, after 100 time steps.
- `pass_mark` an `int`, defines the reward threshold that should constitute a ‘pass’ in the enviroment. Leaving this parameter undefined leads to the default value of 0, whereby any reward value obtained by the Agent results in a pass. This parameter also determines the notifications that players receive at the end of an episode. If used, this parameter should be defined with consideration to the reward size that can feasibly be obtained by the agent in each configuration file.
- `canChangePerspective` a `bool`, defines whether the agent can change its camera perspective during an episode (first-person, third-person or eagle-view). If set to `false`, the agent will be unable to change its camera perspective during an episode by pressing the C button on their keyboards, which will cycle through the cameras attached to the Agent in-gasme. If set to `true`, the agent will be able to change its perspective during an episode. This parameter is set to `true` by default.
- `randomizeArenas` a `bool`, defines whether the arena will be randomized between episodes. If set to `true`, the arena will be randomized between the defined Arenas in the configuration file. If set to `false`, the order to which the arenas are spawned are sequential and top-to-bottom as specified in the configuration file. This parameter is set to `false` by default.
- `showNotification` a `bool`, defines whether the player will receive a notification at the end of an episode. If set to `true`, the player will be shown a notification at the end of an episode for approximately 2.5 seconds, then move on to the next episode (arena). If set to `false`, the agent will not receive a notification at the end of an episode and episode-to-episode termination is back-to-back. This parameter is set to `false` by default.
- `blackouts` [see here](#blackouts)

**N.B.** These parameters are optional (except `t` and `pass_mark`) and can be omitted from the configuration file. If omitted, the default values will be used.

## Objects

All objects can be configured in the same manner, using a set of parameters for each `item` unity object:

- `name`: the name of the object you want to spawn, which must match the object name specified in [object definitions](definitionsOfObjects.md). You can spawn the same object as many times as required, but they must be in different positions from one another (see below)
- `positions`: a list of `Vector3` positions within the arena where you want to spawn items, if the list is empty the position will be sampled randomly in the arena. Any position vector set to -1 will spawn randomly. Also note that Animal-AI enforces a constraint where objects cannot spawn within 0.1 units of each other, so if you try to spawn objects too close together there will be object collision clashes and the objects will not spawn.
- `sizes`: a list of `Vector3` sizes, if the list is empty the size will be sampled randomly (within preset bounds for that particular object). You can set any size to -1 to spawn randomly along that vector only.
- `rotations`: a list of `float` in the range `[0,360]`, if the list is empty the rotation is sampled randomly. Default is 0 degrees.
- `colors`: a list of `RGB` values (integers in the range `[0,255]`), if the list is empty the color is sampled randomly. Note that not all objects can have their colour changed and for those (e.g. transparent objects) this value will be ignored.

**N.B.** Any of these parameters can be omitted in the configuration files per object, in which case the omitted fields are automatically randomized. However, we advise that you specify these parameters as this will allow you to have a more controlled environment in your arena(s). Any Vector3 that contains a -1 for any of its dimensions will spawn that dimension randomly `(e.g. x: -1, y: 10, z: 2 --> will spawn the object randomly along the x axis)`. Finally, some objects have specific parameters applicable only to them, which are described in the [unique/special objects](#uniquespecial-object-parameters).

**All value ranges for the above fields can be found in [object definitions](definitionsOfObjects.md)**. If you go above or below the range for size it will automatically be set to the max or min respectively. If you try to spawn outside the arena (or overlapping with another object) then that object will not be spawned. Objects are placed in the order defined such that the second overlapping object is the one that does not spawn.

## Unique/Special Object Parameters
Some objects have unique/special parameters that only apply to them or a select few objects - they can be written in the configuration in exactly the same way as the 'standard' parameters, but will only be applied if assigned to a valid object:

### Agent-Specific Parameters
- **Skins**:
  List of animal skins for the agent model.
  - **Applies to:** Agent
  - **Default:** "random" (any animal from the list)
  - **Options:** "panda", "pig", "hedgehog", "random", etc.

- **Frozen Agent Delays**:
  Time (in frames) the agent is frozen at the start of an episode.
  - **Applies to:** Agent
  - **Default:** 0 (no delay)

### Goal-Related Parameters
- **Delays**:
  Time delay before special behavior initiation.
  - **Applies to:** DecayGoal, AntiDecayGoal, GrowGoal, ShrinkGoal, SpawnerTree, SpawnerDispenser, SpawnerContainer
  - **Default:** 0

- **Initial Values**:
  Starting reward/size values.
  - **Applies to:** DecayGoal, AntiDecayGoal, GrowGoal, ShrinkGoal, SpawnerTree
  - **Default:** Varies by goal type

- **Final Values**:
  Ending reward/size values.
  - **Applies to:** DecayGoal, AntiDecayGoal, GrowGoal, ShrinkGoal, SpawnerTree
  - **Default:** Varies by goal type

- **Change Rates**:
  Rate at which reward/size changes.
  - **Applies to:** DecayGoal, AntiDecayGoal, GrowGoal, ShrinkGoal
  - **Default:** 0.005 (negative for decaying/shrinking)

### Spawner Parameters
- **Spawn Counts**:
  Number of goals spawned.
  - **Applies to:** SpawnerTree, SpawnerDispenser, SpawnerContainer
  - **Default:** -1 (infinite)

- **Spawn Colors**:
  Color of spawned objects.
  - **Applies to:** SpawnerTree, SpawnerDispenser, SpawnerContainer
  - **Default:** Varies by spawner

- **Times Between Spawns**:
  Interval between spawns.
  - **Applies to:** SpawnerTree, SpawnerDispenser, SpawnerContainer
  - **Default:** 4.0 for trees, 1.5 otherwise

- **Ripen Times**:
  Duration for goals to ripen in a tree.
  - **Applies to:** SpawnerTree
  - **Default:** 6.0

- **Door Delays**:
  Time for a spawner's door to open.
  - **Applies to:** SpawnerDispenser, SpawnerContainer
  - **Default:** 10.0

- **Times Between Door Opens**:
  Interval for a spawner's door to open.
  - **Applies to:** SpawnerDispenser, SpawnerContainer
  - **Default:** -1 (stays open once opened)

### SignBoard Parameters
- **Symbol Names**:
  Names of symbols to be drawn.
  - **Applies to:** SignBoard
  - **Default:** "default"
  - **Options:** "left-arrow", "right-arrow", etc.


## Blackouts

Blackouts are parameters you can pass to each arena, which define between which frames of an episode the lights are 
on or off. If omitted, this parameter automatically sets to have lights on for the entire episode. You can otherwise 
pass two types of arguments for this parameter:

- passing a list of frames `[5,10,15,20,25]` will start with the lights on, switch them off from frames 5 to 9 included, 
then back on from 15 to 19 included etc...
- passing a single negative argument `[-20]` will automatically switch lights on and off every 20 frames.

**Note**: for infinite episodes (where `t=0`), the first point above would leave the light off after frame `25` while the second point would keep switching the lights every `20` frames indefinitely.


## Blackouts

Blackouts define when the lights are on or off during an episode in each arena.

- **Default Behavior**: Lights are on for the entire episode if no blackout parameter is provided.
- **List of Frames**: Provide a list like `[5,10,15,20,25]` to toggle lights. Lights will be off between frames 5-9, 15-19, etc., and on at other times.
- **Regular Intervals**: Use a negative number like `[-20]` to toggle lights every 20 frames.
- **Infinite Episodes**: For episodes with `t=0`, lights will follow the pattern indefinitely.

**Note**: With a list of frames, lights will stay off after the last frame in the list for infinite episodes.

## Rules and Notes for Arena Configuration

When configuring an arena, follow these rules and be aware of certain behaviors:

### Spawning Objects
- **Non-Overlapping**: Objects can only spawn if they don't overlap with others. Overlapping attempts discard the latter object.
- **Spawn Order**: Objects are spawned in the order listed. Randomized components try to spawn up to 20 times; if unsuccessful, the object is discarded.
- **Spawn Likelihood**: Early list objects are more likely to spawn than later ones.
- **Agent Spawning**:
  - The Agent spawns randomly if not specified.
  - Specified Agent positions are processed last, which might conflict with randomly spawned objects.
  - If an object occupies the Agent's spot, the arena resets and spawning restarts.
  - Some objects can spawn on top of each other, with a `0.1` height buffer added automatically.

### Configuration File Values
- **Object Names**: Must match names from [definitions](definitionsOfObjects.md). Unmatched names are ignored.
- **Randomization**: Use `-1` in `positions`, `sizes`, and `rotations` for random values.
- **Ground Level Spawning**: Setting `positions.y = -1` spawns objects at ground level.
- **Goal Scaling**: Goals (except red zone) scale equally on all axes. For sphere goals, only the `x` component of `Vector3` scales all axes.

---