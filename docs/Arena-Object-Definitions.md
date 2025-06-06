# Animal-AI Environment Objects

#### Table of Contents

1. [Introduction](#introduction)
2. [Unity Objects - What are they?](#unity-objects---what-are-they)
3. [The Arena](#the-arena)
4. [The Agent](#the-agent)
5. [Immovable Objects](#immovable-objects)
6. [Movable Objects](#movable-objects)
7. [Valenced Objects](#valenced-objects)
8. [Spawners](#spawners)
9. [Sign Boards](#sign-boards)
10. [Ready-Made Configuration File](#ready-made-configuration-file)

## Introduction

The Animal-AI environment includes various objects categorized into _immovable_, _movable_, _rewards_, and _other/unique_ types. These objects can be configured to create diverse tasks. Each object's name, default characteristics, and configurable ranges are detailed below. All objects can rotate 360 degrees. Unity uses a left-handed coordinate system with `y` as the vertical axis, and `x` and `z` axes representing horizontal and depth dimensions, respectively.

## Unity Objects - What are they?

Unity game objects, commonly referred to as *GameObjects*, are the fundamental components in the Unity Engine, serving as containers for all other components or functionalities within a Unity scene. These objects can represent characters, props, scenery, cameras, lights, and more. Each GameObject can be equipped with various components such as scripts, renderers, colliders, or custom components, defining their behavior and interaction within the game world. *Prefabs* in Unity are essentially templates created from GameObjects; they allow developers to create, configure, and store a GameObject complete with its components and properties. Once a Prefab is created, it can be reused multiple times across the scene or even across different projects, ensuring consistency and efficiency in game development by allowing changes to be made to multiple instances simultaneously.

Most objects in AAI share a handful of fundamental parameters governing their size, position, and other properties. Values for these parameters can be defined in YAML ([see here](/docs/Background-YAML.md)). Common parameters are:
* `name`: the name of the object you want to spawn.
* `positions`: a list of `Vector3` positions within the arena where you want to spawn items. If the list is empty, the position will be sampled randomly in the arena. Any position dimension set to -1 will spawn randomly.
* `sizes`: a list of `Vector3` sizes. If the list is empty, the size will be sampled randomly (within preset bounds for that particular object). You can set any size to -1 to spawn randomly along that dimension only.
* `rotations`: a list of `float` in the range `[0, 360]`. If the list is empty, the rotation is sampled randomly.
* `colors`: a list of `RGB` values (integers in the range `[0, 255]`). If the list is empty, the color is sampled randomly. Note that not all objects can have their color changed, and for those (e.g., transparent objects), this value will be ignored.

All except `name` and `positions` parameters can be omitted in the configuration files, in which case the omitted fields are automatically randomized. Any Vector3 that contains a `-1` value for any of its dimensions (x, y, z) will spawn that dimension randomly. This can be used to spawn, for example, multiple walls of a set width and height but random lengths.

## The Arena

<figure style="text-align: center;">
  <img height="300" src="/docs/figs/prefabs/NewDefaultArenaCapture.png" alt="New Default Arena">
  <figcaption>Animal-AI Default Arena (Animal-AI v4.1.0)</figcaption>
</figure>


A single _Arena_, as shown above, comes with a single _Agent_ (spherical animal), a ground, and four walls/boundaries. It is a square of size 40x40, with the origin (the bottom-left corner) at `(0,0)`. You can provide coordinates for objects in xy,z axis in the range `[0,39.9],[0,~],[0,39.9]` as floats (note y axis is the vertical axis and can be unbounded).

Note that in Unity, the **y** axis is the vertical axis. In the above picture, with the agent on the ground in the center of the environment, the Agent's coordinates are `(x = 20, y = 0, z = 20)`.

## The Agent

The agent can be placed anywhere in the arena with any rotation. It has a fixed size and a fixed set of skins.

* **Name**: `Agent`
* **Size**: `(1,1,1)` (not changeable)
* **Skins**: `"hedgehog"`, `"panda"`, `"pig"` (can be randomized)

Notes: The agent can be frozen for a specified number of frames at the start of an episode. There is no reward decrement during the frozen period. This can be set with an integer value passed to the `frozenAgentDelays` parameter (defaults to `0`).

<table>
  <tr>
    <td><img src="/docs/figs/prefabs/agent-skins/agent-hedgehog.png" width="500"/><p>The Agent as a hedgehog</p></td>
    <td><img src="/docs/figs/prefabs/agent-skins/agent-panda.png" width="500"/><p>The Agent as a panda</p></td>
    <td><img src="/docs/figs/prefabs/agent-skins/agent-pig.png" width="500"/><p>The Agent as a pig</p></td>
  </tr>
</table>


## Immovable Objects

_Immovable_ objects are fixed in place and cannot be moved. The outer walls of the arena are also immovable and are permanently fixed in place to prevent the player/agent from escaping the arena. Immovable objecs are available from Animal-AI v2.0.0.

### Wall

<img align="right" height="100" src="/docs/figs/prefabs/Immovable/Wall.png" />

* **Name**: `Wall`
* **Size Range**: `(0.1,0.1,0.1)-(40,10,40)`
* **Color**: RGB range `(0,0,0)-(255,255,255)`

### Transparent Wall

<img align="right" height="100" src="/docs/figs/prefabs/Immovable/WallTransparent.png" />

* **Name**: `WallTransparent`
* **Size Range**: `(0.1,0.1,0.1)-(40,10,40)`
* **Color**: Not changeable / (transparent)

### Ramp

<img align="right" height="100" src="/docs/figs/prefabs/Immovable/Ramp.png" />

* **Name**: `Ramp`
* **Size Range**: `(0.5,0.1,0.5)-(40,10,40)`
* **Color**: RGB range `(0,0,0)-(255,255,255)`

### Tunnel

<img align="right" height="100" src="/docs/figs/prefabs/Immovable/CylinderTunnel.png" />

* **Name**: `CylinderTunnel`
* **Size Range**: `(2.5,2.5,2.5)-(10,10,10)`
* **Color**: RGB range `(0,0,0)-(255,255,255)`

### Transparent Tunnel

<img align="right" height="100" src="/docs/figs/prefabs/Immovable/CylinderTunnelTransparent.png" />

* **Name**: `CylinderTunnelTransparent`
* **Size Range**: `(2.5,2.5,2.5)-(10,10,10)`
* **Color**: Not changeable / (transparent)

### Datazone

Datazones can be used to record when an agent enters and exits a certain region. This is recorded in the generated CSV file; see the [How are datazones logged?](CSVLoggerGuide.md#how-are-datazones-logged) for more details, and the [Datazone End-to-End test](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-e2e/blob/main/testConfigs/testDatazone.yml) for an example usage.

* **Name**: `CylinderTunnelTransparent`
* **Size Range**: `(0.1,0.1,0.1)-(40,10,40)`
* **Color**: Not changeable / (transparent)
* **triggerZoneID**: User configurable string used to identify the datazone. This string will be logged in the csv when it enters and leaves the datazone
* **zoneVisibility**: Toggles the visibility of the datazone

## Movable Objects

_Movable_ objects can be easily moved by the agent or other objects. These objects can be pushed by the player/agent as the physics engine is enabled for these objects. Note that some movable objects have aliases (alternative names, now deprecated) for backwards compatibility with previous versions of AAI.

### Light Block

<img align="right" height="100" src="/docs/figs/prefabs/Movable/NewLightBlockObj.png" style="margin-left: 5px;" />

<img align="right" margin=1 height="100" src="/docs/figs/prefabs/Movable/LightBlock.png" />

* **Name**: `LightBlock`
* **Size Range**: `(0.5,0.5,0.5)-(10,10,10)`
* **Color**: Changeable / (stone textured) from AAI v4.2.0 onwards
* **Alias**: `CardBox1`

_Updated textures (right) available from Animal-AI v4.2.0 onwards._

### Heavy Block

<img align="right" height="100" src="/docs/figs/prefabs/Movable/NewHeavyBlockObj.png" style="margin-left: 5px;"/>

<img align="right" height="100" src="/docs/figs/prefabs/Movable/LightBlock.png" />

* **Name**: `HeavyBlock`
* **Size Range**: `(0.5,0.5,0.5)-(10,10,10)`
* **Color**: Changeable / (stone textured) from AAI v4.2.0 onwards
* **Alias**: `CardBox2`

_Updated textures (right) available from Animal-AI v4.2.0 onwards._

### U-shaped Block

<img align="right" height="100" src="/docs/figs/prefabs/Movable/UBlock.png" />

* **Name**: `UBlock`
* **Size Range**: `(1,0.3,3)-(5,2,20)`
* **Color**: Changeable / (cardboard textured) from AAI v4.2.0 onwards
* **Alias**: `UObject`

### L-shaped Block

<img align="right" height="100" src="/docs/figs/prefabs/Movable/LBlock.png" />

* **Name**: `LBlock`
* **Size Range**: `(1,0.3,3)-(5,2,20)`
* **Color**: Changeable / (cardboard textured) from AAI v4.2.0 onwards
* **Alias**: `LObject`

### J-shaped Block

<img align="right" height="100" src="/docs/figs/prefabs/Movable/JBlock.png" />

* **Name**: `JBlock`
* **Size Range**: `(1,0.3,3)-(5,2,20)`
* **Color**: Changeable / (cardboard textured) from AAI v4.2.0 onwards
* **Alias**: `JObject`

### Hollow Box

<img align="right" height="100" src="/docs/figs/prefabs/Movable/HollowBox.png" />

* **Name**: `HollowBox`
* **Size Range**: `(0.5,0.5,0.5)-(5,5,5)`
* **Color**: Changeable / (cardboard textured) from AAI v4.2.0 onwards

_Available from Animal-AI v4.2.0 onwards._

## Valenced Objects

Valenced objects increase or decrease the agent's reward when the agent touches them. Some are stationary and some have an initial velocity at the start of an episode. Note that some of these objects have aliases (alternative names) for backwards compatibility with previous versions of AAI.

### Stationary Episode-Ending Positive Goal

<img align="right" height="100" src="/docs/figs/prefabs/ValencedObjects/GoodGoal.png" />

* **Name**: `GoodGoal`
* **Size Range**: `1`
* **Color**: Changeable / (green) from AAI v4.2.0 onwards
* **Valence**: Positive

### Moving Episode-Ending Positive Goal

<img align="right" height="100" src="/docs/figs/prefabs/ValencedObjects/GoodGoal.png" />

* **Name**: `GoodGoalBounce`
* **Size Range**: `1`
* **Color**: Changeable / (green) from AAI v4.2.0 onwards
* **Valence**: Positive

### Non-Episode-Ending Positive Multi Goal

<img align="right" height="100" src="/docs/figs/prefabs/ValencedObjects/GoodGoal.png" />

* **Name**: `GoodGoalMulti`
* **Size Range**: `1`
* **Color**: Not changeable / (green) from AAI v4.2.0 onwards
* **Valence**: Positive

### Stationary Episode-Ending Negative Goal

<img align="right" height="100" src="/docs/figs/prefabs/ValencedObjects/BadGoal.png" />

* **Name**: `BadGoal`
* **Size Range**: `-1`
* **Color**: Changeable / (red) from AAI v4.2.0 onwards
* **Valence**: Negative

### Moving Episode-Ending Negative Goal

<img align="right" height="100" src="/docs/figs/prefabs/ValencedObjects/BadGoal.png" />

* **Name**: `BadGoalBounce`
* **Size Range**: `-1`
* **Color**: Changeable / (red) from AAI v4.2.0 onwards
* **Valence**: Negative

### Non-Episode-Ending Negative Multi Goal

<img align="right" height="100" src="/docs/figs/prefabs/ValencedObjects/BadGoalMulti.png" />

* **Name**: `BadGoalMulti.experimental`
* **Size Range**: `-0.003`
* **Color**: Changeable / (orange) from AAI v4.2.0 onwards
* **Valence**: Negative

_Available from Animal-AI v4.2.0 onwards._

### Stationary Non-Episode-Ending Positive Goal

<img align="right" height="100" src="/docs/figs/prefabs/ValencedObjects/GoodGoalMulti.png" />

* **Name**: `GoodGoalMulti`
* **Size Range**: `0.5-1`
* **Color**: Changeable / (yellow) from AAI v4.2.0 onwards
* **Valence**: Positive

### Moving Non-Episode-Ending Positive Goal

<img align="right" height="100" src="/docs/figs/prefabs/ValencedObjects/GoodGoalMulti.png" />

* **Name**: `GoodGoalMultiBounce`
* **Size Range**: `0.5-5`
* **Color**: Changeable / (yellow) from AAI v4.2.0 onwards
* **Valence**: Positive

### Non-Episode-Ending Ripen Goal

<img align="right" height="100" src="/docs/figs/prefabs/ValencedObjects/RipenGoal.png" />

* **Name**: `RipenGoal`
* **Valence Range**: `0-5`
* **Size**: Automatically sets to final reward value (dynamic), proportionally to the `ripenRate`
* **Color**: Not changeable / (yellow and blue)
* **Ripen Onset Delay Range (frames)** (`delays`): `0-Inf` (default `150`)
* **Ripen Rate (frames)** (`changeRates`): `0.001-Inf` (default `0.005`)
* **Alias**: `AntiDecayGoal`

Note: Colour changes (from grey to yellow) and a radial-timer fills over time during the ripening process. Initial valence can be set with a float passed to the `initialValues` parameter, and final valence can be set with a float passed to the `finalValues` parameter.

### Non-Episode-Ending Decay Goal

<img align="right" height="100" src="/docs/figs/prefabs/ValencedObjects/DecayGoal.png" />

* **Name**: `DecayGoal`
* **Valence Range**: `0-5`
* **Size**: automatically sets to final reward value (dynamic), proportionally to the `decayRate`
* **Color**: Not changeable / (yellow and orange)
* **Decay Onset Delay Range (frames)** (`delays`): `0-Inf` (default `150`)
* **Decay Rate (frames)** (`changeRates`): `-0.001-Inf` (default `-0.005`, automatically converts to negative values if positive provided)

Note: Colour changes (from yellow to grey) and a radial-timer depletes over time during decay process. Initial valence can be set with a float passed to the `initialValues` parameter, and valence can be set with a float passed to the `finalValues` parameter. 

### Episode-Ending Grow Goal

<img align="right" height="100" src="/docs/figs/prefabs/ValencedObjects/GoodGoal.png" />

* **Name**: `GrowGoal`
* **Size Range**: `0.5-5`
* **Valence Change Rate** (`changeRates`): `0.001-Inf` (default `0.005`)
* **Valence**: Positive, proportional to size
* **Color**: Changeable / (green) from AAI v4.2.0 onwards
* **Growth Onset Delay Range (frames)** (`delays`): `0-Inf` (default `0`)

### Episode-Ending Shrink Goal

<img align="right" height="100" src="/docs/figs/prefabs/ValencedObjects/GoodGoal.png" />

* **Name**: `ShrinkGoal`
* **Size Range**: `5-0.5`
* **Valence Change Rate** (`changeRates`): `0.001-Inf` (default `0.005`)
* **Valence**: Negative, proportional to size
* **Color**: Changeable / (green) from AAI v4.2.0 onwards
* **Growth Onset Delay Range (frames)** (`delays`): `0-Inf` (default `0`)

Notes: Maximum size is `5` . Initial valence can be set with a float passed to the `initialValues` parameter, and valence can be set with a float passed to the `finalValues` parameter.

### Decoy Goal

<img align="right" height="100" src="/docs/figs/prefabs/ValencedObjects/DecoyGoal.png" />

* **Name**: `DecoyGoal`
* **Size Range**: `0.5-5`
* **Valence**: `0` - no reward in/decrement
* **Color**: Not changeable / (grey)

Note: The agent's reward is not affected when it touches the decoy goal. It is simply a tool for visual distraction or to create a more complex environment without having the agent's reward affected.

_Available from Animal-AI v4.1.0 onwards._

### Episode-Ending DeathZone

<img align="right" height="100" src="/docs/figs/prefabs/ValencedObjects/DeathZone.png" />

* **Name**: `DeathZone`
* **Size Range**: `(1,0.5,1)-(40,10,40)`
* **Valence**: `-1`
* **Color**: Not changeable / (red)

### Non-Episode-Ending HotZone

<img align="right" height="100" src="/docs/figs/prefabs/ValencedObjects/HotZone.png" />

* **Name**: `HotZone`
* **Valence**: `min(-10/t, -0.00001)` for `t > 0`,  `-0.00001` otherwise, where `t` is the number of steps in the episode
* **Color**: Not changeable / (orange)

Notes: When the agent enters the hot zone, reward decrement is accelerated by a factor of 10 compared to time alone. If a `DeathZone` and a `HotZone` overlap, `DeathZone` prevails.

### 'Bounce' Valenced Objects

Every valenced object (rewards) has a physics-enabled version called Bounce (e.g. GoodGoalBounce), which has an initial velocity at the start of an episode. Furthermore, the objects have gravity enabled which allows them to bounce off the walls and other objects (hence the name).

## Spawners

These objects dispense valenced objects. They are immovable (can't be displaced from their original positions) and have aliases (alternative names) for backwards compatibility with previous versions of AAI.

### SpawnerTree

<img align="right" height="100" src="/docs/figs/prefabs/Dispensers/SpawnerTree.png" />

* **Name**: `SpawnerTree`
* **Size**: Fixed (`5.19 x 5.95 x 5.02`)
* **Spawned Goal Size Range**: `0.2-3`
* **Number of goals to spawn** (`spawnCounts`): `0-Inf` (leave blank or set to `-1` to spawn infinitely)
* **Color**: Not changeable / (green and brown)
* **Growth Onset Delay Range (frames)** (`delays`): `0-Inf` (default `0`)

Notes: The tree spawns `GoodGoalMulti` . They grow on the trees before dropping to the floor once they have reached their final size. The starting size of the goals can be set with the `initialValues` parameter (default: `0.2` ) and the final size with the `finalValues` parameter (default: `1.0` ). The valence of the goals is proportional to their size. The number of seconds it takes to 'grow' the goals on the tree (relative to the timescale of the environment) can be set with the `ripenTimes` parameter. The number of seconds between spawnings (relative to the timescale of the environment) can be set with the `timesBetweenSpawns` parameter (default: 4.0).

### SpawnerDispenserTall

<img align="right" height="100" src="/docs/figs/prefabs/Dispensers/SpawnerDispenserTall.png" />

* **Name**: `SpawnerDispenserTall`
* **Size**: Fixed (`1.67 x 4.46 x 1.67`)
* **Spawned Goal Size Range**: `0.2-1`
* **Number of goals to spawn** (`spawnCounts`): `0-Inf` (leave blank or set to `-1` to spawn infinitely)
* **Color**: RGB range `(0,0,0)-(255,255,255)`
* **Growth Onset Delay Range (frames)** (`delays`): `0-Inf` (default `0`)
* **Alias**: `SpawnerDispenser`

Notes: The dispenser spawns `GoodGoalMulti`. The valence of the goals is proportional to their size. The number of seconds between spawnings (relative to the timescale of the environment) can be set with the `timesBetweenSpawns` parameter (default: 1.5). The object has a door that can be animated to open and close.  The number of seconds before the door opens can be set with the `doorDelays` parameter (default: `10.0` ), and the number of seconds the door remains open for can be ste with the `timesBetweenDoorOpens` parameter (default: `-1` , if `< 0` then, once opened, the door stays open permanently).

### SpawnerContainerShort

<img align="right" height="100" src="/docs/figs/prefabs/Dispensers/SpawnerContainerShort.png" />

* **Name**: `SpawnerDispenserShort`
* **Size**: Fixed (`1.67 x 1.67 x 1.67`)
* **Spawned Goal Size Range**: `0.2-1`
* **Number of goals to spawn** (`spawnCounts`): `0-Inf` (leave blank or set to `-1` to spawn infinitely)
* **Color**: RGB range `(0,0,0)-(255,255,255)`
* **Growth Onset Delay Range (frames)** (`delays`): `0-Inf` (default `0`)
* **Alias**: `SpawnerDispenser`

Notes: The dispenser spawns `GoodGoalMulti` . The valence of the goals is proportional to their size. The number of seconds between spawnings (relative to the timescale of the environment) can be set with the `timesBetweenSpawns` parameter (default: 1.5). The object has a door that can be animated to open and close.  The number of seconds before the door opens can be set with the `doorDelays` parameter (default: `10.0` ), and the number of seconds the door remains open for can be ste with the `timesBetweenDoorOpens` parameter (default: `-1` , if `< 0` then, once opened, the door stays open permanently).

### SpawnerButton

<img align="right" height="100" src="/docs/figs/prefabs/Dispensers/SpawnerButton.png" />

* **Name**: `SpawnerButton`
* **Size**: Fixed (`1.30 x 1.30 x 1.30`)
* **Spawned Goal Size**: `1`
* **Color**: Not changeable / (yellow and light blue)
* **Alias**: `Pillar-Button`
* **Spawned Reward Size**: `spawnedRewardSize` (Optional, defaults to 1)

Notes: Spawns a goal when the player/agent *interacts* with it by colliding with the physical button object (blue). The position of the spawned goal can be set with the a `!Vector3` passed to the `rewardSpawnPos` parameter. The probability that a goal will spawn upon a press can be set with a float between 0 and 1 passed to the `spawnProbability` parameter. Different valenced objects can be spawned on different presses. A list, such as `["GoodGoal", "BadGoal", "GoodGoalMulti"]` , can be passed to `rewardNames` to define the valenced objects (only these three are supported at the moment). A corresponding list of floats between 0 and 1 can be passed to the `rewardWeights` to determine the probability of spawning each of the types of valenced object. The probabilities are normalized to sum to one. The number of frames taken for the button to depress upon touching it can be defined with `moveDurations` , and the number of frames for the button to be reset before it can be pressed again can be set with `resetDurations`.


## Sign Boards

* **Name**: `Sign Boards`
* **Size**: Fixed (`1.40 x 1.40 x 1.40`)
* **Color**: RGB range (0,0,0)-(255,255,255) (only the background color can be changed, the symbols are fixed in color)
* **Alias**: `SignPosterboard`
* **Symbol Names**: a list of strings, the names of the symbols to display:
  - "tick"
  - "u-turn-arrow"
  - "circle"
  - "letter-a"
  - "right-arrow"
  - "left-arrow"
  - "up-arrow"
  - "down-arrow"
  - "cross"


<p align="center">
  <img height="250" src="/docs/figs/exampleGallery/SignPosterboard-preset-symbols.PNG">
</p>

<p align="center">
  <img height="250" src="/docs/figs/exampleGallery/SignPosterboard-special-symbols-annotated.png">
</p>

Sign boards are immovable objects that display a symbol. They can be used to create tasks where the agent has to navigate to a specific location or to perform a specific action.

## Ready-Made Configuration File

For a complete list of all spawnable objects and their default values, see the [Arena Objects.yml](/docs/configGuide/Arena-Objects.yaml) file. It is ready to use and can be copied and pasted into a configuration file.
