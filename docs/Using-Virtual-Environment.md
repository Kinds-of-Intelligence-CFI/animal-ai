# Guide to Using Virtual Environments in Python

## Introduction to Virtual Environments
A _Virtual Environment_ in Python is a self-contained directory that includes a specific version of Python and various packages. This isolated environment helps in managing project dependencies effectively. For more details, visit the [Python venv documentation](https://docs.python.org/3/library/venv.html).

## Benefits of Using a Virtual Environment
Using a Virtual Environment offers several advantages:
1. Simplifies dependency management for individual projects.
2. Facilitates testing with different versions of libraries, ensuring code compatibility.
3. Prevents conflicts between different versions of libraries.
4. Allows for easy sharing of project requirements with collaborators.

## Python Version Compatibility
- This guide is compatible with Python 3.9.9.
- Using newer Python versions might lead to compatibility issues with some libraries.

## Setting Up Virtual Environments

### Common Steps
1. **Install Python 3.9.12**: Ensure this version is installed on your system. If not, download it from [Python's official website](https://www.python.org/downloads/).
2. **Install Pip**:
   - Download Pip: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
   - Install Pip: `python3 get-pip.py`
   - Verify installation: `pip3 -V`
   - **Ubuntu Note**: If you encounter a `ModuleNotFoundError`, install `python3-distutils` using `sudo apt-get install python3-distutils`.

### Mac OS X
1. Create a directory for environments: `mkdir ~/python-envs`.
2. Create a new environment: `python3 -m venv ~/python-envs/sample-env`.
3. Activate the environment: `source ~/python-envs/sample-env/bin/activate`.
4. Update Pip and setuptools:
   - `pip3 install --upgrade pip`
   - `pip3 install --upgrade setuptools`.
5. Deactivate with `deactivate` (reactivate using the same command).

### Ubuntu
1. Install the `python3-venv` package: `sudo apt-get install python3-venv`.
2. Follow the Mac OS X steps for environment creation and management.

### Windows
1. Create a directory for environments: `md python-envs`.
2. Create a new environment: `python -m venv python-envs\sample-env`.
3. Activate the environment: `python-envs\sample-env\Scripts\activate`.
4. Update Pip: `pip install --upgrade pip`.
5. Deactivate with `deactivate` (reactivate using the same command).

**Additional Notes for Windows Users**:
- Confirm Python version: `python --version`.
- Admin privileges may be required for Python installation.
- This guide is specific to Windows 10 with a 64-bit architecture.

## Conclusion
Virtual Environments are essential for effective Python project management, especially when working with different versions and sets of dependencies. This guide should by now have helped you get started with creating and managing your own Virtual Environments, which you can use to run Animal-AI and other Python projects.

For any issues, please submit an issue or get in touch with one of the maintainers.
