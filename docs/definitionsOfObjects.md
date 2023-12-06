


## The Objects

There are 9 types of object split amongst four categories:
* Immovable
    * Walls
    * Ramps
    * Tunnels
* Movable
    * Cardboard Boxes
    * Shapes
* Rewards
    * Food
    * Zones
* Other/Unique
    * Spawners
    * Signs
    * Spawner Buttons

For each object we describe the object name to be used in a configuration file or in Python directly, as well as their default characteristics and the range of values you can assign to them. **All objects can be rotated `360` degrees.**

The axis below corresponds to that shown in the images for each individual object.

<img height="200" src="PrefabsPictures/Referential.png">

**Note:** the **Y axis** is the vertical axis and **Z** is the forward axis (following conventions used in Unity). 

## Immovable

These objects are fixed and cannot be moved:

#### Wall
<img align="right" height="100" src="PrefabsPictures/Immovable/Wall.png">

* name: `Wall`
* size range: `(0.1,0.1,0.1)-(40,10,40)`
* can change color. 

For simplicity, walls in most test problems will be grey and set to RGB (r: 153, g: 153, b: 153). If a wall is used as a platform it will be blue and set to RGB (r: 0, g: 0, b: 255).

#### Transparent Wall
<img align="right" height="100" src="PrefabsPictures/Immovable/WallTransparent.png">

* name: `WallTransparent`
* size range: `(0.1,0.1,0.1)-(40,10,40)`
* cannot change color

#### Ramp
<img align="right" height="100" src="PrefabsPictures/Immovable/Ramp.png">

* name: `Ramp`
* size range: `(0.5,0.1,0.5)-(40,10,40)`
* can change color. 

For simplicity, ramps in most test problems will be pink and set to RGB (r: 255, g: 0, b: 255).

#### Tunnel
<img align="right" height="100" src="PrefabsPictures/Immovable/CylinderTunnel.png">

* name: `CylinderTunnel`
* size range: `(2.5,2.5,2.5)-(10,10,10)`
* can change color

For simplicity, tunnels in most test problems will be grey and set to RGB (r: 153, g: 153, b: 153).

#### Transparent Tunnel
<img align="right" height="100" src="PrefabsPictures/Immovable/CylinderTunnelTransparent.png">

* name: `CylinderTunnelTransparent`
* size range: `(2.5,2.5,2.5)-(10,10,10)`
* cannot change color
    
## Movable

These are objects that are light enough to be easily moved by the agent (or other objects). Note that different object types weigh different amounts. Also note that since v0.6, all movable object have a fixed texture in order to make them easier to differentiate from non movable objects.     

#### Light Cardboard Box
<img align="right" height="100" src="PrefabsPictures/Movable/Cardbox1.png">

* name: `Cardbox1`
* size range: `(0.5,0.5,0.5)-(10,10,10)`
* cannot change color

#### Heavy Cardboard Box
<img align="right" height="100" src="PrefabsPictures/Movable/Cardbox2.png">

* name: `Cardbox2`
* size range: `(0.5,0.5,0.5)-(10,10,10)`
* cannot change color

#### U-shaped Object
<img align="right" height="100" src="PrefabsPictures/Movable/UObject.png">

* name: `UObject`
* size range: `(1,0.3,3)-(5,2,20)`
* cannot change color

#### L-shaped Object
<img align="right" height="100" src="PrefabsPictures/Movable/LObject.png">a L-shaped object with a wooden texture

* name: `LObject`
* size range: `(1,0.3,3)-(5,2,20)`
* cannot change color

#### L-shaped Object Variation
<img align="right" height="100" src="PrefabsPictures/Movable/LObject2.png">symmetric of the L-shaped object
 
* name: `LObject2`
* size range: `(1,0.3,3)-(5,2,20)`
* cannot change color
    
## Rewards

Objects that give a reward and may terminate the event if the agents collides with one. **Important note:** for sphere goals the `y` and `z` components of the provided sizes are ignored and only `x` is used.

#### Stationary Positive Goal
<img align="right" height="100" src="PrefabsPictures/Rewards/GoodGoal.png">
Green spheres with a positive reward equal to their size. Ends the episode on collection.

