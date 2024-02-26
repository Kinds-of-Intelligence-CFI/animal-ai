# Detailed Installation Guide

#### Table of Contents

* [Introduction](#introduction)
  + [Steps:](#steps)
    - [1. Installing Python](#1-installing-python)
    - [2. Cloning the Animal-AI Repository (Optional)](#2-cloning-the-animal-ai-repository-optional)
    - [3. Setting Up a Virtual Environment (Optional)](#3-setting-up-a-virtual-environment-optional)
    - [4. Installing Dependencies](#4-installing-dependencies)
    - [5. Downloading the Animal-AI Environment](#5-downloading-the-animal-ai-environment)
    - [6. Starting Animal-AI](#6-starting-animal-ai)
  + [General Notes](#general-notes)
  + [Troubleshooting](#troubleshooting)

## Introduction

Welcome to the comprehensive installation guide for Animal-AI. This guide is tailored for users who may not be familiar with Python dependencies, navigating GitHub repositories, or working with Unity. It's also here to help you smoothly navigate through any installation hiccups – because let's face it, *it's custom software installation... when **isn't** there a hiccup or two?*.

For **Windows** Users:
This guide is primarily written with Windows users in mind. We've tried to make it as straightforward as possible, so you can get started with Animal-AI without any hassle.

For **Mac** and **Linux** Users:
Similarly for Mac, most of the instructions for Windows users should still apply to you. If you are using MacOS, you may also need to run this command: `chmod -R 777 AnimalAI.app` in your MacOS terminal to unlock permissions for running the application.

If you're a Linux user, you're likely more comfortable with command-line interfaces and installations. Please **note** that if you are using Linux, you may need to make the .exe file executable: Simply run this command in your terminal: `chmod +x env/AnimalAI.x86_64` . Please also make sure that when you extract the folder, you move the files inside the sub-directory to its parent folder.

## Steps:

### 1. Installing Python

* **Download Python**: Obtain Python 3.9.x from [Python's official website](https://www.python.org/downloads/).
* **Run the Installer**: Follow the installation instructions. Ensure to **add Python to your PATH** (via the checkbox). Note: if you're doing a custom intallation, it is recommended to keep the `install pip` box ticked and use `pip` to install dependencies. 
* **Check Installation**: Open a Command Prompt terminal and run `python --version`. You should see the version you installed. Make sure it's Python 3.9.x.
* **Check Pip**: Run `pip --version` to see if pip is installed. If it's not, you can install it by running `python -m ensurepip` in the terminal. If you're using Python 3.4 or later, pip is included by default.
* **Check PATH**: Run `echo %PATH%` in the terminal to see if Python is added to your PATH. If it's not, you can add it manually by following the instructions [here](https://datatofish.com/add-python-to-windows-path/).

### 2. Cloning the Animal-AI Repository (Optional)

**Note**: This step is only necessary if you wish to contribute to Animal-AI. If you only want to use the environment, you can skip this step and go to step 3.
* **Prepare a Directory**: Create a root folder for the AnimalAI project for better organization.
* **Clone the Repository**: Options include:
  + Downloading the `.zip` file from [Animal-AI GitHub](https://github.com/Kinds-of-Intelligence-CFI/animal-ai) and extracting it.
  + Using [GitHub Desktop](https://desktop.github.com/) for direct cloning.
  + Cloning via the [GitHub CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).
* **Check**: The root folder should contain the `animal-ai` folder.

### 3. Setting Up a Virtual Environment (Optional)

* **Creating a Virtual Environment**: Useful for managing dependencies.
  + **Python**: Use `python -m venv your_env_name` and activate it in the `Scripts` directory with `activate`.
  + **Conda**: Use `conda create --name your_env_name` and activate with `conda activate your_env_name`.

For more information on virtual environments, refer to the [Python Documentation](https://docs.python.org/3/tutorial/venv.html) or [Conda Documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

### 4. Installing Dependencies

* **Navigate to the Repository**: Go to `animal-ai`.
* **Install Dependencies**: 
  + **Using pip**: Run `pip install animalai`. This will install the dependencies necessary to run Animal-AI, located in the `animalai` package from PyPI (Python Package Index).
  + **Using Conda**: Install pip (`conda install pip`), then run `pip install animalai`.
  + **Using a Virtual Environment**: Activate your virtual environment, then run `pip install animalai`.
* **Check**: Run `pip list` to see if `animalai` is installed. You should obtain the latest version of the package automatically. If you require an older version, you can specify it with `pip install animalai==x.x.x` where `x.x.x` is the version number.

### 5. Downloading the Animal-AI Environment

* **Download**: Get the version for your OS from the `Releases` section in the repository [here](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/releases).
* **Extract**: Unzip the downloaded folder into any destination of your choosing (we recommend to your Desktop). You can use WinRAR or 7-Zip to extract the files.
* **Check**: The folder should contain the `.exe` file for Windows,  `.app` file for MacOS, and the `.x86_64` file for Linux.

### 6. Starting Animal-AI

You can now start using Animal-AI by launching the application for your OS, located in the directory where you extracted the folder. _Note that Animal-AI does not need to be installed in your system to run._

Please see our [Launching AAI](/docs/gettingStarted/Launching-AAI.md) guide for a step-by-step guide on how to start using Animal-AI.

### General Notes

Folder navigation in Windows is performed using the `cd` command, e.g. if the current directory is shown as `:C\Users\Name` and you want to go to your new Animal-AI root folder called "AAI", you would type `cd AAI` and it will now show you are at `:C\Users\Name\AAI` . To go to the *parent* directory (e.g. in this case `:C\Users` ), you would type `cd..` and if your directory name contains spaces, use speech marks e.g. `cd "AAI Folder"` . You can also use the `dir` command to list the contents of the current directory, and `dir /b` to list the contents without any additional information.

Everything you need to run scripts in Animal-AI (including the correct version of Unity's `ml-agents` package) is found in the Python Index Package `animalai` . This is installed using `pip` or `conda` as described above. The `animalai` package is a Python wrapper for the Unity environment, and is the only dependency you need to install. The `animalai` package is also the only dependency you need to import in your scripts, and it will import everything else you need from the `animalai` package itself.

### Troubleshooting

You can then start using Animal-AI! Any problems, please get in touch (ia424@cam.ac.uk / [alhasacademy96](https://github.com/alhasacademy96/)) or post an issue on the GitHub repository.

Visit our FAQ page for more information on common issues and solutions [here](/docs/FAQ.md).
