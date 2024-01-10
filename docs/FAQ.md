# Frequently Asked Questions
This document provides a comprehensive list of frequently asked questions and troubleshooting tips for the Animal-AI environment.

#### Table of Contents
1. [Troubleshooting Installation Issues](#1-troubleshooting-installation-issues)
   1. [Resolving Environment Permission Errors](#11-resolving-environment-permission-errors)
      1. [For macOS and Linux Users](#111-for-macos-and-linux-users)
      2. [For Windows Users](#112-for-windows-users)
   2. [Addressing Environment Connection Timeouts](#12-addressing-environment-connection-timeouts)
   3. [Communication Port Conflict](#13-communication-port-conflict)
   4. [Mean Reward Displaying NaN](#14-mean-reward-displaying-nan)
   5. [Developer Verification Error on macOS](#15-developer-verification-error-on-macos)

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
Timeout errors when launching through `UnityEnvironment`? Consider these fixes:

- **No Agent in Scene:** Ensure an agent is in the scene.
- **Firewall Issues on macOS:** Follow [Apple's instructions](https://support.apple.com/) to add exceptions.
- **Errors in Unity Environment:** Refer to [Unity log files](https://docs.unity3d.com/Manual/LogFiles.html).
- **Running in a Headless Environment:** Use `--no-graphics` or `no_graphics=True` if you intend on using this feature (not fully supported).

### 1.3 Communication Port Conflict
Encountering port conflicts? Try changing the worker number or port:

```python
UnityEnvironment(file_name=filename, worker_id=X)
```
Or find an available port dynamically:
```python
port = 5005 + random.randint(0, 1000)
```

### 1.4 Mean Reward Displaying NaN
Seeing `Mean reward : nan`? Set the `Max Steps` to a non-zero value or script custom termination conditions.