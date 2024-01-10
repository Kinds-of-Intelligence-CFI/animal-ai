# Detailed Installation Guide

#### Table of Contents
1. [Introduction](#introduction)
2. [Steps](#steps)
    1. [Installing Python](#1-installing-python)
    2. [Cloning the Animal-AI Repository](#2-cloning-the-animal-ai-repository)
    3. [Setting Up a Virtual Environment (Optional)](#3-setting-up-a-virtual-environment-optional)
    4. [Installing Dependencies](#4-installing-dependencies)
    5. [Downloading the Animal-AI Environment](#5-downloading-the-animal-ai-environment)
    6. [Starting Animal-AI](#6-starting-animal-ai)
3. [Additional Resources](#additional-resources)
4. [General Notes](#general-notes)
5. [Troubleshooting](#troubleshooting)

## Introduction
Welcome to the comprehensive installation guide for Animal-AI. This guide is tailored for users who may not be familiar with Python dependencies, navigating GitHub repositories, or working with Unity. It's also here to help you smoothly navigate through any installation hiccups – because let's face it, *it's custom software installation... when **isn't** there a hiccup or two?*.

For **Windows** Users:
This guide is primarily written with Windows users in mind. We've tried to make it as straightforward as possible, so you can get started with Animal-AI without any hassle.

For **Mac** and **Linux** Users:
Similarly for Mac, most of the instructions for Windows users should still apply to you. If you are using MacOS, you may also need to run this command: `chmod -R 777 AnimalAI.app` in your MacOS terminal to unlock permissions for running the application.

If you're a Linux user, you're likely more comfortable with command-line interfaces and installations. The quick install guide in the README.md file should suffice for your needs. Please **note** that if you are using Linux, you may need to make the .exe file executable: Simply run this command in your terminal: `chmod +x env/AnimalAI.x86_64`. Please also make sure that when you extract the folder, you move the files inside the sub-directory to its parent folder.

## Steps:
### 1. Installing Python
- **Download Python**: Obtain Python 3.9.x from [Python's official website](https://www.python.org/downloads/).
- **Run the Installer**: Follow the installation instructions. Ensure to add Python to your PATH (via the checkbox). Note: if you're doing a custom intallation, it is recommended to keep the `install pip` box ticked and use `pip` to install dependencies. 
- **Check Installation**: Open a Command Prompt terminal and run `python --version`. You should see the version you installed. Make sure it's Python 3.9.x.

### 2. Cloning the Animal-AI Repository
- **Prepare a Directory**: Create a root folder for the AnimalAI project for better organization.
- **Clone the Repository**: Options include:
  - Downloading the `.zip` file from [Animal-AI GitHub](https://github.com/Kinds-of-Intelligence-CFI/animal-ai) and extracting it.
  - Using [GitHub Desktop](https://desktop.github.com/) for direct cloning.
  - Cloning via the [GitHub CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).

### 3. Setting Up a Virtual Environment (Optional)
- **Creating a Virtual Environment**: Useful for managing dependencies.
  - **Python**: Use `python -m venv your_env_name` and activate it in the `Scripts` directory with `activate`.
  - **Conda**: Use `conda create --name your_env_name` and activate with `conda activate your_env_name`.
For more information on virtual environments, refer to the [Python Documentation](https://docs.python.org/3/tutorial/venv.html) or [Conda Documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

### 4. Installing Dependencies
- **Navigate to the Repository**: Go to `animal-ai-main`.
- **Install Dependencies**: 
  - **Using pip**: Run `pip install animalai`. This will install the dependencies necessary to run Animal-AI, located in the `animalai` package from PyPI (Python Package Index).
  - **Using Conda**: Install pip (`conda install pip`), then run `pip install animalai`.

### 5. Downloading the Animal-AI Environment
- **Download**: Get the version for your OS from the `Releases` section in the repository.
- **Extract**: Unzip into the `env` folder in the main repository.
- **Check**: The `env` folder should contain the `.exe` file and other files from the `.zip` download.

### 6. Starting Animal-AI
- You can now start using Animal-AI. Contact the team for any issues you may encounter.
- **Note**: If you're using a virtual environment, make sure to activate it before running Animal-AI.

### Additional Resources
- [Quick Start Guide](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/blob/main/docs/quickStart.md) - for a quick overview of how to get started with Animal-AI, including running the standalone arena and learning controls for manual play.
- [Configuration Guide](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/blob/overhaul_docs/docs/configGuide/ConfigFileGuide.md) - for a detailed guide on how to design and run configuration files in Animal-AI.
- [Training Agents](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/blob/b596c6a8a9d36d2a504db7a06dc814d0a8b76c4a/docs/Training.md) - for a detailed guide on how to train agents in Animal-AI.


### General Notes
Folder navigation in Windows is performed using the `cd` command, e.g. if the current directory is shown as `:C\Users\Name` and you want to go to your new Animal-AI root folder called "AAI", you would type `cd AAI` and it will now show you are at `:C\Users\Name\AAI`. To go to the *parent* directory (e.g. in this case `:C\Users`), you would type `cd..` and if your directory name contains spaces, use speech marks e.g. `cd "AAI Folder"`. You can also use the `dir` command to list the contents of the current directory, and `dir /b` to list the contents without any additional information.

Everything you need to run scripts in Animal-AI (including the correct version of Unity's `ml-agents` package) is found in the Python Index Package `animalai`. This is installed using `pip` or `conda` as described above. The `animalai` package is a Python wrapper for the Unity environment, and is the only dependency you need to install. The `animalai` package is also the only dependency you need to import in your scripts, and it will import everything else you need from the `animalai` package itself.

### Troubleshooting
You can then start using Animal-AI! Any problems, please get in touch (ia424@cam.ac.uk / [alhasacademy96](https://github.com/alhasacademy96/) or post an issue on the GitHub repository.