* name: `GoodGoal`
* size range: `0.5-5`
* cannot change color

#### Moving Positive Goal
<img align="right" height="100" src="PrefabsPictures/Rewards/GoodGoal.png">
Moving food with positive reward. Starts by moving in the direction provided by the rotation parameter.

* name: `GoodGoalBounce`
* size range: `0.5-5`
* cannot change color

#### Stationary Negative Goal
<img align="right" height="100" src="PrefabsPictures/Rewards/BadGoal.png">
Red spheres with a negative reward equal to their size. Ends the episode on collection.
       
* name: `BadGoal`
* size range: `0.5-5`
* cannot change color

#### Moving Negative Goal
<img align="right" height="100" src="PrefabsPictures/Rewards/BadGoal.png">
Moving food with negative reward. Starts by moving in the direction provided by the rotation parameter.

* name: `BadGoalBounce`
* size range: `0.5-5`
* cannot change color

#### Stationary Positive Reward
<img align="right" height="100" src="PrefabsPictures/Rewards/GoodGoalMulti.png">
Golden spheres with a positive reward equal to their size. Does **not** terminate the episode. The episode **is** terminated if all goals are collected. So, in an episode with only these rewards the episode will terminate when the last one is obtained.

* name: `GoodGoalMulti`
* size range: `0.5-5`
* cannot change color

#### Moving Positive Reward
<img align="right" height="100" src="PrefabsPictures/Rewards/GoodGoalMulti.png">
Moving food with positive reward (non-terminating). Starts by moving in the direction provided by the rotation parameter.
   
* name: `GoodGoalMultiBounce`
* size range: `0.5-5`
* cannot change color

#### DeathZone: 
<img align="right" height="100" src="PrefabsPictures/Rewards/DeathZone.png">
A red zone with reward -1 that terminates the episode on contact.

* name: `DeathZone`
* size range: `(1,0.5,1)-(40,10,40)`
* terminates an episode
* cannot change color

#### HotZone: 
<img align="right" height="100" src="PrefabsPictures/Rewards/HotZone.png">
An orange zone with reward `min(-10/T,-1e-5)` (or `-1e-5` if `T=0`) that **does not** end an episode.
        
* name: `HotZone`
* size range: `(1,0.5,1)-(40,10,40)`
* does not terminate an episode
* cannot change color
* if a `DeathZone` and a `HotZone` overlap the `DeathZone` prevails

#### Decay Goal: 
<img align="right" height="100" src="PrefabsPictures/Rewards/DecayGoal.png">
Variable-reward spheres whose reward 'decays' over time, following a (configurable) delay time. Colour changes (from purple to grey) and a radial-timer depletes over time during decay process. **Does not** end an episode except if all goals collected.

* name: `DecayGoal`
* initial/final reward value range: `0-5`
* size automatically sets to initial reward value
* fixed frame delay value range: `0-inf` (default is `150` frames)

#### Anti-Decay Goal: 
<img align="right" height="100" src="PrefabsPictures/Rewards/AntiDecayGoal.png">
Variable-reward spheres whose reward 'ripens' over time, following a (configurable) delay time. Colour changes (from grey to purple) and a radial-timer fills up over time during anti-decay process. **Does not** end an episode except if all goals collected.

* name: `AntiDecayGoal`
* initial/final reward value range: `0-5`
* size automatically sets to final reward value
* fixed frame delay value range: `0-inf` (default is `150` frames)

#### Grow Goal: 
<img align="right" height="100" src="PrefabsPictures/Rewards/GrowGoal.png">
Variable-reward spheres whose physical size grows over time, following a (configurable) delay time. Reward tracks size change. **Does not** end an episode except if all goals collected.

* name: `GrowGoal`
* initial/final reward value range: `0-5`
* reward increases along with size value
* fixed frame delay value range: `0-inf` (default is `0` frames)
* growth halts when `GrowGoal` is trapped between/underneath other objects

#### Shrink Goal: 
<img align="right" height="100" src="PrefabsPictures/Rewards/ShrinkGoal.png">
Variable-reward spheres whose physical size shrinks over time, following a (configurable) delay time. Reward tracks size change. **Does not** end an episode except if all goals collected.

