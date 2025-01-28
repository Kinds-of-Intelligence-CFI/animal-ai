# Launching Animal-AI Guide

#### Table of Contents

1. [Introduction](#introduction)
2. [Getting Ready to Launch Animal-AI](#getting-ready-to-launch-animal-ai)
3. [Launching Animal-AI](#launching-animal-ai)
    - [Manual Play](#manual-play)
    - [Training Mode](#training-mode)
4. [Conclusion](#conclusion)

## Introduction

This guide explains how to launch the Animal-AI environment and run the simulation in either _training_ or _manual play_ mode. The steps are consistent across all platforms (Windows, Linux, and macOS), though specific commands may vary slightly.

## Getting Ready to Launch Animal-AI

1. **Download the Application**: 
   - Visit our [Releases page](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/releases) to download the appropriate version for your operating system (Windows, Linux, or macOS).
   - Extract the contents to a directory of your choice (e.g., `C:\Animal-AI` on Windows, `/home/username/Animal-AI` on Linux, or `/Users/username/Animal-AI` on macOS).

2. **Install the `animalai` Package**:
   - Create a virtual environment for your project if you haven't already. If you use Conda, activate your environment before proceeding.
   - Run the following command in your terminal:

     ```bash
     pip install animalai stable-baselines3
     ```

   - Note: `stable-baselines3` is required for training and helps avoid dependency issues.

3. **Prepare a Configuration File**:
   - The configuration file (YAML format) defines the settings for your Animal-AI environment, including arena and objects.
   - Create your own configuration file following our [guide on YAML syntax](/docs/configGuide/YAML-Config-Syntax.md), or download an [example file](/docs/configGuide/Example-YAML-File.yaml).
   - Save the configuration file in your chosen directory (e.g., `C:\Animal-AI` on Windows, `/home/username/Animal-AI` on Linux, or `/Users/username/Animal-AI` on macOS).

## Launching Animal-AI

To launch the Animal-AI environment, use Python scripts that specify both the configuration file and the path to the `AnimalAI.exe/app` file. Below, we'll demonstrate how to launch Animal-AI in both manual play and training modes using _Jupyter Notebook and Kernel Gateway_.

For simplicity and consistency, the same code examples apply to both modes.

### Manual Play

Copy and paste this code into a Jupyter Notebook. Save the file as `launch_animal_ai.ipynb` and run it. Ensure you have a kernel gateway set up; see our [Jupyter Notebook guide](/docs/Using-Jupyter-Notebooks.md) for instructions. You can also use the "Run All Cells" option to execute the code and install the kernel gateway quickly.

```python

# Import the necessary libraries
import sys
import random
import os

from animalai.environment import AnimalAIEnvironment
from mlagents_envs.exception import UnityCommunicationException

# IMPORTANT! Replace configuration file with the correct path here:
configuration_file = r"your-config-file.yml"

with open(configuration_file) as f:
    print(f.read()) 

# IMPORTANT! Replace the path to the application .exe here:
env_path = r'your-path-to-application.exe' 

port = 5005 + random.randint(
    0, 1000
)  # uses a random port to avoid problems with parallel runs

print("Initializing AAI environment")
try:
    environment = AnimalAIEnvironment(
        file_name=env_path,
        base_port=port,
        arenas_configurations=configuration_file,
        play=True,
    )

except UnityCommunicationException:
    # you'll end up here if you close the environment window directly
    # always try to close it from script (environment.close())
    environment.close()
    print("Environment was closed")
```

The most common mistake is not specifying the correct path to the application and/or the configuration file. Ensure you replace `your-config-file.yml` with the path to your configuration file and `your-path-to-application.exe` with the path to the AnimalAI.exe file.

After running the code, the Animal-AI environment will launch in manual play mode. You can now interact with the environment using the keyboard and mouse.

#### Controls in Play Mode

In play mode, you can switch the camera view and control the agent using the following keyboard commands (Q key only works on Play Mode):

| Keyboard Key  | Action               |
| ------------- | -------------------- |
| W             | Move agent forwards  |
| S             | Move agent backwards |
| A             | Turn agent left      |
| D             | Turn agent right     |
| C             | Switch camera view   |
| R             | Reset environment    |
| Q             | Quit application     |

Toggle the camera between first-person, third-person, and bird's eye view using the `C` key. Control the agent using `W`, `A`, `S`, `D`, or the arrow keys. Press `R` or collect certain rewards (green or red) to reset the arena or move to the next. If only one arena is defined in the configuration file, it will repeat indefinitely. Note that camera and agent controls are not available in `Train` mode, which currently supports only third-person camera (additional camera observations during training may be added in future updates).

### Training Mode

To launch the Animal-AI environment in training mode, save the following code as `launch_animal_ai_training.ipynb` and run it in your Jupyter Notebook. You can create code cells in the notebook by clicking the `+` button (assuming you're using an IDE such as Visual Studio Code) and selecting `Code`. Copy and paste the code below into the code cells and run them sequentially.

We will use Stable-Baselines3 to train the PPO agent in this example. Refer to the [Stable-Baselines3 documentation](https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html) for more information on using the PPO agent for training (`classstable_baselines3.common.policies.ActorCriticCnnPolicy`).

```python

# Import the necessary libraries
from stable_baselines3 import PPO
import matplotlib.pyplot as plt
from stable_baselines3.common.monitor import Monitor

import torch as th

import sys
import random
import pandas as pd
import os

from mlagents_envs.envs.unity_gym_env import UnityToGymWrapper
from animalai.environment import AnimalAIEnvironment
import subprocess

def train_agent_single_config(configuration_file, env_path , log_bool = False, aai_seed = 2023, watch = False, num_steps = 10000, num_eval = 100):
    
    port = 5005 + random.randint(
    0, 1000
    )  # uses a random port to avoid problems if a previous version exits slowly
    
    # Create the environment and wrap it...
    aai_env = AnimalAIEnvironment( # the environment object
        seed = aai_seed, # seed for the pseudo random generators
        file_name=env_path,
        arenas_configurations=configuration_file,
        play=False, # note that this is set to False for training
        base_port=port, # the port to use for communication between python and the Unity environment
        inference=watch, # set to True if you want to watch the agent play
        useCamera=True, # set to False if you don't want to use the camera (no visual observations)
        resolution=64,
        useRayCasts=False, # set to True if you want to use raycasts
        no_graphics=False, # set to True if you don't want to use the graphics ('headless' mode)
        timescale=1
    )

    env = UnityToGymWrapper(aai_env, uint8_visual=True, allow_multiple_obs=False, flatten_branched=True) # the wrapper for the environment
    
    runname = "optional_run_name" # the name of the run, used for logging

    policy_kwargs = dict(activation_fn=th.nn.ReLU) # the policy kwargs for the PPO agent, such as the activation function
    
    model = PPO("CnnPolicy", env, policy_kwargs=policy_kwargs, verbose=1, tensorboard_log="./tensorboardLogs") 
    # verbosity level: 0 for no output, 1 for info messages (such as device or wrappers used), 2 for debug messages
    
    for i in range(num_eval):
        model.learn(num_steps, reset_num_timesteps=False)
    env.close()

# IMPORTANT! Replace the path to the application and the configuration file with the correct paths here:
env_path = r"your-path-to-application.exe"
configuration_file = r"your-config-file.yml"

rewards = train_agent_single_config(configuration_file=configuration_file, env_path = env_path, watch = True, num_steps = 500, num_eval = 3000)
```

Here's a breakdown of what the above code does:

- **Import Libraries:** Imports necessary libraries, including the PPO algorithm from Stable-Baselines3.
- **Define Function:** Defines `train_agent_single_config` which takes the configuration file, path to AnimalAI.exe, and other parameters as inputs. This function:
  - Creates the Animal-AI environment and wraps it using `UnityToGymWrapper`.
  - Creates a PPO agent using Stable-Baselines3 and trains it for a specified number of steps.
- **Parameters:**
  - `log_bool`: Boolean to log the training process using TensorBoard.
  - `aai_seed`: Integer specifying the seed for the Animal-AI environment.
  - `watch`: Boolean to watch the agent play.
  - `num_steps`: Number of steps to train the agent.
  - `num_eval`: Number of evaluations to perform.
- **Call Function:** Calls `train_agent_single_config` with the configuration file and path to AnimalAI.exe.
- **Store Rewards:** Stores rewards obtained during training in the `rewards` variable.

**Note:** Replace `configuration_file` and `env_path` with the path to your configuration file and Animal-AI.exe/app file.

Running this code launches the Animal-AI environment in training mode. The agent is trained using the PPO algorithm and learns to navigate the environment and collect rewards based on the configuration file.

A `tensorboardLogs` folder will be created in the current working directory, where you can view training logs.

For new users, a guide on integrating Animal-AI with other AI libraries like Stable-Baselines3 and DreamerV3 is available [here](/docs/integration/Integrate-AAI.md).

## Conclusion

Congratulations! You've successfully launched the Animal-AI environment.

This guide has provided the necessary steps to launch the Animal-AI environment in both manual play and training modes. You can now interact with the environment using the keyboard and mouse in manual play mode or train an agent using the provided code in training mode. You can also use the provided code in your Python scripts to launch the Animal-AI environment. Please check our documentation for more information on the platform and how to use it.

If you encounter any issues or have any questions, please reach out to us on our [GitHub Discussions](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/discussions). You may also wish to check our [FAQs](/docs/FAQ.md) for answers to common questions.
