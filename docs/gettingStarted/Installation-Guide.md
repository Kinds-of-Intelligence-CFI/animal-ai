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

Welcome to the comprehensive installation guide for Animal-AI. This guide is designed to help you install and set up Animal-AI smoothly, even if you're not familiar with Python dependencies, GitHub repositories, or Unity.

**For Windows Users:**
This guide is tailored for Windows, aiming to provide a straightforward installation process.

**For Mac and Linux Users:**
Most instructions for Windows should apply to you as well. For MacOS, you might need to run `chmod -R 777 AnimalAI.app` in your terminal to adjust permissions. Linux users may need to make the `.exe` file executable with `chmod +x env/AnimalAI.x86_64` and ensure files are moved to the parent folder after extraction.

## Steps:

### 1. Installing Python

* **Download Python**: Obtain Python 3.9.x from [Python's official website](https://www.python.org/downloads/).
**N.B. Python 3.10.x is the mininum version for AAI version 4.2.0 and above.**
* **Run the Installer**: Follow the installation prompts and ensure to **add Python to your PATH** (via the checkbox). For custom installations, keep the `install pip` box ticked.
* **Check Installation**: Open Command Prompt and run `python --version` to verify the version. It should be Python 3.9.x.
* **Check Pip**: Run `pip --version`. If pip is not installed, run `python -m ensurepip`. Pip is included by default in Python 3.4 and later.
* **Check PATH**: Run `echo %PATH%` to verify Python is added to your PATH. Instructions for manual addition can be found [here](https://datatofish.com/add-python-to-windows-path/).

### 2. Cloning the Animal-AI Repository (Optional)

This step is only needed if you want to contribute to Animal-AI. For users who just want to use the environment, you can skip to step 3.

* **Prepare a Directory**: Create a root folder for the AnimalAI project.
* **Clone the Repository**: Choose one of the following options:
  + Download the `.zip` file from [Animal-AI GitHub](https://github.com/Kinds-of-Intelligence-CFI/animal-ai) and extract it.
  + Use [GitHub Desktop](https://desktop.github.com/) for cloning.
  + Clone via the [GitHub CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).
* **Verify**: Ensure the root folder contains the `animal-ai` directory.

### 3. Setting Up a Virtual Environment (Optional)

* **Creating a Virtual Environment**: This helps manage dependencies.
  + **Python**: Use `python -m venv your_env_name` and activate it from the `Scripts` directory with `activate`.
  + **Conda**: Use `conda create --name your_env_name` and activate with `conda activate your_env_name`.

For more on virtual environments, see the [Python Documentation](https://docs.python.org/3/tutorial/venv.html) or [Conda Documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

### 4. Installing Dependencies

* **Navigate to the Repository**: Go to the `animal-ai` directory.
* **Install Dependencies**:
  + **Using pip**: Run `pip install animalai` to install necessary dependencies from PyPI.
  + **Using Conda**: Install pip with `conda install pip`, then run `pip install animalai`.
  + **Using a Virtual Environment**: Activate your environment, then run `pip install animalai`.
* **Check**: Run `pip list` to confirm `animalai` is installed. For a specific version, use `pip install animalai==x.x.x (e.g. 4.0.0)`.

### 5. Downloading the Animal-AI Environment

* **Download**: Get the appropriate version for your OS from the [Releases](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/releases) section.
* **Extract**: Unzip the downloaded file to your preferred location (Desktop recommended). Use tools like WinRAR or 7-Zip.
* **Verify**: Ensure the folder contains the `.exe` file for Windows, `.app` file for MacOS, and `.x86_64` file for Linux.

### 6. Starting Animal-AI

Launch the Animal-AI application from the directory where you extracted the files. Note that Animal-AI does not need to be installed on your system.

Refer to our [Launching AAI](/docs/gettingStarted/Launching-AAI.md) guide for detailed instructions on starting and using Animal-AI.

### General Notes

* **Folder Navigation**: Use `cd` to change directories. For example, `cd AAI` moves to the "AAI" folder. Use `cd..` to go up one directory level. For directory names with spaces, use quotes: `cd "AAI Folder"`. List contents with `dir` or `dir /b` for a basic listing.

* **Dependencies**: All necessary dependencies, including Unity's `ml-agents` package, are included in the Python package `animalai`. This is the only dependency needed. The package itself imports everything required.

### Troubleshooting

If you encounter issues, please contact ia424@cam.ac.uk or reach out on [GitHub](https://github.com/alhasacademy96/). For common issues and solutions, visit our [FAQ page](/docs/FAQ.md).

Happy experimenting with Animal-AI!