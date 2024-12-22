# Animal-AI Technical Guide

# TODO: Complete the technical guide for the Animal-AI environment.

# IMPORTANT! This is a work in progress. Please check back soon for updates.

This guide will walk you through the engineering aspects of the Animal-AI Environment. It provides an overview of the environment and its components. If you are intending on contributing, then this guide will be a good place to start.


#### Table of Contents

* [Running the Environment](#running-the-environment)
  + [Play Mode](#play-mode)
      - [Controls in Play Mode](#controls-in-play-mode)
  + [Train Mode](#train-mode)
* [Environment Overview](#environment-overview)
   - [Observations](#observations)
   - [Actions](#actions)
   - [Rewards](#rewards)
   - [Curriculum](#curriculum)
   - [Configuration Files](#configuration-files)
   - [Arena Files](#arena-files)
   - [Unity Editor](#unity-editor)
* [Training Agents](#training-agents)
   - [Baselines](#baselines)
   - [Training Scripts](#training-scripts)
   - [Training Observations](#training-observations)
   - [Training Rewards](#training-rewards)
   - [Training Curriculum](#training-curriculum)
   - [Training Arena Files](#training-arena-files)
   - [Training Configuration Files](#training-configuration-files)
* [Testing Agents](#testing-agents)
* [Contributing](#contributing)
* [Citation](#citation)
* [License](#license)

## Running the Environment

The Animal-AI Environment can be run in one of two modes: `Play` and `Train` . In `Play` mode, the environment is run with a human player controlling the agent. In `Train` mode, the environment is run with an AI agent (see [Training Agents](#training-agents)). 

### Play Mode

To run the environment in `Play` mode, simply run the Animal-AI application for your OS, specifiying the configuration file location in full. This will launch the environment in play mode with the specified configuration file. The `play.py` command takes a single argument - the path to the configuration file to use. For example, to run the environment in `Play` mode using the `configs/curriculum/0.yaml` configuration file, use the following command:

```bash
animalai play configs/curriculum/0.yaml
```

#### Controls in Play Mode

In play mode, the player can control the agent using the keyboard. The following table lists the available controls:

| Keyboard Key | Action               |
| ------------ | -------------------- |
| W            | Move agent forwards  |
| S            | Move agent backwards |
| A            | Turn agent left      |
| D            | Turn agent right     |
| C            | Switch camera view   |
| R            | Reset environment    |
| Q            | Quit application     |

Toggle the camera between first-person, third-person, and bird's eye view using the `C` key. The agent can be controlled using `W` , `A` , `S` , `D` (or the arrow keys). Hitting `R` or collecting certain rewards (green or red) will reset the arena. Note that the camera and agent controls are not available in `Train` mode, with only third-person perspective implemented currently (we plan to add multiple camera observations during training at some point). Furthermore, you can toggle on/off the ability to restrict the player's camera angles via the `canChangePerspective` parameter in the configuration file. If this is set to false, then the player will not be able to change the camera angle. In addition, you can toggle on/off the ability to reset the arena via the `canResetArena` parameter in the configuration file. If this is set to false, then the player will not be able to reset the arena manually. A new feature added is that users can now toggle on/off Lastly, if you have multiple arenas specified in youur configuration file, you can randomize via the `randomizeArenas` parameter. This is false by default.

### Train Mode

To run the environment in `Train` mode, use the `animalai train` command. This will launch the environment with an AI agent controlling the agent. The `animalai train` command takes a single argument, the path to the configuration file to use. 

## Environment Overview

Regardless on what mode you are using, the arena you specify in the configuration file will be loaded. The agent will be placed in the arena and the environment will run until the agent reaches the goal or the episode time limit is reached. The environment will then reset and the process will repeat. The order of the arenas in the configuration file will be used to determine the order in which the arenas are loaded. Take a look at the [Configuration Files](#configuration-files) section for more details on how to create your own configuration files.
