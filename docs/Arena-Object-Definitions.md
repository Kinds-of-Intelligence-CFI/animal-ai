# Animal-AI Environment Objects

### Table of Contents
1. [Introduction](#introduction)
2. [Unity Objects - What are they?](#unity-objects---what-are-they)
3. [Immovable Objects](#immovable-objects)
4. [Movable Objects](#movable-objects)
5. [Rewards](#rewards)
6. [Reward Spawners](#reward-spawners)
7. [Other/Unique Objects](#otherunique-objects)

## Introduction

The Animal-AI environment comprises various objects categorized into _immovable_, _movable_, _rewards_, and _other/unique_ types. These objects can be configured in numerous ways to create diverse tasks. Each object's name, default characteristics, and configurable ranges are detailed below. All objects can rotate 360 degrees. Unity uses a left-handed coordinate system with `y` as the vertical axis, and `x` and `z` axes representing horizontal and depth dimensions, respectively.


## Unity Objects - What are they?

Briefly, Unity game objects, commonly referred to as *GameObjects*, are the fundamental components in the Unity Engine, serving as containers for all other components or functionalities within a Unity scene. These objects can represent characters, props, scenery, cameras, lights, and more. Each GameObject can be equipped with various components such as scripts, renderers, colliders, or custom components, defining their behavior and interaction within the game world. *Prefabs* in Unity are essentially templates created from GameObjects; they allow developers to create, configure, and store a GameObject complete with its components and properties. Once a Prefab is created, it can be reused multiple times across the scene or even across different projects, ensuring consistency and efficiency in game development by allowing changes to be made to multiple instances simultaneously.

## Immovable Objects

_Immovable_ objects are fixed in place and cannot be moved. The outer walls of the arena are also immovable and are permanently fixed in place to prevent the player/agent from escaping the arena.

<table>
  <tr>
    <td><img src="../../docs/media/prefabs/arena/arena-2DView.png" width="500"/>
    <p>2D view of the Arena</p></td>
    <td><img src="../../docs/media/prefabs/arena/arena-FP.png" width="500"/><p>First-person view of agent</p></td>
    <td><img src="../../docs/media/prefabs/arena/arena-New.png" width="500"/><p>Full view of arena</p></td>
  </tr>
  <tr>
    <td><img src="../../docs/media/prefabs/arena/arena-Ground.png" width="500"/><p>Close-up of arena ground</p></td>
    <td><img src="../../docs/media/prefabs/arena/arena-TP.png" width="500"/><p>Third Persion view of one of the agent skins</p></td>
    <td><img src="../../docs/media/prefabs/arena/arena-Walls.png" width="500"/><p>Side view of walls</p></td>
  </tr>
</table>

### Wall
- **Name**: `Wall`
- **Size Range**: `(0.1,0.1,0.1)-(40,10,40)`
- **Color**: Changeable (Default: Grey, RGB: 153, 153, 153)

### Transparent Wall
- **Name**: `WallTransparent`
- **Size Range**: `(0.1,0.1,0.1)-(40,10,40)`
- **Color**: Not changeable

### Ramp
- **Name**: `Ramp`
- **Size Range**: `(0.5,0.1,0.5)-(40,10,40)`
- **Color**: Changeable (Default: Pink, RGB: 255, 0, 255)

### Tunnel
- **Name**: `CylinderTunnel`
- **Size Range**: `(2.5,2.5,2.5)-(10,10,10)`
- **Color**: Changeable (Default: Grey, RGB: 153, 153, 153)

### Transparent Tunnel
- **Name**: `CylinderTunnelTransparent`
- **Size Range**: `(2.5,2.5,2.5)-(10,10,10)`
- **Color**: Not changeable

## Movable Objects

_Movable_ objects can be easily moved by the agent or other objects. These objects can be pushed by the player/agent as the physics engine is enabled for these objects directly.

### Light Cardboard Box
- **Name**: `Cardbox1`
- **Size Range**: `(0.5,0.5,0.5)-(10,10,10)`
- **Color**: Not changeable

### Heavy Cardboard Box
- **Name**: `Cardbox2`
- **Size Range**: `(0.5,0.5,0.5)-(10,10,10)`
- **Color**: Not changeable

### U-shaped Object
- **Name**: `UObject`
- **Size Range**: `(1,0.3,3)-(5,2,20)`
- **Color**: Not changeable

### L-shaped Object
- **Name**: `LObject`
- **Size Range**: `(1,0.3,3)-(5,2,20)`
- **Color**: Not changeable

### L-shaped Object Variation
- **Name**: `LObject2`
- **Size Range**: `(1,0.3,3)-(5,2,20)`
- **Color**: Not changeable

## Rewards

Rewards are objects that provide positive or negative feedback to the agent. These objects are stationary or moving, and can be configured to provide positive or negative rewards to the agent. The agent collides with these objects to receive feedback. 

### Stationary Positive Goal
- **Name**: `GoodGoal`
- **Reward Range**: `1`
- **Color**: Not changeable

### Moving Positive Goal
- **Name**: `GoodGoalBounce`
- **Reward Range**: `1`
- **Color**: Not changeable

### Stationary Negative Goal
- **Name**: `BadGoal`
- **Reward Range**: `-1`
- **Color**: Not changeable

### Moving Negative Goal
- **Name**: `BadGoalBounce`
- **Reward Range**: `-1`
- **Color**: Not changeable

### Stationary Positive Reward
- **Name**: `GoodGoalMulti`
- **Size Range**: `0.5-5`
- **Color**: Not changeable

### Moving Positive Reward
- **Name**: `GoodGoalMultiBounce`
- **Reward Range**: `0.5-5`
- **Color**: Not changeable

### Decay Reward
- **Name**: `DecayGoal`
- **Reward Range**: `1 - (-0.005)`
- **Color**: Not changeable
Notes: The Decay Reward is a reward that physically gets smaller (decays) over time. The reward is set to a default value of 1, and decays by 0.005 every time step.

## Grow Reward
- **Name**: `GrowGoal`
- **Reward Range**: `0.5 + 0.01, with a max of 5`
- **Color**: Not changeable
Notes: The Grow Reward is a reward that phyisically grows over time. The reward is set to a default value of 0.5, and grows by 0.01 every time step. The reward has a maximum value of 5.

## Ripen Reward
- **Name**: `RipenGoal`
- **Reward Range**: `0 + 0.01, with a max of 3`
- **Color**: Not changeable
Notes: The Ripen Reward is a reward that 'ripens' (increases in reward value) over time. The reward is set to a default value of 0, and ripens by 0.01 every time step. The reward has a maximum value of 3 after which the value does not increase further.

## DeathZone
- **Name**: `DeathZone`
- **Reward Range**: `-1`
- **Color**: Not changeable
Notes: The DeathZone is a reward that has a default value of -1. The DeathZone is meant to be used as a fatal punishment mechanisim for the player/agent. If the player/agent collides with the DeathZone (i.e. steps on it), the episode is terminated and the player/agent is reset to the starting position.

## HotZone
- **Name**: `HotZone`
- **Reward Range**: `-10`
- **Color**: Not changeable
Notes: The HotZone is a reward that has a default value of -10. The HotZone is meant to be used as a steady punishment mechanisim for the player/agent. If the player/agent collides with the HotZone (i.e. steps on it and continues to do so) they will be inflicted with a -10 health penalty at every second they are in the zone. The episode is terminated and the player/agent is reset to the starting position if the player/agent's health reaches 0. Finally, the HotZone is a 3D stationary object that is meant to be placed on the ground.

## Reward Spawners

These objects have unique functionalities and characteristics and their primary function is to spawn rewards in the environment. They are immoveable (once they are spawned, they can't be moved).

### SpawnerTree
- **Name**: `SpawnerTree`
- **Size**: Fixed (scalable in future versions)
- **Spawned Goal Size Range**: `0.2-3`
- **Color**: Spawner color not changeable; spawned goals color changeable
- **Functionality**: Spawns rewards at a fixed rate (can be set via a parameter) at a fixed location (the rewards spawn on top of the tree, simulating a tree with ripening rewards that then fall off the tree). Currently, only the positive reward is spawned (yellow rewards).

### SpawnerDispenserTall
- **Name**: `SpawnerDispenserTall`, formerly `SpawnerDispenser`
- **Size**: Fixed (scalable in future versions)
- **Spawned Goal Size Range**: `0.2-1`
- **Color**: Spawner and goals color changeable
- **Functionality**: Dispenses rewards at a fixed rate (can be set via a parameter) at a fixed location (the rewards spawn inside the container, at the top of the prefab). Currently, only the positive reward is spawned (yellow rewards). The object has a door that can be animated to open and closes respectively via the boolean. The rewards can be *stockpiled* inside the dispenser, gradually increasing the number of rewards contained inside the dispenser.

### SpawnerContainerShort
- **Name**: `SpawnerContainerShort`, formerly `SpawnerContainer`
- **Size**: Fixed (scalable in future versions)
- **Spawned Goal Size Range**: `0.2-1`
- **Color**: Spawner and goals color changeable
- **Functionality**: Spawns rewards at a fixed rate (can be set via a parameter) at a fixed location (the rewards spawn inside the container). Currently, only the positive reward is spawned (yellow rewards). The object has a door that can be animated to open and closes respectively via the boolean. 

### SpawnerButton
- **Name**: `SpawnerButton`
- **Size**: Fixed (scalable in future versions)
- **Spawned Goal Size Range**: `1`
- **Color**: Spawner color not changeable; spawned goals color changeable
- **Functionality**: Spawns a reward when the player/agent *interacts* with it by colliding with the phyisical object. The rewards can be set via a simple probability distribution between the three types of rewards (positive, negative, and neutral). The rewards are spawned at any location within the arena via a parameter. Lastly, the SpawnerButton can be interacted with multiple times to spawn multiple rewards (this can also be set via a parameter, where you have complete control over how many times a reward type spawns and it's spawn rate).

## Other/Unique Objects

These objects have specific and limited functionalities, with their primary function is to provide a unique experience for the player or specific cues for the agent.

### SignBoard
- **Name**: `SignBoard`, formerly `SignPosterboard`
- **Color**: Symbol color changeable; SignBoard color fixed
- **Symbol**: Specified using `symbolNames` parameter
- **Functionality**: The SignBoard is a 3D object that can be placed in the environment to provide a visual cue to the player/agent. The SignBoard has a fixed color (grey) and a symbol that can be changed via the `symbolNames` parameter. The SignBoard can be placed on the ground or on a wall.
