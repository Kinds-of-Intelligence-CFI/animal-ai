### Table of Contents

- [YAML? What is it](#yaml-what-is-it)
- [Configuration of Training Environments and Agents in ML-Agents](#configuration-of-training-environments-and-agents-in-ml-agents)
  - [Defining Agent Behaviors in ML-Agents](#defining-agent-behaviors-in-ml-agents)
  - [Setting Hyperparameters for Training in ML-Agents](#setting-hyperparameters-for-training-in-ml-agents)
- [Example of a YAML Configuration in ML-Agents](#example-of-a-yaml-configuration-in-ml-agents)
- [Example of a YAML Configuration in Animal-AI](#example-of-a-yaml-configuration-in-animal-ai)
- [Advantages of Using YAML in Animal-AI Context](#advantages-of-using-yaml-in-animal-ai-context)
  - [Easy to Read and Modify](#easy-to-read-and-modify)
  - [Facilitating Complex Configurations](#facilitating-complex-configurations)


## YAML? What is it?

*YAML* (YAML Ain't Markup Language) is a data serialization format widely used in Unity and other setups (as well as in ML-Agents) for its readability and ease of use. It allows developers and researchers to define and adjust the behavior and training parameters of AI agents within Unity simulations. Due to it's human-readable format, YAML is also useful for researchers who have little experience with programming. 

## Configuration of Training Environments and Agents

YAML files are used to configure training environments and agents in ML-Agents. These files are used to define the parameters of the training process, such as the neural network architecture, the reward signals, and the hyperparameters. They are also used to define the parameters of the agents, such as the observation types, the action spaces, and the reward signals. 

### Defining Agent Behaviors

YAML files in ML-Agents are used to set up behavior parameters for agents, such as neural network models, observation types, actions, and reward signals. 

### Setting Hyperparameters for Training

These files are crucial for defining hyperparameters that guide the training process, like learning rate, batch size, and neural network configurations. 

## Example of a YAML Configuration in ML-Agents

```yaml
behaviors:
  SoccerPlayer:
    trainer_type: ppo
    hyperparameters:
      batch_size: 64
      buffer_size: 12000
      learning_rate: 0.0003
    network_settings:
      normalize: false
      hidden_units: 128
    reward_signals:
      extrinsic:
        gamma: 0.99
        strength: 1.0
    max_steps: 5e5
    time_horizon: 64
    summary_freq: 10000
```
The above example shows a YAML configuration file for a soccer player agent in ML-Agents. The agent's behavior is defined by the `SoccerPlayer` behavior name. The `trainer_type` parameter specifies the type of training algorithm used to train the agent. The `hyperparameters` section defines the hyperparameters for the training process. The `network_settings` section defines the neural network architecture for the agent. The `reward_signals` section defines the reward signals used to train the agent. The `max_steps` parameter defines the maximum number of steps the agent can take in the environment. The `time_horizon` parameter defines the number of steps the agent can take before the environment is reset. The `summary_freq` parameter defines the frequency at which the agent's training progress is logged. 

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
      name: Pillar-Button
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