# Arena Environment Guide

#### Table of Contents

* [Introduction](#introduction)
* [The Arena](#the-arena)
* [The Agent](#the-agent)
  + [Agent HUD (Heads-Up Display)](#agent-hud-heads-up-display)
  + [Arena/Agent Limitations](#arenaagent-limitations)
  + [Agent Properties](#agent-properties)
* [GameObjects](#gameobjects)
  + [Unique/Special Object Parameters](#uniquespecial-object-parameters)
  + [Agent-Specific Parameters](#agent-specific-parameters)
  + [Goal-Related Parameters](#goal-related-parameters)
  + [Spawner Parameters](#spawner-parameters)
  + [SignBoard Parameters](#signboard-parameters)
* [Blackouts](#blackouts)
* [Rules and Notes for Arena Configurations](#rules-and-notes-for-arena-configurations)
  + [Spawning GameObjects](#spawning-gameobjects)
  + [Configuration File Values](#configuration-file-values)


## Introduction

This guide will help you understand the structure of the physical Arena Environment as developed in Unity. We will explain the various functions of the arena environment, and their purposes and uses. We will also outline the various parameters that can be used to configure the arena environment, and how to use them. 

Please see the [YAML Config Syntax](/docs/configGuide/YAML-Config-Syntax.md) guide for a detailed explanation of the syntax used in the configuration files for additional information. Be aware that this guide is not a comprehensive guide to Unity, and assumes that you have a basic understanding of the Unity Engine. If you are unfamiliar with Unity, please refer to the [Background - Unity](/docs/Background-Unity.md) guide for a brief overview of the Unity Engine as well as relevant useful links.

## The Arena

<table>
  <tr>
    <td><img src="../docs/figs/prefabs/arena/arena-2DView.png" width="500"/>
    <p>2D view of the Arena</p></td>
    <td><img src="../docs/figs/prefabs/arena/arena-FP.png" width="500"/><p>First-person view of agent</p></td>
    <td><img src="../docs/figs/prefabs/arena/arena-New.png" width="500"/><p>Full view of arena</p></td>
  </tr>
  <tr>
    <td><img src="../docs/figs/prefabs/arena/arena-Ground.png" width="500"/><p>Close-up of arena ground</p></td>
    <td><img src="../docs/figs/prefabs/arena/arena-TP.png" width="500"/><p>Third Persion view of one of the agent skins</p></td>
    <td><img src="../docs/figs/prefabs/arena/arena-Walls.png" width="500"/><p>Side view of walls</p></td>
  </tr>
</table>

Each **episode** (a single run) contains an _arena_ environment. Currently, an arena can only support a single agent (with spherical animal skins - _hedgehog_, _pig_, or _panda_). It is currently a square of fixed size `40x40` , meaning the size of the arena is immutable, with the origin of the arena is set to `(0,0)` . You can provide coordinates for objects in the range `[0,40]x[0,40]` as floats.

The default arena is made up of a set of gameobjects, which itself is contained in a _Unity Scene_, which are as follows:

* **Walls**: The walls of the arena, which are 10 units high and 40 units long. The walls are made up of 4 gameobjects, one for each wall, which are named `Wall1`,  `Wall2`,  `Wall3`, and `Wall4`, each with a set of childobjects called `fences`, which contain the textures for the walls. The walls are all children of the `Walls` gameobject, which is itself a child of the `Arena` gameobject.
#####
* **Ground**: The ground of the arena, which is 40 units long and 40 units wide. The ground is a child of the `Arena` gameobject.
#####
* **Lights**: The lights of the arena, which are 4 spotlights, one for each corner of the arena. The lights are all children of the `Lights` gameobject, which is a child of the `Arena` gameobject.
#####
* **SpawnArea**: The spawn gameobject responsible for spawning objects defined in the configuration file, which is a child of the `Arena` gameobject. This gameobject essentially controls the size of the spawn area, currently set to within the bounds of the walls of the arena.
#####
* **Agent**: The agent, which is a child of the `Arena` gameobject, is the main character in the arena, and is used for playing and training; must be spawned in every arena.

<p align="center">
  <img height="300" src="../docs/figs/prefabs/DefaultArena.png">
</p>

In the above picture with the agent on the ground in the center of the environment its coordinates are `(20, 0, 20)` . Below is a sample configuration file for the default arena as shown above:

```YAML
!ArenaConfig
randomizeArenas: false
showNotification: false 
canResetEpisode: true 
canChangePerspective: true 
arenas:
  n: !Arena # note that the n is a placeholder integer between 0 and n, but the first arena must start with 0
    #pass_mark: 0 # This syntax is only supported for AAI builds less than v4.0.0. If you are using newer versions, please use the 'passMark' syntax.
    passMark: 0 # The pass mark for the arena. The agent must achieve this score to pass the arena.
    #t: 250 # This syntax is only supported for AAI builds less than v4.0.0. If you are using newer versions, please use the 'timeLimit' syntax.
    timeLimit: 250 # The time limit for the arena in seconds. In other words, the time limit for the agent to complete the task (the arena resets after this time).
    items:
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 20, y: 0, z: 20}
      rotations: [0]
```

* `(n): !Arena` an `int`, denotes the unique arena index, which is used to identify the arena in the configuration file. The first arena must start with `0`, upto `n`, where `n` is the number of arenas defined in a single configuration file. 
#####
* `timeLimit` an `int`, defines the length of an episode which can change from one episode to the other. A value of `0` means that the episode will not terminate until a reward has been collected (setting `t=0` and having no reward will lead to an infinite episode). This value is converted into a decay rate for the health of the agent. A `t` of 100 means that the agent's health will decay to 0, and the episode will end, after 100 time steps. **Note: This parameter name is supported in AAI builds v4.0.0 and below. It is replaced by `timeLimit` in AAI builds v4.1.0 and above.**
#####
* `passMark` an `int`, defines the reward threshold that should constitute a ‘pass’ in the enviroment. Leaving this parameter undefined leads to the default value of 0, whereby any reward value obtained by the Agent results in a pass. This parameter also determines the notifications that players receive at the end of an episode. If used, this parameter should be defined with consideration to the reward size that can feasibly be obtained by the agent in each configuration file. **Note: This parameter name is supported in AAI builds v4.0.0 and below. It is replaced by `passMark` in AAI builds v4.1.0 and above.**
#####
* `canChangePerspective` a `bool`, defines whether the agent can change its camera perspective during an episode (first-person, third-person or eagle-view). If set to `false`, the agent will be unable to change its camera perspective during an episode by pressing the C button on their keyboards, which will cycle through the cameras attached to the Agent in-gasme. If set to `true`, the agent will be able to change its perspective during an episode. This parameter is set to `true` by default.
#####
* `randomizeArenas` a `bool`, defines whether the arena will be randomized between episodes. If set to `true`, the arena will be randomized between the defined Arenas in the configuration file. If set to `false`, the order to which the arenas are spawned are sequential and top-to-bottom as specified in the configuration file. This parameter is set to `false` by default.
#####
* `showNotification` a `bool`, defines whether the player will receive a notification at the end of an episode. If set to `true`, the player will be shown a notification at the end of an episode for approximately 2.5 seconds, then move on to the next episode (arena). If set to `false`, the agent will not receive a notification at the end of an episode and episode-to-episode termination is back-to-back. This parameter is set to `false` by default.
#####
* `blackouts` a `list`, defines the frames at which the lights are on or off during an episode. If omitted, the lights will be on for the entire episode. For more information on blackouts, [see here](#blackouts).

**N. B:** These parameters are optional (except `t` and `pass_mark` ) and can be omitted from the configuration file. If omitted, the default values will be used, which are explained in detail in our [YAML Config Syntax](/docs/configGuide/YAML-Config-Syntax.md) guide.

## The Agent

The agent is the main character in the arena, for playing and training. It is a spherical animal with a set of controls that can be used to move it around the arena. The agent can be configured to have a set of different skins, which can be specified in the configuration file, under it's parameters. The agent has a set of controls that can be used to move it around the arena. 

The controls are as follows:

* `W` - move forward
* `A` - move left
* `S` - move backward
* `D` - move right
* `C` - change camera perspective (first-person, third-person, eagle-view, only if `canChangePerspective` is `true`)
* `R` - reset the arena (cycles to the next episode if `canResetEpisode` is `true`)
* `Q` - quit (exits the application upon press)

The agent has a set of skins that can be used to change its appearance in the arena. The skins are as follows:

<table>
    <td><img src="../docs/figs/prefabs/agent-skins/agent-hedgehog.png" width="500"/><p>Hedgehog</p></td>
    <td><img src="../docs/figs/prefabs/agent-Skins/agent-panda.png" width="500"/><p>Panda</p></td>
    <td><img src="../docs/figs/prefabs/agent-Skins/agent-pig.png" width="500"/><p>Pig</p></td>
</table>

### Agent HUD (Heads-Up Display)

The agent has a HUD that displays the following information per episode by default:

* **Health**: The health of the agent, which is a value between `0` and `1`. The agent's health decays over time, and is reset to `1` when the agent collects a reward. The agent's health is displayed as a green-yellow-red bar at the bottom of the HUD.
#####
* **Reward**: The reward collected by the agent, which is a value between `-1` and `1`. The agent's reward is displayed as a text at the top of the HUD, which is updated in real-time as the agent collects rewards. It contains the previous episode's reward (not valid if the current arena is the first), as well as the current episode's reward.
#####
* **Yaml File Details**: The YAML file details of the current yaml file used, which is displayed at the top-right of the HUD. This is an integer that contains the arena number out of total arenas, and the total number of objects spawned as an integer.
#####
* **Notification**: The notification displayed to the agent at the end of an episode. The notification is currently a combination of color gradients and a short animated GIF. This is an optional HUD and only appears if `showNotification` parameter is set to `true` in the configuration file. _Note that this feature has no effect on training, and is only used for play mode._

| ![](../docs/figs/Agent-HUD/agent-health.png)     | ![](../docs/figs/Agent-HUD/agent-REWARD.png)      |
| ------------------------------------------------ | ------------------------------------------------- |
| ![](../docs/figs/Agent-HUD/notification-bad.png) | ![](../docs/figs/Agent-HUD/notification-good.png) |
| ![](../docs/figs/Agent-HUD/yaml-file-data.png)   |


### Arena/Agent Limitations

The arena/agent has a few limitations to be considered, which are as follows:

1. Only a single agent _per_ arena/episode is supported, both for play and training.
2. The agent can only move on the ground, and cannot move on the walls or any other object (except when placed on top of objects that have a flat surface).
3. The agent cannot move through objects (except for the hot/death zones).
4. The agent cannot jump or fly.
5. The agent cannot pick up objects (however, this is a feature to be added in the future).
6. The arena is reset _only_ when the health of the agent reaches `0`, or when the `R` key is pressed (in play mode). This is a limitation as the arena is limited in episode-to-episode flexibility.
7. The logic of spawning objects in the arena is fixed and currently prioritises the agent over other objects. Furthermore, the current spawn logic dictates that objects spawn in the order they are defined in the configuration file. This too is a limitation as it does not allow for more complex/flexible spawning logic.

### Agent Properties

The agent has a Physics component attached to it, which allows it to interact with other objects in the arena. Please read our [Background - Unity](/docs/Background-Unity.md) guide for more information. 

_Essentially, you can expect that the Physics of Unity game engine are modelled to mimic our three-dimensional reality as much as possible_. The agent has the following properties:

* **Scale**: The scale of the agent, which is set to `1x1x1` by default.
* **Mass**: The mass of the agent, which is set to `100` by default.
* **Drag**: The drag of the agent, which is set to `1.2` by default.
* **Angular Drag**: The angular drag of the agent, which is set to `0.05` by default.
* **Gravity**: Enabled for the agent (and for all other objects for that matter), which means that the Agent will fall to the ground when spawned if it's `y` coordinate `> 0`.
* **Speed**: The speed of the agent, which is set to `30` by code. This is the speed at which the agent moves when the `W`,  `A`,  `S`, and `D` keys are pressed. Note that the speed of the agent is affected by the `drag` and `angular drag` properties, which means that the agent will slow down over time if the keys are not pressed.
* **Rotation Speed**: The rotation speed of the agent, which is set to `100` by code. This is the speed at which the agent rotates when the `A` and `D` keys are pressed. Rotation speed is unaffected by the `drag` and `angular drag` properties.
* **Rotation Angle**: The angle of rotation of the agent, which is `0.25` by code. This property is used to dictate the angle of rotating the agent when the `A` and `D` keys are pressed. Rotation angle is unaffected by the `drag` and `angular drag` properties.


## Game Objects

All objects can be configured in the same manner, using a set of parameters for each `item` Unity Game Object:

* `name`: the name of the object you want to spawn, which must match the object name specified in [Arena Object Definitions](/docs/Arena-Object-Definitions.md). You can spawn the same object as many times as required, but they must be in different positions from one another.
#####
* `positions`: a list of `Vector3` positions within the arena where you want to spawn items, if the list is empty the position will be sampled randomly in the arena. Any position vector set to -1 will spawn randomly. Also note that Animal-AI enforces a constraint where objects cannot spawn within 0.1 units of each other, so if you try to spawn objects too close together there will be object collision clashes and the objects will not spawn.
#####
* `sizes`: a list of `Vector3` sizes, if the list is empty the size will be sampled randomly (within preset bounds for that particular object). You can set any size to -1 to spawn randomly along that vector only.
#####
* `rotations`: a list of `float` in the range `[0,360]`, if the list is empty the rotation is sampled randomly. Default is 0 degrees.
#####
* `colors`: a list of `RGB` values (integers in the range `[0,255]`), if the list is empty the color is sampled randomly. Note that not all objects can have their colour changed and for those (e.g. transparent objects) this value will be ignored.

**N. B:** Any of these parameters can be omitted in the configuration files per object, in which case the omitted fields are automatically randomized. However, we advise that you specify these parameters as this will allow you to have a more controlled environment in your arena(s). Any Vector3 that contains a -1 for any of its dimensions will spawn that dimension randomly `(e.g. x: -1, y: 10, z: 2 --> will spawn the object randomly along the x axis)` . Finally, some objects have specific parameters applicable only to them, which are described in the [Unique/Special Objects](#uniquespecial-object-parameters).

**All value ranges for the above fields can be found in [Arena Object Definitions](/docs/Arena-Object-Definitions.md) guide**. If you go above or below the range for size it will automatically be set to the max or min respectively. If you try to spawn objects outside the arena (i.e. with a configuration like this: `x = 41, z = 41` ) or overlapping with another object with very close spawn positions, then that object will not be spawned. Objects are placed in the order defined such that the second overlapping object is the one that does not spawn.

## Unique/Special Object Parameters

Some objects have unique/special parameters that only apply to them or a select few objects - they can be written in the configuration in exactly the same way as the 'standard' parameters, but will only be applied if assigned to a valid object:

### Agent-Specific Parameters

* **Skins**:
  List of animal skins for the agent model.
  + **Applies to:** Agent
  + **Default:** "random" (any animal from the list)
  + **Options:** "panda", "pig", "hedgehog", "random", etc.

* **Frozen Agent Delays**:
  Time (in frames) the agent is frozen at the start of an episode.
  + **Applies to:** Agent
  + **Default:** 0 (no delay), n (delay of n frames)

### Goal-Related Parameters

* **Delays**:
  Time delay before special behavior initiation.
  + **Applies to:** DecayGoal, AntiDecayGoal, GrowGoal, ShrinkGoal, SpawnerTree, SpawnerDispenser, SpawnerContainer
  + **Default:** 0

* **Initial Values**:
  Starting reward/size values.
  + **Applies to:** DecayGoal, AntiDecayGoal, GrowGoal, ShrinkGoal, SpawnerTree
  + **Default:** Varies by goal type

* **Final Values**:
  Ending reward/size values.
  + **Applies to:** DecayGoal, AntiDecayGoal, GrowGoal, ShrinkGoal, SpawnerTree
  + **Default:** Varies by goal type

* **Change Rates**:
  Rate at which reward/size changes.
  + **Applies to:** DecayGoal, AntiDecayGoal, GrowGoal, ShrinkGoal
  + **Default:** 0.005 (negative for decaying/shrinking)

### Spawner Parameters

* **Spawn Counts**:
  Number of goals spawned.
  + **Applies to:** SpawnerTree, SpawnerDispenser, SpawnerContainer
  + **Default:** -1 (infinite)

* **Spawn Colors**:
  Color of spawned objects.
  + **Applies to:** SpawnerTree, SpawnerDispenser, SpawnerContainer
  + **Default:** Varies by spawner

* **Times Between Spawns**:
  Interval between spawns.
  + **Applies to:** SpawnerTree, SpawnerDispenser, SpawnerContainer
  + **Default:** 4.0 for trees, 1.5 otherwise

* **Ripen Times**:
  Duration for goals to ripen in a tree.
  + **Applies to:** SpawnerTree
  + **Default:** 6.0

* **Door Delays**:
  Time for a spawner's door to open.
  + **Applies to:** SpawnerDispenser, SpawnerContainer
  + **Default:** 10.0

* **Times Between Door Opens**:
  Interval for a spawner's door to open.
  + **Applies to:** SpawnerDispenser, SpawnerContainer
  + **Default:** -1 (stays open once opened)

### SignBoard Parameters

* **Symbol Names**:
  Names of symbols to be drawn.
  + **Applies to:** SignBoard
  + **Default:** "default"
  + **Options:** "left-arrow", "right-arrow", etc.

## Blackouts

_Blackouts_ define when the lights are on or off during an episode in each arena, resulting in a black screen/view in any camera angle. This is an optional parameter in the configuration file, and can be omitted if you don't want to use it. If omitted, the lights will be on for the entire episode.

* **Default Behavior**: Lights are on for the entire episode if no blackout parameter is provided.
* **List of Frames**: Provide a list like `[5,10,15,20,25]` to toggle lights. Lights will be off between frames 5-9, 15-19, etc., and on at other times.
* **Regular Intervals**: Use a negative number like `[-20]` to toggle lights every 20 frames.
* **Infinite Episodes**: For episodes with `t=0`, lights will follow the pattern indefinitely.

**Note**: With a list of frames, the lights will stay off after the last frame in the list for infinite episodes. 

See the [YAML Config Syntax](/docs/configGuide/YAML-Config-Syntax.md) guide for a detailed tutorial on how to use blackouts.

## Rules and Notes for Arena Configurations

When configuring an arena, follow these rules and be aware of certain behaviors:

### Spawning GameObjects

* **Non-Overlapping**: Objects can only spawn if they don't overlap with others. Overlapping attempts discard the latter object (i.e. the object that is spawned later in the configuration file). This is to avoid object collision issues during runtime.
#####
* **Spawn Order**: Objects are spawned in the order listed. Randomized objects (i.e. the object is set to spawn randomly) try to spawn up to 20 times concurrently in any given arena/episode; if unsuccessful, the object is discarded and the arena continues to spawn the next object in the list (if any).
#####
* **Spawn Likelihood**: Early list objects are more likely to spawn than later ones. This is because the configuration file is scanned from top to bottom, and objects are spawned in the order they are found.
#####
* **Agent Spawning**:
  + The Agent spawns randomly within the arena bounds if it's spawn position is not specified.
  + Specified Agent positions are processed _first_, which might conflict with randomly spawned objects that are spawned _after_ the Agent, as the Agent's position is not known until runtime.
  + If you have defined the Agent's position and another object tries to spawn at the same position as the Agent then the environment will always spawn the Agent in that position always, as _the Agent has priority above every other object_. This is to avoid a potential conflict during runtime.
  + Some objects can spawn on top of each other (a `0.1` height buffer added to accomodate this). 

### Configuration File Values

* **n: ! Arena**: The `n` in `n: !Arena` is a placeholder integer between `0` and `n`, where `n` is the number of arenas defined in a single configuration file. The first arena must start with `0`, upto `n` arenas. Any negative arena numbers are automatically converted to positive integers accordingly, resulting in flexible and robust arena numbering and management.
#####
* **Object Names**: Must match names from [Arena Object Definitions](/docs/Arena-Object-Definitions.md). Unmatched names are ignored and may result in unexpected behavior or fatal errors.
#####
* **Randomization**: Use `-1` or leave blank in `positions`,  `sizes`, and `rotations` for random values for any object that supports randomization (see [Arena Object Definitions](/docs/Arena-Object-Definitions.md)).
#####
* **Ground Level Spawning**: Setting `positions.y = 0` spawns objects at ground level (with a `0.1` height buffer to prevent gameobject clipping).
#####
* **Goal Scaling**: Goals (except red zone) scale equally on all axes. For sphere goals, only the `x` component of `Vector3` scales all axes.
#####
* **Arena Height Bounds**: Currently, objects can spawn at any height within the arena, which translates to the `y` component of `Vector3` in the configuration file. However, a recommended height range is between `0` and `50` units, as anything above `50` units will be out of the camera's view until the object falls from the sky and lands on the ground at the specified `x` and `z` coordinates, which may take a while depending on the object's mass and drag properties. This is not an issue for objects that spawn on the ground, as they will spawn at the specified `x` and `z` coordinates, and at ground level (i.e. `y = 0`).
#####
* **Arena Size Bounds**: The arena is currently a square of fixed size `40x40`, meaning the size of the arena is immutable, with the origin of the arena is set to `(0,0)`. You can provide coordinates for objects in the range `[0,40]x[0,40]` as floats. Any coordinates outside this range will be discarded and the object will not spawn. We plan to make the arena size configurable in the future.

---
