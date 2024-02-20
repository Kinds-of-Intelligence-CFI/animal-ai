# Launching Animal-AI

#### Table of Contents

1. [Introduction](#introduction)
2. [Launching Animal-AI](#launching-animal-ai)
3. [Running the Simulation](#running-the-simulation)
4. [Stopping the Simulation](#stopping-the-simulation)

## Introduction

This document provides instructions on how to launch the Animal-AI environment and run the Animal-AI simulation (application). This is a step=by-step guide to help you get running Animal-AI in either of the two modes: _training or manual play modes_.

Note that the steps are the same for all platforms (Windows, Linux, and macOS). However, the commands may differ slightly between platforms.

## Getting Ready to Launch Animal-AI

Before you can launch the Animal-AI environment, you need to download the application from our [Releases page](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/releases). You may choose to download the application for Windows, Linux, or macOS, depending on your operating system. After downloading, simply extract the contents of the downloaded file to a directory of your choice (e.g., `C:\Animal-AI` on Windows, `/home/username/Animal-AI` on Linux, or `/Users/username/Animal-AI` on macOS).

The next thing to do is to install the `animalai` package in your Python environment. You can do this by running the following command in your terminal (Command Prompt, Terminal, etc.). It's recommended to create a virtual environment for your project before installing the `animalai` package.

```bash
pip install animalai
```

After installing the `animalai` package, you need to create a configuration file for the Animal-AI environment. The configuration file is a YAML file that specifies the settings for the environment, such as the arena and the objects within it. You can create a configuration file by following the instructions in our [Creating a Configuration File](/docs/configGuide/YAML-Config-Syntax.md) guide or use our example configuration file as a starting point [here](/docs/configGuide/Example-YAML-File.yaml). Download this file and save it to a directory of your choice (e.g., `C:\Animal-AI` on Windows, `/home/username/Animal-AI` on Linux, or `/Users/username/Animal-AI` on macOS.

## Launching Animal-AI

You can use Python scripts to launch the Animal-AI environment by specifying the configuration file and the path to the AnimalAI.exe file. For simplicity and coherence sake, we will showcase how to launch via _Jupyter Notebook and Kernel Gateway_ for both manual play and training modesW. 

### Manual Play

Note that you need to have the `animalai` package installed in your Python environment to run the code below. 

Copy and paste this code into a Jupyter Notebook and run it to launch the Animal-AI environment. Save the file as `launch_animal_ai.ipynb` and run it in your Jupyter Notebook. Also, remember to create a kernel gateway in your Jupyter Notebook to run the code above. We have a guide on how to do that in our [Jupyter Notebook guide](/docs/Using-Jupyter-Notebooks.md).

```python

import sys
import random
import os

from animalai.environment import AnimalAIEnvironment
from mlagents_envs.exception import UnityCommunicationException

configuration_file = r"your-config-file.yml"

with open(configuration_file) as f:
    print(f.read()) 

env_path = r'your-path-to-application.exe' # where you extracted the application that you downloaded from our Releases page
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

Toggle the camera between first-person, third-person, and bird's eye view using the `C` key. The agent can be controlled using `W` , `A` , `S` , `D` (or the arrow keys). Hitting `R` or collecting certain rewards (green or red) will reset the arena. Note that the camera and agent controls are not available in `Train` mode, with only third-person perspective implemented currently (we plan to add multiple camera observations during training at some point).

### Training Mode

To launch the Animal-AI environment in training mode, follow these steps:

1. Open a terminal window (e.g., Command Prompt, Terminal, etc.).
