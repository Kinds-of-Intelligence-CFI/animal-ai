# Changelog

This document records all notable changes to the Animal-AI project. It follows the [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) format and adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html). For an overview of the project's development, see the [Roadmap](/project/AAI-RoadMap.md).

## Version 4.1.0 (upcoming)
### Notes
_A small breaking change is introduced in this version for YAML configuration files. The YAML syntax for defining arenas has been updated to be more user-friendly and intuitive. The new syntax is backward incompatible with the previous version `v4.0.0`. Please refer to the updated documentation for more information._

### Added
- _New Object: [Spawner] `Hollow-Object`._
  - This new object is a hollow box that can be configured to have a reward spawn right above it (by setting the y axis to anything above 1). The reward will be spawned at the same x and z position as the hollow object, so it is easy to configure the reward to spawn directly above the hollow object. The hollow object can be used to create more complex environments and challenges for the agent.
  - The new object has a few parameters specific to it, such as `rewardToSpawn` (string), `rewardSpawnPosition` (Vector3), `delayRewardSpawn` (bool), delayTime (float), and `rewardSpawnHeight` (float).
- _New UI Element: `AAI Build Version`._
  - Now, users will directly see the Animal-AI Build Version in the UI they are using for quick reference. It is displayed in the bottom-right corner of the UI.
- _New Functionality: `mergeArenas`._ 
  - This new functionality allows users to merge multiple arenas into one. This is useful for creating more complex environments with multiple arenas. The merged arenas will be placed in the same position in the scene, and the agent will be able to move between them seamlessly. An example YAML configuration file is provided in the documentation (see [here](docs/configGuide/Example-Merged-Arenas-YAML-File.yml)).

### Changed
- YAML syntax has major (breaking) changes: 
  - `"t"` parameter has been renamed to `"timeLimit"` to better reflect its purpose and improve readability.
  - `"pass_mark"` parameter has been renamed to `"passMark"` for coherency with other parameters.
  - UI text elements have been set to use the same font style for coherency.
- _New Object: [Spawner] `Hollow-Object`._
  - This new object is a hollow box that can be configured to have a reward spawn right above it (by setting the y axis to anything above 1). The reward will be spawned at the same x and z position as the hollow object, so it is easy to configure the reward to spawn directly above the hollow object. The hollow object can be used to create more complex environments and challenges for the agent.
  - The new object has a few parameters specific to it, such as `rewardToSpawn` (string), `rewardSpawnPosition` (Vector3), `delayRewardSpawn` (bool), delayTime (float), and `rewardSpawnHeight` (float).
- _New UI Element: `AAI Build Version`._
  - Now, users will directly see the Animal-AI Build Version in the UI they are using for quick reference. It is displayed in the bottom-right corner of the UI.
- _New Functionality: `mergeArenas`._ 
  - This new functionality allows users to merge multiple arenas into one. This is useful for creating more complex environments with multiple arenas. The merged arenas will be placed in the same position in the scene, and the agent will be able to move between them seamlessly. An example YAML configuration file is provided in the documentation (see [here](docs/configGuide/Example-Merged-Arenas-YAML-File.yml)).


### Fixed

---

## Version 4.0.0 (Released on 08.03.2024)
### Notes
- _This release is a major update that moves away from the experimental phase and introduces a stable version of the Animal-AI environment._
- _This release is backward incompatible with the previous version `v3.1.4.exp`, and agents trained on the previous version may work with this new version._

### Added
- New valanced objects: `DecayGoal` and `DecayGoalBounce`.
- New UI for presenting data to the user: Arena and Object statistics.
- New csharp Script: `UIManager.cs`, for managing the UI and displaying data about the current YAML configuration file arenas and total spawned objects.

### Changed
- Updated to TMPro for text rendering in Unity, for better performance and flexibility in the UI.
- Changed the layout of the UI to be more user-friendly and intuitive.
- Changed UI text colours to be more accessible and readable.

### Fixed
- Fixed object tag being incorrectly set for game object `RAMP` (from _IMMOVABLE_ to _RAMP_).

---

## Version 3.1.3 (Released on 30.09.2023)
### Added
- Arena randomization via the `randomizeArenas` parameter in YAML.
- More robust error-checking for arena ID's and cycling.
- Unit tests on `TrainingArena.cs` and `ArenaParameters.cs`.
- Visual elements for reinforcing cues (colors, short GIFs).

### Changed
- Shortened end-of-episode notification to 2.5 seconds.
- Minor Unity script optimizations.

### Fixed
- Resolved Spawner Tree Clock desync issue.
- Fixed Multiple Arenas cycling issue.
- Addressed Unity native warning in Training Arena script.
- Rectified the invisibility of the SignBoard prefab.

---

## Version 3.1.2.exp1 (Released on 11.09.2023)
### Fixed
- Hotfix for a bug affecting the Spawner Tree.

---

## Version 3.1.1 (Released on 10.08.2023)
### Added
- "End of Episode Notification" feature.
- Unofficial support for "Headless" mode in training (with Raycasting).
- Added additional "Interactive Button" feature parameters for customization.

### Fixed
- Bug affecting the Spawner Tree.
- Bug affecting the Interactive Button.

---

## Version 3.1.0
### Added
- "Interactive Button" feature.


---

## Version 3.0.2
### Changed
- Upgraded Mlagents to 2.3.0-exp3 (mlagents python version 0.30.0).

### Fixed
- Various bug fixes.

### Added
- Updated `README.md` with detailed instructions.
- Unit tests on `TrainingArena.cs` and `ArenaParameters.cs`.

---

## Version 3.0.1
### Added
- Agent Freezing Parameter.

---

## Version 3.0
### Changed
- Enhanced agent handling (stop and acceleration).
- Added new objects, spawners, signs, goal types.
- Updated object graphics.
- Released Unity Environment.
- Upgraded to Mlagents 2.1.0-exp.1 (ml-agents python version 0.27.0).

### Fixed
- Various bug fixes.

### Note
- Agents trained on earlier versions may perform differently due to control and graphic changes.

---

## Version 2.2.3
### Added
- Support for multiple arenas in a single YAML file.

---

## Version 2.2.2
### Changed
- Introduced low-quality version for improved fps.

---

## Version 2.2.1
### Fixed
- UI scaling issues.
- Cardbox objects spawning at incorrect sizes.
- Environment timeout issue.

### Changed
- Enhanced Death Zone shader for varying sizes.

---

## Version 2.2.0
### Added
- Health-based system.
- Basic Gym Wrapper.
- Basic heuristic agent for benchmarking and testing.

### Fixed
- Environment reset bug during training.
- Added frameskip setting (DecisionPeriod) for environment instantiation.

---

## Version 2.1.1 (Released on 01.07.2021)
### Added
- RayCast Observations.

### Fixed
- Raycast length issue (less than diagonal arena length).

---

## Version 2.1 (Beta Release 2019)
### Added
- Raycast observations.
- Agent global position tracking.

### Changed
- Upgraded to ML-Agents release 2 (0.26.0).

---

## Version 2.0 (Initial Port 2019)
### Added
- Ported Unity Environment from ml-agents 0.15 to 2.0.
- Ported basic python scripts from ml-agents 0.15 to 2.0.
- Added basic documentation.
- Added basic training scripts.
- Added basic training configurations.

--- _end of Changelog_ ---
