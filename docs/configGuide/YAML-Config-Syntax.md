# Detailed Arena Config Guide

#### Table of Contents

1. [Introduction](#introduction)
2. [Understanding YAML Syntax](#understanding-yaml-syntax)
   2.1 [YAML Hierarchical Syntax](#yaml-hierarchical-syntax)
   2.2 [Global Parameters](#global-parameters)
   2.3 [Local Parameters](#local-parameters)
3. [Example YAML Configurations](#examples-of-yaml-configurations)
   3.1 [Example 1 - Standard Parameters & Randomisation](#example-1---standard-parameters--randomisation)
   3.2 [Example 2 - Decay Goals / Size-Changing Goals](#example-2---decay-goals--size-changing-goals)
   3.3 [Example 3 - SignBoard (Preset Symbols)](#example-3---signboard-preset-symbols)
   3.4 [Example 4 - SignBoard (Special Symbols)](#example-4---signboard-special-symbols)
   3.5 [Example 5 - SpawnerButton (Interactive Objects)](#example-5---spawnerbutton-interactive-objects)
   3.6 [Example 6 - Multiple Arenas (Randomisation)](#example-6---multiple-arenas-randomisation)
   3.7 [Example 7 - Arena 'Blackouts'](#example-7---arena-blackouts)
   3.8 [Example 8 - Multi-Arena Episodes](#example-8---multi-arena-episodes)
4. [Conclusion](#conclusion)
5. [Further Reading and Documentation](#further-reading-and-documentation)


### Introduction

In this guide, we'll explore how to use the custom YAML syntax in Animal-AI to create your own unique arenas. We'll start with basic examples to familiarize ourselves with the syntax and gradually progress to more complex scenarios. Let's begin by covering the essentials of the syntax!


### Understanding YAML Syntax

#### YAML Hierarchical Syntax

```YAML
# Note: In later versions of Animal-AI, the arena size will be configurable and be set dynamically via a separate parameter.
!ArenaConfig
arenas:
  0: !Arena 
  items: 
    ... # rest of configuration file...
    .
    .
    .
  n: !Arena
  items: 
    ... # rest of configuration file...
```

**Observations:**

We can observe the following syntax structure:

* `!ArenaConfig` is the root tag.
* `arenas` is the tag for the arenas, representing an ordered list of arenas.
* `0` denotes the first arena in the file, while `n` represents the nth arena.
* `!Arena` is the tag for an individual arena, followed by a list of parameters that define the arena.
* `items` is the tag for the objects to be spawned in the arena, represented as a list.

The `!ArenaConfig` tag indicates that the YAML file is used for configuring arenas. The `arenas` tag signifies that the file contains one or more arena configurations. The `0` tag marks the beginning of the arena sequence, continuing up to `n arenas`.

The `!Arena` tag specifies that the following YAML content defines an arena. The `!` symbol denotes a custom class; in this case, `!Arena` indicates that the file describes an arena configuration specific to Animal-AI environments.

Following the `!Arena` tag, a list of parameters is provided to define the arena, including the objects to spawn in that arena. Some parameters, such as `t` (renamed to `timeLimit` in build v4.1.0) and `pass_mark` (renamed to `passMark` in build v4.1.0), apply locally to the arena. Other parameters apply globally. Refer to the example below for further details.

#### Global Parameters

```YAML
!ArenaConfig
# Global Parameters that are optional are put here, at the top of the yaml file under the !ArenaConfig tag.
canChangePerspective: false # Can the agent change its camera perspective? (i.e. switch between first-person and third-person view)
canResetEpisode: false # Can the agent reset the episode? 
showNotification: false # Show the notification to the user upon completion of the episode? 
randomizeArenas: false # Randomize the arenas? This applies if there are > 1 arenas in the file. 
arenas:
  0: !Arena
    ... # rest of configuration file...

```

**Observations:**

We can observe the following:

* The default values for global parameters are:
  - `canChangePerspective: true`
  - `canResetEpisode: true`
  - `showNotification: false`
  - `randomizeArenas: false`
  
Global parameters are optional. If not defined, these default values are used.

* If global parameters are not provided, the default values are applied. For instance, if no value is specified for `canChangePerspective`, it defaults to `true`.

* When a value is provided for a global parameter, it applies to all arenas in the file. For example, setting `canChangePerspective` to `false` will prevent the agent from changing its perspective in all arenas. Conversely, setting it to `true` will allow perspective changes in all arenas.

In the example above, global parameters are defined before the arenas, affecting all arenas in the file. Note that these parameters apply only during `Play` mode, not during agent `Training` mode as the agent's perspective is controlled by the training algorithm.

#### Local Parameters

```YAML
!ArenaConfig
arenas:
  0: !Arena
    timeLimit: 0 # Time limit for the arena. This is a local parameter, and is only applicable to this arena.
    passMark: 100 # Pass mark for the arena (i.e. the minimum reward required to pass the arena). This is a local parameter, and is only applicable to this arena.
    items: # List of objects to spawn in the arena. This is a list which is converted to a GameObject array in Unity.
    - !Item # An individual object to spawn in the arena. This object is then added to the list of objects to spawn in the arena.
      name: Agent
      positions:
      - !Vector3 {x: 10, y: 0, z: 20}
      rotations: [90]
      skins:
      - "hedgehog"

  1: !Arena # Note that the arena number is 1, meaning this is the second arena in the file. Each arena must have a unique number and the first arena must be 0.
    timeLimit: 100
    passMark: 0
    items: # List of objects to spawn in the arena. This is a list which is converted to a GameObject array in Unity.
    - !Item # An individual object to spawn in the arena. This object is then added to the list of objects to spawn in the arena.
      name: Agent
      positions:
      - !Vector3 {x: 10, y: 0, z: 20}
      rotations: [90]
      skins:
      - "hedgehog"
```

**Observations:**

Regarding Arena and Item local parameters, we can observe the following:

* **Arena-Specific Parameters:** These parameters apply only to the arena in which they are defined. For instance, if `t` (time limit) is set to `250`, the time limit for that particular arena will be 250 seconds. If another arena within the same YAML configuration file has `t` set to `500`, then that arena will have a time limit of 500 seconds. These parameters are relevant for both `Play` and `Training` modes.

* **Item-Specific Parameters:** The properties defined for each "Item" are local to that specific object. For example, if an `Agent` object is assigned a `hedgehog` skin, only that `Agent` object will have a `hedgehog` skin within that arena.

```YAML
!ArenaConfig
arenas:
  0: !Arena
    timeLimit: 100
    passMark: 0
    items: # List of objects to spawn in the arena. This is a list which is converted to a GameObject array in Unity.
    - !Item # An individual object to spawn in the arena. This object is then added to the list of objects to spawn in the arena.
      name: Agent
      ... # rest of Agent parameters...

    - !Item
      name: Wall
      positions:
      - !Vector3 {x: 10, y: 0, z: 10}
      colors:
      - !RGB {r: 204, g: 0, b: 204 }
      rotations: [45]
      sizes:
      - !Vector3 {x: 5, y: 5, z: 5}
      
    - !Item
      name: Wall
      positions:
      - !Vector3 {x: 10, y: 10, z: 10}
      colors:
      - !RGB {r: 204, g: 0, b: 204 }
      rotations: [0]
      sizes:
      - !Vector3 {x: 1, y: 1, z: 1}
```

* Additionally, the `!Item` tag includes its own local parameters, which we refer to as _item-specific_ local parameters. These parameters apply exclusively to the object in which they are defined. For instance, if a `Wall` object is defined twice within the same arena (as shown in the example YAML snippet above), the local parameters such as position, size, color, and rotation specified for the first `Wall` will not affect the second `Wall` in the same arena.

The syntax provides significant flexibility, allowing multiple objects of the same type to be defined with different properties within the same arena without any conflicts.

Next, we will explore more complex examples to better understand how to use YAML syntax in Animal-AI for creating custom arenas.

### Examples of YAML Configurations

Let's take a look at some examples to understand how to use the YAML syntax in Animal-AI to create custom arenas.

#### EXAMPLE 1 - Standard Parameters & Randomisation

```YAML
!ArenaConfig
arenas:
  0: !Arena
    timeLimit: 100
    passMark: 0
    items:
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 10, y: 0, z: 20}
      skins: # Optional parameter. If not specified, a random skin will be assigned.
      - "hedgehog"

    - !Item
      name: Wall
      positions:
      - !Vector3 {x: 10, y: 0, z: 10}
      - !Vector3 {x: -1, y: 0, z: 30}
      # Note that the second wall game object has a '-1' value defined for x axis, which means that the x axis will be randomomized.
      colors:
      - !RGB {r: 204, g: 0, b: 204 }
      - !RGB {r: 204, g: 0, b: 204 }
      rotations: [45, 45] # Optional parameter for the rotation of the object. If not specified, the object is not rotated.
      sizes:
      - !Vector3 {x: -1, y: 5, z: -1}

    - !Item
      name: CylinderTunnel
      positions:
      - !Vector3 {x: 20, y: 0, z: 20}
      - !Vector3 {x: 30, y: 0, z: 20}
      - !Vector3 {x: 40, y: 0, z: 20}
      colors:
      - !RGB {r: 204, g: 0, b: 204 }
      - !RGB {r: 204, g: 0, b: 204 }
      - !RGB {r: 204, g: 0, b: 204 }
```

<p align="center">
  <img height="250" src="/docs/figs/exampleGallery/Yaml-Config-Syntax-Arenas/example1.png">
</p>

**Observations:**

* The number of parameters for `positions`, `rotations`, and `sizes` do not need to be equal.
* The environment will spawn `max(len(positions), len(rotations), len(sizes))` objects.
* Missing parameters will be assigned randomly. For instance, if `positions` are specified but `sizes` are not, the environment will assign random sizes to the objects.

In this case, the objects will spawn in the following order:

* A pink Cube will appear at coordinates `[10, 10]` on the ground, with a rotation of `45` degrees. Its size will be random along the `x` and `z` axes, with a fixed size of `y=5`.
* Another Cube will be placed on the ground at a random `x` coordinate and `z=30`. This cube's rotation, size, and color will be randomly determined.
* Three `CylinderTunnel` objects will spawn next, each with random values for position, size, color, and rotation.
* A `GoodGoal` object will then appear, with all its attributes randomized.
* Finally, the agent will spawn first. This is noteworthy as it takes priority over all other objects and will be placed before any other objects.

&nbsp; 

#### EXAMPLE 2 - Decay Goals / Size-Changing Goals

```YAML
!ArenaConfig
arenas:
  0: !Arena
    timeLimit: 100
    passMark: 0
    items:
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 10, y: 0, z: 20}
      rotations: [90]
      skins:
      - "hedgehog"
    - !Item
      name: ShrinkGoal
      positions:
      - !Vector3 {x: 20, y: 0, z: 11}
      sizes:
      - !Vector3 {x: 0.1, y: 0.1, z: 0.1}
      initialValues: [2.5]
      finalValues: [1.5]
      delays: [400]
      changeRates: [-0.2]
    - !Item
      name: DecayGoal
      positions:
      - !Vector3 {x: 20, y: 0, z: 17}
      initialValues: [4]
      finalValues: [3]
      delays: [250]
      changeRates: [-0.003]
    - !Item
      name: AntiDecayGoal
      positions:
      - !Vector3 {x: 20, y: 0, z: 23}
      sizes:
      - !Vector3 {x: 0.1, y: 0.1, z: 0.1}
      initialValues: [1]
      finalValues: [1.5]
      delays: [300]
      changeRates: [-0.007]
    - !Item
      name: GrowGoal
      positions:
      - !Vector3 {x: 20, y: 0, z: 29}
      initialValues: [1]
      finalValues: [3.5]
      delays: [100]
      changeRates: [0.01]
```

<p align="center">
  <img height="250" src="/docs/figs/exampleGallery/Yaml-Config-Syntax-Arenas/example2.png">
</p>

**Observations:**

This example demonstrates various goal types that undergo transformations such as `decay`, `growth`, `shrinkage`, and `ripening` (anti-decay). Each `Item` in this setup includes certain parameters that may be irrelevant or used incorrectly. These extraneous parameters, although not utilized effectively, do not affect the overall outcome or cause issues within the AAI environment.

In this scenario:

* The `ShrinkGoal` and `GrowGoal` ignore the `sizes` parameter and instead adjust their sizes based on `initialValues` and `finalValues`.
* For both `DecayGoal` and `AntiDecayGoal`, the size is determined by the greater of the `initialValue` or `finalValue`.
* Additionally, the reward for these goals transitions from the initial value to the final value over time.
* Notably, the `ShrinkGoal` includes a `symbolNames` parameter, which is generally intended for `SignBoard` objects. This parameter is not applicable in this context and is therefore ignored.
* An 'animal skin' feature is also utilized in this example, where the `Agent` is configured to always display a 'hedgehog' skin.

&nbsp; 

#### EXAMPLE 3 - SignBoard (Preset Symbols)

```YAML
!ArenaConfig
arenas:
  0: !Arena
    timeLimit: 100
    passMark: 0
    items:
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 10, y: 0, z: 20}
      rotations: [90]
    - !Item
      name: SignBoard
      positions: # Note that the positions, rotations, and sizes parameters must be of the same length 
      # ...(i.e. if there are 5 positions, there must be 5 rotations and 5 sizes).
      - !Vector3 {x: 20, y: 0, z: 8}
      - !Vector3 {x: 20, y: 0, z: 14}
      - !Vector3 {x: 20, y: 0, z: 20}
      - !Vector3 {x: 20, y: 0, z: 26}
      - !Vector3 {x: 20, y: 0, z: 32}
      rotations: [0, 0, 0, 0, 0]
      sizes:
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      symbolNames: # Note also that the symbolNames parameter must be of the same length as the positions parameters 
      # ...(i.e. if there are 5 positions, there must be 5 symbolNames). Each position is an instance of a SignBoard object, and each SignBoard object can only have one symbol.
      - "left-arrow"
      - "letter-a"
      - "circle"
      - "u-turn-arrow"
      - "tick"
```

<p align="center">
  <img height="250" src="/docs/figs/exampleGallery/Yaml-Config-Syntax-Arenas/example3.png">
</p>

**Observations:**

This example demonstrates the use of predefined symbols via the `symbolNames` parameter, which is specific to `SignBoard` objects. Each symbol in the `symbolNames` list is associated with a default color. However, these default colors do not influence the appearance of the symbols on the `SignBoard`. Instead, the color of the `SignBoard` gameobject is determined solely by the `colors` parameter.

&nbsp; 

#### EXAMPLE 4 - SignBoard (Special Symbols)

```YAML
!ArenaConfig
arenas:
  0: !Arena
    timeLimit: 100
    passMark: 0
    items:
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 10, y: 0, z: 20}
      rotations: [90]
    - !Item
      name: SignBoard
      positions:
      - !Vector3 {x: 20, y: 0, z: 8}
      - !Vector3 {x: 20, y: 0, z: 14}
      - !Vector3 {x: 20, y: 0, z: 20}
      - !Vector3 {x: 20, y: 0, z: 26}
      - !Vector3 {x: 20, y: 0, z: 32}
      rotations: [0, 0, 0, 0, 0]
      sizes:
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      symbolNames:
      - "01/10"    
      - "111/110/001"    
      - "001010/011000/100001/101010/111001"    
      - "0101/**10/0010/0***"
      - "13x11"
```

<p align="center">
  <img height="250" src="/docs/figs/exampleGallery/Yaml-Config-Syntax-Arenas/example4.png">
</p>

**Observations:**

This example illustrates the use of *special codes* to create black-and-white pixel grids as symbols. The encoding is as follows:
- `0` represents black,
- `1` represents white,
- `*` is a 'joker' character that randomly outputs either black or white.

The grid's dimensions are specified using the `/` character. Each row of the grid must be enclosed between `/` characters, and all rows must be of the same length for the code to be valid.

To generate fully-random grids, use the code format `"MxN"`, where `M` and `N` represent the grid's width and height, respectively. For example, `"5x3"` will produce a 5x3 grid.

&nbsp; 

#### EXAMPLE 5 - SpawnerButton (Interactive Objects)

```YAML
!ArenaConfig
arenas:
  0: !Arena
    timeLimit: 100
    passMark: 0
    items:
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 10, y: 0, z: 20}
      rotations: [90]
    - !Item
      name: SpawnerButton
      positions:
      - !Vector3 {x: 10, y: 0, z: 10}
      sizes:
      - !Vector3 {x: 5, y: 5, z: 5}
      rotations: [0]
      # Note that the SpawnerButton is a modular object and the colors are fixed for each part of the game object in order to remove
      # ... the occurance of each part having the same color, which would be confusing for the player/agent.
      moveDurations: [0.1]
      resetDurations: [1.0]
      rewardNames: ["GoodGoal", "BadGoal", "GoodGoalMulti"]
      rewardWeights: [100, 0, 0]
      spawnProbability: 1.0
      maxRewardCounts: [-1, -1, -1]
      rewardSpawnPos: !Vector3 {x: 25, y: 0, z: 23} # The position where the reward will be spawned.
      spawnedRewardSize: !Vector3 {x: 1, y: 1, z: 1} # the size of the reward
```

<p align="center">
  <img height="250" src="/docs/figs/exampleGallery/Yaml-Config-Syntax-Arenas/example5.png">
</p>

**Observations:**

* The `SpawnerButton` is an interactive object that can be engaged by the player or agent.
* It is a modular object consisting of multiple modules.

In the example above, the `SpawnerButton` is used to spawn rewards upon interaction (such as 'colliding' with the gameobject). The `SpawnerButton` has several parameters that define its behavior:

* `moveDurations`: Specifies how long the button moves when pressed.
* `resetDurations`: Specifies how long the button takes to reset after being pressed.
* `rewardNames`: A list of rewards that can be spawned.
* `rewardWeights`: Determines the weight of each reward in the `rewardNames` list. Weights control the probability of each reward being spawned. For instance:
  - With weights `[100, 0, 0]`, the probability of spawning the first reward is 100%, and the other rewards have 0% probability.
  - With weights `[50, 50, 0]`, the probability of spawning the first and second rewards is 50% each, with 0% for the third reward.
  - With weights `[33, 33, 33]`, each reward has an equal probability of 33%.
* `spawnProbability`: Controls the overall chance of spawning any reward upon interaction. This works in conjunction with `rewardWeights`:
  - With `rewardWeights` set to `[100, 100, 100]` and `spawnProbability` set to `0.5`, the chance of spawning a reward is 50% per interaction.
  - With `rewardWeights` set to `[100, 100, 100]` and `spawnProbability` set to `0.0`, the chance of spawning a reward is 0%, meaning no reward will spawn.
* `maxRewardCounts`: Defines the maximum number of times each reward can be spawned. A value of `-1` indicates no limit per episode.
* `rewardSpawnPos`: Specifies the location where the reward will appear. If not specified, the reward will be spawned randomly within the arena.

&nbsp; 

#### EXAMPLE 6 - Multiple Arenas (Randomisation)

```YAML
!ArenaConfig
randomizeArenas: true # Here, we set randomizeArenas to true, which means that the arenas will be randomized upon play. Note that this is not applicable to training mode.
arenas:
  0: !Arena
    timeLimit: 100
    passMark: 0
    items:
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 10, y: 0, z: 20}
      rotations: [90]
    - !Item
      name: SpawnerButton
      positions:
      - !Vector3 {x: 10, y: 0, z: 10}
      sizes:
      - !Vector3 {x: 5, y: 5, z: 5}
      rotations: [0]
      moveDurations: [0.1]
      resetDurations: [1.0]
      rewardNames: ["GoodGoal", "BadGoal", "GoodGoalMulti"]
      rewardWeights: [100, 0, 0]
      spawnProbability: 1.0
      maxRewardCounts: [-1, -1, -1]
      rewardSpawnPos: !Vector3 {x: 25, y: 0, z: 23}

  1: !Arena # We define a second arena. However, for example sake, the second arena has the same objects and parameters as the first arena.
    timeLimit: 100
    passMark: 0
    items:
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 10, y: 0, z: 20}
      rotations: [90]
    - !Item
      name: SpawnerButton
      positions:
      - !Vector3 {x: 10, y: 0, z: 10}
      sizes:
      - !Vector3 {x: 5, y: 5, z: 5}
      rotations: [0]
      moveDurations: [0.1]
      resetDurations: [1.0]
      rewardNames: ["GoodGoal", "BadGoal", "GoodGoalMulti"]
      rewardWeights: [100, 0, 0]
      spawnProbability: 1.0
      maxRewardCounts: [-1, -1, -1]
      rewardSpawnPos: !Vector3 {x: 25, y: 0, z: 23}

```

<table>
  <tr>
    <td><img src="/docs/figs/exampleGallery/Yaml-Config-Syntax-Arenas/example5.png" width="500"/>
    <p>Arena 0 </p></td>
    <td><img src="/docs/figs/exampleGallery/Yaml-Config-Syntax-Arenas/example6.png" width="500"/><p>Arena 1</p></td>
  </tr>
</table>

**Observations:**

We can observe the following:

* Setting `randomizeArenas` to `false` ensures that arenas are played in the order they are defined in the file. For instance, with `randomizeArenas` set to `false`, the first arena will be played first, followed by the second arena.
* Setting `randomizeArenas` to `true` enables randomization of the arenas. In this case, the arenas will be played in a random order. After all arenas have been cycled through once, the sequence will start again from the beginning.

In the provided example, two arenas are defined, and `randomizeArenas` is set to `true`. This means that the arenas will be played in a randomized order. It's important to note that this randomization does not apply during training mode. Consequently, the order of arena definition is irrelevant since the arenas will be randomized during play. Also, remember that `randomizeArenas` affects only the order of arenas in the file and does not impact the objects within each arena.

&nbsp; 

#### EXAMPLE 7 - Arena 'Blackouts'

```YAML
!ArenaConfig
arenas:
  0: !Arena
    timeLimit: 100
    passMark: 0
    blackouts: [10, 43, 50, 20] # We are defining the blackout times (in frames) for the arena at interval frames [10, 43], and [50 and 60]. The blackout zones are defined in frames, not in seconds. Note that the intervals are increasing in value from left to right, meaning. for example, a blackout can't start at frame 43 and end at frame 10.
    items:
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 10, y: 0, z: 20}
      rotations: [90]
```

<p align="center">
  <img height="250" src="/docs/figs/exampleGallery/Yaml-Config-Syntax-Arenas/example7.png">
</p>

**Observations:**

We can observe the following:

* The `blackouts` parameter defines the blackout zones for the arena. This parameter is a list of frames at which the arena will experience a blackout. During these frames, the player will not receive any visual information, as no light will be emitted to the arena.
* If `blackouts` is set to a negative value, such as `[-20]`, the arena will experience a blackout every 20 frames. The '-' sign indicates that the blackout should repeat at regular intervals.
* The blackout only affects visual visibility and does not impact other aspects of the agent or the arena. For example, the agent can still move around, and the objects within the arena remain visible to the agent. _RayCasting_ will continue to function as usual.

&nbsp;

#### EXAMPLE 8 - Multi-Arena Episodes

```YAML
!ArenaConfig
arenas:
  0: !Arena
    timeLimit: 50
    mergeNextArena: true # Here, we set mergeNextArena to true, which means that the next arena will be merged with this arena, creating a single episode.
    items:
    - !Item
      name: GoodGoal
      positions:
      - !Vector3 {x: 20, y: 0, z: 25}
      rotations: [0]
      sizes:
      - !Vector3 {x: 1, y: 1, z: 1}
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 20, y: 0, z: 20}
      rotations: [0]

  1: !Arena
    timeLimit: 50
    items:
    - !Item
      name: GoodGoal
      positions:
      - !Vector3 {x: 20, y: 0, z: 15}
      rotations: [0]
      sizes:
      - !Vector3 {x: 1, y: 1, z: 1}
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 20, y: 0, z: 20}
      rotations: [0]
      sizes:
      - !Vector3 {x: 1, y: 1, z: 1}
```

**Observations:**

In some scenarios, you may want to include multiple arenas within a single episode—such as when testing in-context learning for maze navigation. This can be achieved by setting the `mergeNextArena` parameter to `true`. 

For instance, in the example provided, setting `mergeNextArena` to `true` causes Animal-AI to treat arena 0 (where the reward is located ahead of the agent) and arena 1 (where the reward is behind) as a single continuous unit. The episode will only conclude when either the episode fails or both arenas are completed. 

You can extend this approach to merge more than two arenas by setting the `mergeNextArena` parameter in each arena, which will sequentially add the next arena to the current episode.

### Conclusion

We hope that this guide has helped you understand how to use the YAML syntax in Animal-AI to create custom arenas. 

### Further Reading and Documentation

For more information on how YAML works, please refer to the [YAML documentation](https://yaml.org/spec/1.2/spec.html). If you are still unsure about how to use the YAML syntax, please refer to the [Background-YAML](/docs/Background-YAML.md) guide for a closer look into how YAML is used.

---
