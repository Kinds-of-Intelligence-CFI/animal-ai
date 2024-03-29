# Launching Animal-AI Guide

#### Table of Contents

1. [Introduction](#introduction)
2. [Getting Ready to Launch Animal-AI](#getting-ready-to-launch-animal-ai)
3. [Launching Animal-AI](#launching-animal-ai)
    - [Manual Play](#manual-play)
    - [Training Mode](#training-mode)
4. [Conclusion](#conclusion)

## Introduction

This document provides instructions on how to launch the Animal-AI environment and run the Animal-AI simulation (application). This is a step-by-step guide to help you get running Animal-AI in either of the two modes: _training or manual play modes_.

Note that the steps are the same for all platforms (Windows, Linux, and macOS). However, the commands may differ slightly between platforms.

## Getting Ready to Launch Animal-AI

As a reminder (or if you have not done so already) you need to download the application from our [Releases page](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/releases). You may choose to download the application for Windows, Linux, or macOS, depending on your operating system. After downloading, simply extract the contents of the downloaded file to a directory of your choice (e.g., `C:\Animal-AI` on Windows, `/home/username/Animal-AI` on Linux, or `/Users/username/Animal-AI` on macOS).

The next thing to do is to install the `animalai` package into your Python environment. You can do this by running the following command in your terminal (Command Prompt, Terminal, etc.). It's recommended to create a virtual environment for your project before installing the `animalai` package. If you already have a conda environment, you can activate it before install animalai package.

```bash
pip install animalai stable-baselines3 # we will need stable-baselines3 for training and it's good practice to install it now to avoid dependency issues which may arise later.
```

After installing the `animalai` package, you can use a configuration file for the Animal-AI environment. The configuration file is a YAML file that specifies the settings for the environment, such as the arena and the objects within it. You can create a configuration file by following the instructions in our [Creating a Configuration File](/docs/configGuide/YAML-Config-Syntax.md) guide or use our example configuration file as a starting point [here](/docs/configGuide/Example-YAML-File.yaml). Download this file and save it to a directory of your choice (e.g., `C:\Animal-AI` on Windows, `/home/username/Animal-AI` on Linux, or `/Users/username/Animal-AI` on macOS.)

## Launching Animal-AI

You can use Python scripts to launch the Animal-AI environment by specifying the configuration file and the path to the AnimalAI.exe file. For simplicity and coherence sake, we will showcase how to launch via _Jupyter Notebook and Kernel Gateway_ for both manual play and training modes below using the same code. 

### Manual Play

Note that you need to have the `animalai` package installed in your Python environment to run the code below (regardless of the mode you choose).

Copy and paste this code into a Jupyter Notebook and run it to launch the Animal-AI environment. Save the file as `launch_animal_ai.ipynb` and run it in your Jupyter Notebook. Also, remember to create a kernel gateway in your Jupyter Notebook to run the code below. We have a guide on how to do that in our [Jupyter Notebook guide](/docs/Using-Jupyter-Notebooks.md).

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

if environment:
    environment.close() # takes a few seconds to close...
```

The most common mistake is not specifying the correct path to the application and/or the configuration file. Make sure to replace `your-config-file.yml` with the path to your configuration file and `your-path-to-application.exe` with the path to the AnimalAI.exe file.

After running the code, the Animal-AI environment will launch in manual play mode. You can now interact with the environment using the keyboard and mouse.

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

Toggle the camera between first-person, third-person, and bird's eye view using the `C` key. The agent can be controlled using `W` , `A` , `S` , `D` (or the arrow keys). Hitting `R` or collecting certain rewards (green or red) will reset the arena (if there is only one defined arena in the configuration file, it will play the same arena infinitely). Note that the camera and agent controls are not available in `Train` mode, with only third-person camera implemented (we plan to add multiple camera observations during training at some point).

### Training Mode

For training mode, you can use the following code to launch the Animal-AI environment. Save the code below as `launch_animal_ai_training.ipynb` and run it in your Jupyter Notebook. In addition, you can create code junks to sequentially run bits of code by clicking on the `+` button in the Jupyter Notebook (assuming you're using an IDE such as Visual Studio Code) and selecting `Code`. Copy and paste the code below into the code junk and run it. 

Lastly, we will be using Stable-Baselines3 to train the PPO agent in this example. Refer to the [Stable-Baselines3 documentation](https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html) for more information on how to use the PPO agent for training (_class_: `classstable_baselines3.common.policies.ActorCriticCnnPolicy`).


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
So, what are we doing in the above code? 

- We first import the necessary libraries, including the PPO algorithm from Stable-Baselines3.

- We then define a function called `train_agent_single_config` that takes the configuration file, the path to the AnimalAI.exe file, and other parameters as input. The function creates the Animal-AI environment and wraps it using the `UnityToGymWrapper` class from the `mlagents_envs` package. We then create a PPO agent using the `PPO` class from Stable-Baselines3 and train the agent for a specified number of steps. 

- The other parameters are as follows:
    - `log_bool` - a boolean value that specifies whether to log the training process using TensorBoard.
    - `aai_seed` - an integer value that specifies the seed for the Animal-AI environment.
    - `watch` - a boolean value that specifies whether to watch the agent play.
    - `num_steps` - an integer value that specifies the number of steps to train the agent.
    - `num_eval` - an integer value that specifies the number of evaluations to perform.

- We then call the `train_agent_single_config` function with the configuration file and the path to the AnimalAI.exe file as input.

- Lastly, the rewards obtained during training are stored in the `rewards` variable.

**N.B:** The `configuration_file` and `env_path` variables should be replaced with the path to your configuration file and the Animal-AI.exe file, respectively, as in our previous example.

After running the code, the Animal-AI environment will launch in training mode. The agent will be trained using the PPO algorithm. Note that the controls in training mode are not available. The agent will learn to navigate the environment and collect rewards based on the configuration file you provided.

A folder named `tensorboardLogs` will be created in the current working directory (where you ran the code). You can view the training logs there directly.

If you are new to training agents in Animal-AI, we've provide a guide on how to integrate Animal-AI with other AI libraries such as Stable-Baselines3 and DreamerV3 [here](/docs/integration/Integrate-AAI.md).


## Conclusion

Congradulations! You've successfully launched the Animal-AI environment.

This guide hopefully has provided you with the necessary steps to launch the Animal-AI environment in both manual play and training modes. You can now interact with the environment using the keyboard and mouse in manual play mode or train an agent using the code provided in training mode. Of course, you can also use the code provided in your own Python scripts to launch the Animal-AI environment. Please check our documentation for more information on the platform and how to use it.

If you encounter any issues or have any questions, please feel free to reach out to us on our [GitHub Discussions](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/discussions). You may also wish to check our [FAQs](/docs/FAQ.md) for answers to common questions.
