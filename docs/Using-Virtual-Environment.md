# Using Virtual Environments for Animal-AI

#### Table of Contents

* [Introduction to Virtual Environments](#introduction-to-virtual-environments)
* [Benefits of Using a Virtual Environment](#benefits-of-using-a-virtual-environment)
* [Python Version Compatibility](#python-version-compatibility)
* [Setting Up Virtual Environments](#setting-up-virtual-environments)
  + [Common Steps](#common-steps)
  + [Mac OS X](#mac-os-x)
  + [Ubuntu](#ubuntu)
  + [Windows](#windows)
* [Introduction to Conda Environments](#introduction-to-conda-environments)
* [Setting Up Conda Environments](#setting-up-conda-environments)
  + [Installing Conda](#installing-conda)
  + [Creating a Conda Environment](#creating-a-conda-environment)
  + [Managing Packages](#managing-packages)
  + [Deactivating an Environment](#deactivating-an-environment)
* [Conclusion](#conclusion)

## Introduction to Virtual Environments

A _Virtual Environment_ in Python is a self-contained directory that includes a specific version of Python and various packages. This isolated environment helps in managing project dependencies effectively. For more details, visit the [Python venv documentation](https://docs.python.org/3/library/venv.html) and [Anaconda documentation](https://docs.anaconda.com/).

## Benefits of Using a Virtual Environment

Using a Virtual Environment offers several advantages:
1. Simplifies dependency management for individual projects.
2. Facilitates testing with different versions of libraries, ensuring code compatibility.
3. Prevents conflicts between different versions of libraries.
4. Allows for easy sharing of project requirements with collaborators.

## Python Version Compatibility

* This guide is compatible with Python version `3.9.9`.
* Using newer Python versions might lead to compatibility issues with some libraries.

## Setting Up Virtual Environments

### Common Steps

1. **Install Python 3.9.9**: Ensure this version is installed on your system. If not, download it from [Python's official website](https://www.python.org/downloads/).
2. **Install Pip**:
   - Download Pip: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`

   - Install Pip: `python3 get-pip.py`

   - Verify installation: `pip3 -V`

   - **Ubuntu Note**: If you encounter a `ModuleNotFoundError` , install `python3-distutils` using `sudo apt-get install python3-distutils` .

### Mac OS X

1. Create a directory for environments: `mkdir ~/python-envs`.
2. Create a new environment: `python3 -m venv ~/python-envs/sample-env`.
3. Activate the environment: `source ~/python-envs/sample-env/bin/activate`.
4. Update Pip and setuptools:
   - `pip3 install --upgrade pip`

   - `pip3 install --upgrade setuptools` .
5. Deactivate with `deactivate` (reactivate using the same command).

### Ubuntu

1. Install the `python3-venv` package: `sudo apt-get install python3-venv`.
2. Follow the Mac OS X steps for environment creation and management.

### Windows

1. Create a directory for environments: `md python-envs` .
2. Create a new environment: `python -m venv python-envs\sample-env` .
3. Activate the environment: `python-envs\sample-env\Scriptsctivate` .
4. Update Pip: `pip install --upgrade pip` .
5. Deactivate with `deactivate` (reactivate using the same command).

**Additional Notes for Windows Users**:
* Confirm Python version: `python --version`.
* Admin privileges may be required for Python installation.
* This guide is specific to Windows 10 with a 64-bit architecture.

## Introduction to Conda Environments

_Anaconda_ (or simply Conda) is an open-source package management and environment management system that runs on Windows, macOS, and Linux. Conda environments are similar to Python virtual environments but they are managed with the Conda package manager.

## Setting Up Conda Environments

### Installing Conda

1. Download and install Anaconda or Miniconda from [Conda's official website](https://www.anaconda.com/distribution/).
2. Open a terminal (or Anaconda Prompt on Windows) and check the Conda version: `conda --version`.

### Creating a Conda Environment

1. Create a new environment: `conda create --name myenv` (replace `myenv` with your desired environment name).
2. Activate the environment: `conda activate myenv`.

### Managing Packages

* Install a package: `conda install numpy` (replace `numpy` with your desired package).
* Update a package: `conda update numpy`.
* List installed packages: `conda list`.

### Deactivating an Environment

* Deactivate with `conda deactivate`.

## Conclusion

Virtual Environments offer a robust solution for managing complex dependencies and are particularly useful for projects requiring a combination of Python and non-Python packages. This guide should help you get started with Conda or Python's Virtual Environments for using with Animal-AI.
