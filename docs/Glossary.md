# Animal-AI Glossary

#### Table of Contents

  1. [RL/ML-Agents Terms](#rlml-agents-terms)
  2. [Unity Terms](#unity-terms)
  3. [YAML Terms](#yaml-terms)

## RL/ML-Agents Terms

- **Academy**: A singleton object controlling the timing, reset, and training/inference settings of the environment.
- **Action**: The execution of a decision by an agent within the environment.
- **Agent**: A Unity Component that generates observations and takes actions in the environment, based on decisions from a Policy.
- **Decision**: The output of a Policy, specifying an action in response to an observation.
- **Editor**: The Unity Editor, encompassing various panes like Hierarchy, Scene, Inspector.
- **Environment**: The Unity scene containing Agents.
- **Experience**: A tuple [Agent observations, actions, rewards] representing a single Agent's data after a Step.
- **FixedUpdate**: A Unity method called at each step of the game engine, where ML-Agents logic is typically executed.
- **Frame**: An instance of rendering by the main camera, corresponding to each `Update` call in the game engine.
- **Observation**: Information available to an agent about the environment's state (e.g., Vector, Visual).
- **Policy**: The decision-making mechanism (often a neural network) that produces decisions from observations.
- **Reward**: A signal indicating the desirability of an agent’s action within the current environment state.
- **State**: The underlying properties of the environment and all agents within it at a given time.
- **Step**: An atomic change in the engine occurring between Agent decisions.
- **Trainer**: A Python class responsible for training a group of Agents.
- **Update**: A Unity function called at each frame rendering. ML-Agents logic is typically not executed here.

## Unity Terms

- **Unity Objects**: Fundamental components in the Unity Engine, serving as containers for all other components or functionalities within a Unity scene.
- **GameObjects**: Core elements in Unity, representing characters, props, scenery, cameras, lights, etc.
- **Prefabs**: Templates created from GameObjects in Unity, allowing for reuse and consistency across scenes or projects.
- **Immovable Objects**: Objects in the Animal-AI environment that are fixed in place and cannot be moved, like walls and ramps.
- **Movable Objects**: Objects that can be easily moved by the agent or other objects in the environment.
- **Rewards**: Objects providing positive or negative feedback to the agent, including stationary and moving goals.
- **Reward Spawners**: Objects with the primary function of spawning rewards in the environment.
- **Environment Permission Errors**: Issues related to file permissions when importing a Unity environment, particularly on macOS and Linux.
- **Environment Connection Timeouts**: Problems encountered when launching the Animal-AI environment through `UnityEnvironment`.
- **Communication Port Conflict**: Issues arising from port conflicts when initializing the Unity environment.
- **Mean Reward Displaying NaN**: A scenario where the mean reward metric shows 'nan', indicating an issue with the environment setup or configuration.

## YAML Terms

- **YAML File**: A file containing data in YAML format.
- **YAML Configuration File**: A YAML file containing configuration data for the Animal-AI environment.
- **YAML Configuration Name**: The name of a YAML configuration file, which is used to identify the configuration. Your custom configurations are used to create a new environment.
- **YAML Configuration Path**: The path to a YAML configuration file.