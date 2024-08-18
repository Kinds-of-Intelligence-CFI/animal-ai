# Changelog

This document records all notable changes to the Animal-AI project. It follows the [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) format and adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html). For an overview of the project's development, see the [Roadmap](/project/AAI-RoadMap.md).

## [4.1.0] - Upcoming

### Notes
This version introduces a breaking change for YAML configuration files. The syntax for defining arenas has been updated to be more user-friendly and intuitive but is not backward compatible with `v4.0.0`. Please refer to the documentation for more information.

### Added
- **New Game Objects**:
  - **Movable: `HollowBox`**: A hollow box that agents can move around the arena to create more complex environments and challenges.
  - **Movable: `DecoyGoal` and `DecoyGoalBounce`**: These objects can be used similarly to the `HollowBox` for added complexity.
- **New UI Element: `AAI Build Version`**: Displays the Animal-AI Build Version in the bottom-right corner of the UI for quick reference.

### Changed
- **YAML Syntax Changes**:
  - `"t"` parameter renamed to `"timeLimit"` for clarity.
  - `"pass_mark"` parameter renamed to `"passMark"` for consistency.
- **UI Text Elements**: Now use the same font style for coherency.

### Fixed
- Fixed a bug where the agent would sometimes get stuck near the SpawnerButton.
- Fixed incorrect game object tags in Unity.

---

## [4.0.0] - 2024-03-09
### Notes
- _This release is a major update that moves away from the experimental phase and introduces a stable version of the Animal-AI environment._
- _This release is also backward incompatible with the previous versions (i.e. `v3.1.4.exp`), and agents trained on the previous version may not work with this new version._

### Added
- New valanced objects: `DecayGoal` and `DecayGoalBounce`.
- **New Feature: `mergeArenas`**. Allows users to merge multiple arenas into one, enabling more complex environments. Merged arenas will be in the same scene, allowing seamless agent movement between them. See the documentation for an example YAML configuration file.

### Changed
- Updated to TMPro package for text rendering in Unity, for better performance and flexibility.
- Changed the layout of the UI to be more user-friendly and intuitive.
- Changed UI text colours to be more accessible and readable.

### Fixed
- Fixed object tag being incorrectly set for game object `RAMP` (from _IMMOVABLE_ to _RAMP_).

---

## [3.1.4.exp] - 2023-12-22
### Added
- Enhanced Unit Tests for Unity codebase.

### Fixed
- Fixed a bug where randomizeArenas was not cycling through all available arenas if set to true.
- Added measures to make sure if the randomizeArenas feature is set to true, the same arena is not selected twice in a row.

### Changed
- Improvements to the UI layout and design.

---

## [3.1.3] - 2023-09-30
### Added
- Arena randomization via `randomizeArenas` feature.
- More robust error-checking for arena ID's and cycling.
- Visual elements for reinforcing cues (colors, short GIFs).

### Changed
- Shortened end-of-episode notification durations to 2.5 seconds.
- Updated visual cues like colors and short GIFs for reinforcement for feature end-of-episode notifications (more user-friendly).
- Minor Unity script optimizations (Animal-AI runs smoother now with more FPS on average).

### Fixed
- Resolved rare SpawnerTree Clock desync issue.
- Fixed Multiple Arenas cycling issue (via enhanced error-checking).
- Rectified the invisibility of the SignBoard prefab (now visible and functional).

---

## [3.1.2.exp] - 2023-09-11

### Added
- "Camera and Reset Buttons" feature.

### Changed
- Updated End of Episode Notification to be more user-friendly and fun.
- Increased next episode spawn (if end-of-episode notifcation is set to true) delay before next episode from 2 to 5 seconds.
- Improved SpawnerButton for better handling of missing values.

### Fixed
- Hotfix for a bug affecting the SpawnerTree (where the SpawnerTree game object would have inconsistent behavior).
- Fixed bug with multiple GIFs playing when health is 0 (if end-of-episode notification is set to true).

---

## [3.1.1] - 2023-08-10
### Added
- "End of Episode Notification" feature.
- "SpawnerButton" feature
- Added additional "Interactive Button" feature parameters for customization.

### Fixed
- Bug (minor) affecting the SpawnerTree.
- Bug (minor) affecting the SpawnerButton parameters.

---

## [3.0.2] - 2023-04-03
### Added
- Unit tests on Unity csharp scripts.

### Changed
- Upgraded MLagents to 2.3.0-exp3 (MLagents python version 0.30.0).
- Upgraded Unity Engine Editor to 2021.3.21f1.
- Updated `README.md` with more added information.

### Fixed
- Fixed bug where objects had dark shadows during arena initialisation.


# --- Legacy Versions: ---

## [3.0.1] - 2022
### Added
- Agent Freezing Parameter.

---

## [3.0.0] - 2022
### Changed
- Enhanced agent handling (stop and acceleration).
- Added new objects, spawners, signs, goal types.
- Updated object graphics.
- Released Unity Environment.
- Upgraded to Mlagents 2.1.0-exp.1 (ml-agents python version 0.27.0).

### Fixed
- Minor bug fixes.

### Notes
- Agents trained on earlier versions may perform differently due to control and graphic changes.

---

## [2.2.3] - 2021
### Added
- Support for multiple arenas in a single YAML file.

---

## [2.2.2] - 2021
### Changed
- Introduced low-quality version for improved fps.

---

## [2.2.1] - 2021
### Fixed
- UI scaling issues.
- Cardbox objects spawning at incorrect sizes.
- Environment timeout issue.

### Changed
- Enhanced Death Zone shader for varying sizes.

---

## [2.2.0] - 2021
### Added
- Health-based system.
- Basic Gym Wrapper.
- Basic heuristic agent for benchmarking and testing.

### Fixed
- Environment reset bug during training.
- Added frameskip setting (DecisionPeriod) for environment instantiation.

---

## [2.1.1] - 2021
### Added
- RayCast Observations.

### Fixed
- Raycast length issue (less than diagonal arena length).

---

## [2.1] - 2019
### Added
- Raycast observations.
- Agent global position tracking.

### Changed
- Upgraded to ML-Agents release 2 (0.26.0).

---

## [2.0] - 2019
### Added
- Ported Unity Environment from ml-agents 0.15 to 2.0.
- Ported basic python scripts from ml-agents 0.15 to 2.0.
- Added basic documentation.
- Added basic training scripts.
- Added basic training configurations.

_end of changelog_