
# Detailed Arena Examples

Let's take a look at some examples to understand how to use the YAML syntax in Animal-AI to create custom arenas.

### EXAMPLE 1 - Standard Parameters & Randomisation
```
!ArenaConfig
arenas:
  0: !Arena
    t: 0
    items:
    - !Item
      name: Wall
      positions:
      - !Vector3 {x: 10, y: 0, z: 10}
      - !Vector3 {x: -1, y: 0, z: 30}
      colors:
      - !RGB {r: 204, g: 0, b: 204 }
      rotations: [45]
      sizes:
      - !Vector3 {x: -1, y: 5, z: -1}
    - !Item
      name: CylinderTunnel
      colors:
      - !RGB {r: 204, g: 0, b: 204 }
      - !RGB {r: 204, g: 0, b: 204 }
      - !RGB {r: 204, g: 0, b: 204 }
    - !Item
      name: GoodGoal
```
**Observations:** 
- The number of parameters for `positions`, `rotations`, and `sizes` do not need to match.
- The environment will spawn `max(len(positions), len(rotations), len(sizes))` objects.
- Missing parameters are assigned randomly.

In this scenario, the objects will spawn in the following order:

- A pink Cube will appear at coordinates [10, 10] on the ground. It will have a rotation of 45 degrees and its size will be random along the x and z axes, with a fixed size of y=5.
Another Cube will be placed on the ground at a random x coordinate and z=30. This cube's rotation, size, and color will all be randomly determined.
- Three CylinderTunnel objects will spawn next, and each of these will be entirely random in terms of position, size, color, and rotation.
- A GoodGoal object will then appear, with all its attributes randomized.
- Finally, the agent will spawn in a random position and orientation if it is unspecified in the arena instance. This is an important point to note, as if the agent was specified, it would have priority over all other objects and would be spawned first, before any other object(s).

&nbsp;

### EXAMPLE 2 - Decay Goals / Size-Changing Goals
```
!ArenaConfig
arenas:
  0: !Arena
    pass_mark: 0
    t: 250
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
      symbolNames:
      - "left-arrow"
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
**Observations:**

This example showcases various goals that undergo changes such as `decay`, `growth`, `shrinkage`, and `ripening` (anti-decay). Each Item in this setup includes certain parameters that are either irrelevant or used incorrectly. These 'red herring' parameters, while not utilized properly, do not impact the overall outcome or cause issues with the AAI environment.

In the above scenario:

- The `ShrinkGoal` and `GrowGoal` ignore the declared `sizes` parameter. Instead, their sizes change based on the initialValues and finalValues.
- For both `DecayGoal` and `AntiDecayGoal`, the size is determined by the larger of the `initialValue` or `finalValue`. 
- Additionally, the reward for these goals transitions from the initial value to the final value over time.
Interestingly, the ShrinkGoal includes a `symbolNames` parameter, which is typically reserved for `SignBoard` objects. This parameter is not applicable here and is therefore disregarded.
- Furthermore, an 'animal skin' feature is utilized in this example. Specifically, the Agent is configured to always appear with a 'hedgehog' skin.

<p align="center">
  <img width="700" src="ExampleGallery/decay-sizechange-goal-test.PNG">
</p>

After a few seconds, the changed goals will look as follows:

<p align="center">
  <img width="700" src="ExampleGallery/decay-sizechange-goal-test-changes.PNG">
</p>

&nbsp;

### EXAMPLE 3 - SignBoard (Preset Symbols)
```
!ArenaConfig
arenas:
  0: !Arena
    pass_mark: 0
    t: 250
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
      - "left-arrow"    
      - "letter-a"    
      - "circle"    
      - "u-turn-arrow"    
      - "tick"
```
**Observations:**

This example illustrates how to employ predefined symbols using the `symbolNames` parameter, which is exclusive to `SignBoard` objects. Each symbol in this list comes with a default color. However, these colors can be customized by specifying different values in the colors list. In this particular instance, the default colors for each symbol are retained without any modifications.

<p align="center">
  <img height="300" src="ExampleGallery/SignPosterboard-preset-symbols.PNG">
</p>

&nbsp;

### EXAMPLE 4 - SignBoard (Special Symbols)
```
!ArenaConfig
arenas:
  0: !Arena
    pass_mark: 0
    t: 250
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
**Observations:**

This example demonstrates the use of *special codes* to generate black-and-white pixel grids to use as symbols. `0` -> black, `1` -> white, and `*` is a 'joker' character that chooses to output black or white at random. The dimensions of the grid are given by the `/` character - each row between `/`s must be of the same size for the code to be valid.

Fully-random grids can be generated using the code `"MxN"`, where `M` and `N` are the grid width and height dimensions respectively. For example, `"5x3"` will generate a 5x3 grid.

For more information on how YAML works, please refer to the [YAML documentation](https://yaml.org/spec/1.2/spec.html).