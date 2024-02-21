# Changelog

All notable changes to the Animal-AI project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

_Please also refer to the [Roadmap](/project/AAI-RoadMap.md) for a high-level overview of the project._

## [v4.0.0] - 05.03.2024

### Added

### Changed

### Fixed

--- 

## [v3.1.3] - 30.09.2023

### Fixed
* Resolved Spawner Tree Clock desync issue.
* Resolved Multiple Arenas improper cycling issue.
* Addressed Unity native warning in Training Arena script.
* Rectified the invisibility issue of the SignBoard  prefab.

### Added

* Enhanced arenas randomization via the `randomizeArenas` parameter in YAML.
* Added more robust error-checking for arena ID's and arena cycling.
* Conducted unit tests on `TrainingArena.cs` and `ArenaParameters.cs`.
* Added visual elements of paired reinforcing cues such as colours and short GIFs for better visual understanding for the user.

### Changed

* Shortened end-of-episode notification to *2.5 seconds*.
* Undertook minor Unity script optimizations.
* Updated the `README.md` file with more detailed instructions.

## [v3.1.2.exp1] - 11.09.2023

### Fixed
* Implemented hot fix for a newly discovered bug affecting the Spawner Tree.

## [v3.1.1] - 10.08.2023

### Added
* Introduced "End of Episode Notification" feature.
* Supported "Headless" mode unofficially for training agents (works with Raycasting).

### Fixed

* Fixed bug affecting the Spawner Tree.
* Fixed bug affecting the Interactive Button.

## [v3.1.0]

### Added
* Introduced "Interactive Button" feature.

## [v3.0.2]

### Changed
* Upgraded Mlagents to 2.3.0-exp3 (mlagents python version 0.30.0).

## [v3.0.1]

### Added
* Added Agent Freezing Parameter.

## [v3.0]

### Changed
* Updated agent handling for improved stop and acceleration.
* Added new objects, spawners, signs, goal types.
* Updated graphics for many objects.
* Made the Unity Environment available.
* Upgraded to Mlagents 2.1.0-exp.1 (ml-agents python version 0.27.0).

### Fixed

* Various bug fixes.

### Note

* Due to changes to controls and graphics, agents trained on previous versions might not perform the same.

## [v2.2.3]

### Added
* Ability to specify multiple different arenas in a single YAML config file.

## [v2.2.2]

### Changed
* Introduced a low-quality version with improved fps.

## [vv2.2.1]

### Fixed
* Improved UI scaling with respect to screen size.
* Fixed an issue with cardbox objects spawning at the wrong sizes.
* Fixed an issue where the environment would time out incorrectly.

### Changed

* Improved Death Zone shader for unusual Zone sizes.

## [v2.2.0]

### Added
* Switched to health-based system.
* Added basic Gym Wrapper.
* Added basic heuristic agent for benchmarking and testing.

### Fixed

* Fixed a reset environment bug during training.
* Added the ability to set the DecisionPeriod (frameskip) when instantiating an environment.

## [v2.1.1] - 01.07.2021

### Added
* RayCast Observations

### Fixed

* Fixed raycast length being less than diagonal length of standard arena.

## [v2.1] - Beta Release 2019

### Added
* Raycast observations.
* Agent global position to observations.

### Changed

* Upgraded to ML-Agents release 2 (0.26.0).

## [v2.0] - Initial Port 2019

### Added

* Ported Unity Environment from ml-agents 0.15 to 2.0.
* Ported basic python scripts from ml-agents 0.15 to 2.0.

* * *