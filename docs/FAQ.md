# Frequently Asked Questions
We have compiled a list of frequently asked questions and troubleshooting tips for Animal-AI. 

### Table of Contents
- [Troubleshooting Installation Issues](#troubleshooting-installation-issues)
  - [Resolving Environment Permission Errors](#resolving-environment-permission-errors)
    - [For macOS and Linux Users](#for-macos-and-linux-users)
    - [For Windows Users](#for-windows-users)
  - [Addressing Environment Connection Timeouts](#addressing-environment-connection-timeouts)
  - [Communication Port Conflict](#communication-port-conflict)
  - [Mean Reward Displaying NaN](#mean-reward-displaying-nan)
  - [Developer Verification Error on macOS](#developer-verification-error-on-macos)

## Troubleshooting Installation Issues
If you encounter issues installing the Animal-AI environment, consider the following solutions:

### Resolving Environment Permission Errors

#### For macOS and Linux Users
If you encounter a permission error after importing a Unity environment without building it in the editor, you may need to adjust file permissions. 

**On macOS**, execute the following command in the terminal:
```sh
chmod -R 755 *.app
```

**For Linux**, use:
```sh
chmod -R 755 *.x86_64
```

#### For Windows Users
Windows users can refer to the [Microsoft Documentation](https://docs.microsoft.com/) for adjusting permissions.

### Addressing Environment Connection Timeouts
If launching the environment through `UnityEnvironment` leads to a timeout error stating, "UnityAgentsException: The Communicator was unable to connect," consider these potential causes and solutions:

- **No Agent in Scene:** Ensure that your scene contains an agent.
- **Firewall Issues on macOS:** The firewall might block communication. Add the environment binary to the exceptions list following [Apple's instructions](https://support.apple.com/).
- **Errors in Unity Environment:** Check the [Unity log files](https://docs.unity3d.com/Manual/LogFiles.html) for potential errors that might hinder communication.
- **Proxy Environment Variables:** If `HTTP_PROXY` and `HTTPS_PROXY` are set in your environment variables, remove or unset them and retry.
- **Running in a Headless Environment:** When using a server or remote setup, include `--no-graphics` in the `mlagents-learn` command, or set `no_graphics=True` in `RemoteRegistryEntry.make()` or the `UnityEnvironment` initializer. For visual observations, consider setting up `xvfb` or an equivalent service.

### Communication Port Conflict
If you encounter the error, "Couldn't launch new environment because communication port {} is still in use," change the worker number in your Python script:

```python
UnityEnvironment(file_name=filename, worker_id=X)
```

### Mean Reward Displaying NaN
Receiving a `Mean reward : nan` message during PPO model training indicates non-terminating episodes. To resolve this, set the `Max Steps` parameter for Agents in the Scene Inspector to a non-zero value. Alternatively, script custom episode-termination conditions by manually setting `done` conditions.

### Developer Verification Error on macOS
Users who downloaded the repository via GitHub on macOS 10.15 (Catalina) or later might encounter a developer verification error when playing scenes. Solutions include installing the package via the Unity Package Manager (the recommended approach detailed [here](https://docs.unity3d.com/Manual/upm-ui-install.html)), or manually verifying files as described in [Apple's support guide](https://support.apple.com/).