* name: `ShrinkGoal`
* initial/final reward value range: `0-5`
* reward decreases along with size value
* fixed frame delay value range: `0-inf` (default is `0` frames)


## Other/Unique

Special objects with unique functionality. *Spawners* create and deposit new food into the arena, whilst *Signs* communicate visual information to the agent. These objects tend to have fixed dimensions (that may still be *scaled* by the `size` parameter).

#### Tree Spawner
<img align="right" height="110" src="PrefabsPictures/Other-Unique/SpawnerTree.PNG">
Tree that grows new food over time. Food objects spawn and grow in the tree branches, then fall to the ground after a configurable 'ripening' time.

* name: `SpawnerTree`
* fixed size: dimensions `5.19 x 5.95 x 5.02` *(may be scalable in future version)*
* spawned goal size range: `0.2-3`
* #spawns range: `0-inf` (leave blank or set to `-1` to spawn infinitely)
* cannot change color of spawner; can change color of spawned goals

#### Goal Dispenser
<img align="right" height="110" src="PrefabsPictures/Other-Unique/SpawnerDispenser.PNG">
Spawns new goal objects (finitely or otherwise) like a vending machine. After an optional, configurable time delay, the dispenser door can open and close at a regular specified interval. Food rolls out of the machine whenever the door is open.

* name: `SpawnerDispenser`
* fixed size: dimensions `1.67 x 4.46 x 1.67` *(may be scalable in future version)*
* spawned goal size range: `0.2-1`
* #spawns range: `0-inf` (leave blank or set to `-1` to spawn infinitely)
* can change color of spawner/goals

#### Goal Container
<img align="right" height="110" src="PrefabsPictures/Other-Unique/SpawnerContainer.PNG">
Spawns new goal objects (finitely or otherwise) in a small transparent container. After an optional, configurable time delay, the container door can open and close at a regular specified interval. Food stays within the container and can only be accessed by the agent when the door is open.

* name: `SpawnerContainer`
* fixed size: dimensions `1.67 x 1.67 x 1.67` *(may be scalable in future version)*
* spawned goal size range: `0.2-1`
* #spawns range: `0-inf` (leave blank or set to `-1` to spawn infinitely)
* can change color of spawner/goals

#### Sign Posterboard
<img align="right" height="90" src="PrefabsPictures/Other-Unique/SignPosterboard.PNG">
Posterboard communicating visual information to the agent. Features a 'symbol' that can be chosen from a list of presets, or generated as a matrix of pixels from a special code (see [configFile.md](configFile.md)).

* name: `SignPosterboard`
* size range: `0.5-2.5` (**note:** `x` is posterboard thickness, `y` is height, `z` is width - size values for posterboards are a *scale factor*, not the actual size)
* color change overrides the color of the *symbol*, not the posterboard itself - leave empty for the symbol's default color to be used
* symbol is specified using the `symbolNames` parameter
&nbsp;

#### Spawner Button

Pillar that spawns new goals into the enviroment. The probability with which different goals are spawned into the environment by the pillar can be defined by the user.

* name: `Pillar-Button`
* fixed size: dimensions `insert here` 
* spawned goal size range: `insert here`
* #spawns range: `0-inf` (leave blank or set to `-1` to spawn infinitely)
* moveDurations: A value which defines the delay period between the pillar button being activated and the reward object being spawned.
* resetDurations: A value which defines the delay between period betweeen the pillar button spawning a reward and when it is next able to spawn another.
* rewardNames: A list object which specifices the reward(s) that a pliiar button will spawn. For example, ["GoodGoal"] would only spawn green reward objects, whilst ["GoodGoal", "BadGoal", "GoodGoalMulti"] would spawn each of these three rewards with varuing probabilities. 
* rewardWeights: A list of values which specifices the likelihood with which each reward object is likely to be spawned by the pillar button. For example, [1, 0, 0] would always spawn a "GoodGoal" from the rewardNames example, whilst [0.5,0.5,0] whould spawn a "GoodGoal" or a "BadGoal" with equal probability. 
* spawnProbability: A value between `0.0-1.0` which defines the likelihood that the pillar button will spawn a reward on a given occassion
* rewardSpawnPos: The location that the reward objects will be spawned.
