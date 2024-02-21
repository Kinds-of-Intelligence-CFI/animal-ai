# Background: YAML

#### Table of Contents

+ [YAML? What is it?](#yaml-what-is-it)
+ [Configuration of Training Environments and Agents](#configuration-of-training-environments-and-agents)
  + [Example of a YAML Configuration in Animal-AI](#example-of-a-yaml-configuration-in-animal-ai)
+ [Advantages in Animal-AI Context](#advantages-in-animal-ai-context)
  - [Easy to Read and Modify](#easy-to-read-and-modify)
  - [Facilitating Complex Configurations](#facilitating-complex-configurations)

## YAML? What is it?

*YAML* (YAML Ain't Markup Language) is a data serialization format widely used in Unity and other setups (as well as in ML-Agents) for its readability and ease of use. It allows developers and researchers to define and adjust the behavior and training parameters of AI agents within Unity simulations. Due to it's human-readable format, YAML is also useful for researchers who have little experience with programming. 

## Configuration of Training Environments and Agents

YAML files are used to configure training environments and agents in Animal-AI. These files are used to define the parameters of the training process, such as the neural network architecture, the reward signals, and the hyperparameters. They are also used to define the parameters of the agents, such as the observation types, the action spaces, and the reward signals. 

## Example of a YAML Configuration in Animal-AI

```yaml
!ArenaConfig
arenas:
  0: !Arena
    pass_mark: 0
    t: 500
    items:
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 2, y: 0, z: -1}
      rotations: [90]
    - !Item
      name: SpawnerButton
      positions:
      - !Vector3 {x: 20, y: 0, z: 20}
      moveDurations: [0.1]
      resetDurations: [1.0]
      rewardNames: ["GoodGoal", "BadGoal", "GoodGoalMulti"]
      rewardWeights: [1, 0, 0]
      spawnProbability: 1.0
      rewardSpawnPos: !Vector3 {x: 20, y: 0, z: 35}
```

The above example shows a YAML configuration file for an arena in Animal-AI. The `!ArenaConfig` tag indicates that the file is a configuration file for an arena. The `arenas` section defines the arenas in the environment. The `0` tag indicates that the arena is the first arena in the environment. The `pass_mark` parameter defines the minimum score required to pass the arena. The `t` parameter defines the maximum number of steps the agent can take in the arena. The `items` section defines the objects in the arena. The `name` parameter defines the name of the object. The `positions` parameter defines the positions of the object. The `rotations` parameter defines the rotations of the object. The `moveDurations` parameter defines the durations of the object's movements. The `resetDurations` parameter defines the durations of the object's resets. The `rewardNames` parameter defines the names of the object's rewards. The `rewardWeights` parameter defines the weights of the object's rewards. The `spawnProbability` parameter defines the probability of the object spawning. The `rewardSpawnPos` parameter defines the position of the object's reward.

## Advantages in Animal-AI Context

### Easy to Read and Modify

YAML's human-readable format makes it easier for developers and researchers to understand and modify the configurations of their Animal-AI environments. This is especially useful for researchers who have little experience with programming. 

### Facilitating Complex Configurations

The structure of YAML supports complex configurations with nested parameters, allowing for clear hierarchies and groupings of settings in Animal-AI. This makes it easier for developers to organize and modify their configurations. 

---
