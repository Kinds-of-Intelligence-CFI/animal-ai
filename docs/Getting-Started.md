# Animal-AI Detailed Overview

This guide will walk you through the process of running the Animal-AI Environment. It will also provide an overview of the environment and its components. If you have any questions or issues, please check the [FAQ](docs/FAQ.md) and documentation before posting an issue on GitHub. If you are unable to find an answer to your question, please post an issue on GitHub.

### Table of Contents

- [Installation](#installation)
- [Running the Environment](#running-the-environment)
  - [Play Mode](#play-mode)
      - [Controls in Play Mode](#controls-in-play-mode)
  - [Train Mode](#train-mode)
- [Environment Overview](#environment-overview)
   - [Observations](#observations)
   - [Actions](#actions)
   - [Rewards](#rewards)
   - [Curriculum](#curriculum)
   - [Configuration Files](#configuration-files)
   - [Arena Files](#arena-files)
   - [Unity Editor](#unity-editor)
- [Training Agents](#training-agents)
   - [Baselines](#baselines)
   - [Training Scripts](#training-scripts)
   - [Training Observations](#training-observations)
   - [Training Rewards](#training-rewards)
   - [Training Curriculum](#training-curriculum)
   - [Training Arena Files](#training-arena-files)
   - [Training Configuration Files](#training-configuration-files)
- [Testing Agents](#testing-agents)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)

## Installation

If you have not already done so, please follow the [installation instructions](docs\installation\InstallationGuide.md) to install the Animal-AI Environment before reading this guide. If you have done so and are ready to get started, please continue reading.



## Running the Environment

The Animal-AI Environment can be run in one of two modes: `Play` and `Train`. In `Play` mode, the environment is run with a human player controlling the agent. In `Train` mode, the environment is run with an AI agent controlling the agent. The environment can be run in either mode using the `animalai` command line tool and by launching the environment directly from the Unity Editor or application.

### Play Mode

To run the environment in `Play` mode, use the `animalai play` command. This will launch the environment with a human player controlling the agent. The `animalai play` command takes a single argument, the path to the configuration file to use. For example, to run the environment in `Play` mode using the `configs/curriculum/0.yaml` configuration file, use the following command:

```bash
animalai play configs/curriculum/0.yaml
```
#### Controls in Play Mode

In play mode, you can switch the camera view and control the agent using the following keyboard commands: 

| Keyboard Key  | Action               |
| ------------- | -------------------- |
| W             | Move agent forwards  |
| S             | Move agent backwards |
| A             | Turn agent left      |
| D             | Turn agent right     |
| C             | Switch camera view   |
| R             | Reset environment    |
| Q             | Quit application     |

Toggle the camera between first-person, third-person, and bird's eye view using the `C` key. The agent can be controlled using `W`, `A`, `S`, `D`. Hitting `R` or collecting certain rewards (green or red) will reset the arena. 

 

### Train Mode

To run the environment in `Train` mode, use the `animalai train` command. This will launch the environment with an AI agent controlling the agent. The `animalai train` command takes a single argument, the path to the configuration file to use. For example, to run the environment in `Train` mode using the `configs/curriculum/0.yaml` configuration file, use the following command:

```bash
animalai train configs/curriculum/0.yaml
```
