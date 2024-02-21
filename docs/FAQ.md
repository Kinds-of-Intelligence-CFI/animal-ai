# Frequently Asked Questions | Known Issues

Encountering issues with the Animal-AI environment? Here are some solutions to common problems:

#### Table of Contents

* [Troubleshooting Installation Issues](#1-troubleshooting-installation-issues)
  * [Resolving Environment Permission Errors](#11-resolving-environment-permission-errors)
    * [For macOS and Linux Users](#111-for-macos-and-linux-users)
    * [For Windows Users](#112-for-windows-users)
  * [Addressing Environment Connection Timeouts](#12-addressing-environment-connection-timeouts)
  * [Communication Port Conflict](#13-communication-port-conflict)
* [Mean Reward Displaying NaN](#2-mean-reward-displaying-nan)
* [Python API / Package Dependency Issues](#3-python-api--package-dependency-issues)
  * [No Module Named `animalai`](#31-no-module-named-animalai)
  * [Incompatible Python Version](#32-incompatible-python-version)
* [File Not Found Error](#4-file-not-found-error)
* [Unity Environment Not Found](#5-unity-environment-not-found)
* [Unity Environment Not Responding](#6-unity-environment-not-responding)
* [During Training, First Arena is Not Loaded](#7-during-training-first-arena-is-not-loaded)


## 1. Troubleshooting Installation Issues

Encountering issues while installing the Animal-AI environment? Here are some solutions to common problems:

### 1.1 Resolving Environment Permission Errors

#### 1.1.1 For macOS and Linux Users
Permission errors after importing a Unity environment? Adjust file permissions with these commands:

**macOS:**

```sh
chmod -R 755 *.app
```

**Linux:**

```sh
chmod -R 755 *.x86_64
```

#### 1.1.2 For Windows Users

Windows users generally don't need additional permissions. If needed, refer to [Microsoft Documentation](https://docs.microsoft.com/).

### 1.2 Addressing Environment Connection Timeouts

Timeout errors when launching through `UnityEnvironment` ? Consider these fixes:

* **No Agent in Scene:** Ensure an agent is in the scene.
* **Firewall Issues on macOS:** Follow [Apple's instructions](https://support.apple.com/) to add exceptions.
* **Errors in Unity Environment:** Refer to [Unity log files](https://docs.unity3d.com/Manual/LogFiles.html).
* **Running in a Headless Environment:** Use `--no-graphics` or `no_graphics=True` if you intend on using this feature (not fully supported).

### 1.3 Communication Port Conflict

Encountering port conflicts? Try changing the worker number or port:

```python
UnityEnvironment(file_name=filename, worker_id=X)
```

Or find an available port:

```python
port = 5005 + random.randint(0, 1000)
```

## 2. Mean Reward Displaying NaN

Seeing `Mean reward : nan` ? Set the `Max Steps` to a non-zero value or script custom termination conditions.

## 3. Python API / Package Dependency Issues

Encountering issues with the Python API or package dependencies? Here are some solutions to common problems:

### 3.1 No Module Named `animalai`

Seeing `ModuleNotFoundError: No module named 'animalai'` ? Ensure the `animalai` package is installed:

```sh
pip install animalai
```
or if you are using a virtual environment:

```sh
pip install animalai --user
```
or conda:
```sh 
conda install -c conda-forge animalai
```

Please do not forget to activate your environment before installing the package.

You can verify the installation by running:
```sh
python -c "import animalai"
```

### 3.2 Incompatible Python Version

Currently, the Animal-AI environment only supports **Python 3.6 to 3.9.** We have tested using 3.6, 3.7 and 3.8, but we cannot guarantee that it will work with these versions for everyone. If you are using a different version of Python, please install Python 3.9 for the optimal experience.

Please verify that you are using the correct version of Python by running:

```sh
python --version
```

## 4. File Not Found Error

Seeing `FileNotFoundError: [Errno 2] No such file or directory: 'AnimalAI/AnimalAI.app'`? Ensure the `AnimalAI` folder is in the same directory as your Python script.

If you are using macOS, you may get this error: `FileNotFoundError: [Errno 2] No such file or directory: 'env/AnimalAI'` . This error occurs when running the `python play.py` command from the `animal-ai/examples` folder. To fix this, simply rename the `MACOS.app` folder you downloaded to `Animal-AI`. This will allow the `play.py` script to find the environment. Note that this error is likely to occur in older versions of Animal-AI.

## 5. Unity Environment Not Found

Seeing `UnityEnvironmentException: Couldn't launch the Unity environment`? Ensure the `file_name` parameter is set to the correct path.

## 6. Unity Environment Not Responding

Seeing `UnityActionException: The Unity environment took too long to respond`? Ensure the `timeout_wait` parameter is set to a higher value. Alternatively, during training, try not to close the Unity environment window. This will prevent the environment from terminating the connection with the Python API, which will avoid a freeze or crash of the environment.

## 7. During Training, First Arena is Not Loaded

We are aware of this issue with the first arena (typically index 0) being skipped entirely during the initial training loop. However, this issue is resolved in the subsequent training loops. For a temporary fix, you can duplicate the first arena with the same parameters but change the index to 1. This will ensure that the first arena is loaded during the initial training loop in place of the first arena.

We are working on a fix for this issue. We apologize for any inconvenience this may cause.