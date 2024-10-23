# Animal-AI RoadMap

#### Table of Contents

* [Project Overview](#project-overview)
* [Roadmap](#roadmap)

_Note: This roadmap is subject to change and is a work in progress._

## Project Overview

We aim to enable interdisciplinary research to better understand human, animal, and artificial cognition. Additionally, we want the project to be a valuable resource for advancing AI in these challenging areas and to track progress, allowing us to stay informed about AI breakthroughs with significant societal implications.

## Roadmap

### 2.1.0 Initial Port + RayCasts [Major Release]

* [x] Port Unity Environment from ml-agents 0.15 to 2.0
* [x] Port basic Python scripts from ml-agents 0.15 to 2.0
* [x] Add RayCast observations

The environment was ported to ml-agents 2.0. Raycast observations were added and ensured to be roughly backwards compatible with 2.0.

### 2.2.0 Health and Basic Scripts [Major Release]

* [x] Switch from reward system to health system (functionally similar from a DRL perspective but unlocks more tasks and better integration with a continual learning setting)
* [x] Add decaying rewards
* [x] Improve Hotzone/Deathzone graphics and allow scaling
* [x] Add/improve Python wrappers for all main use cases (play, OpenAI Gym, low-level API, mlagents-learn)
* [x] Add heuristic agent for testing/debugging
* [x] Improve play mode overlay

The previous setting had an abstract system where food = +ve reward and time = -ve reward. This was converted to decaying health that must be maintained by seeking out rewards. Many tasks are functionally identical, but this setup is better for future tasks and persistent survival. Other additions include improvements to the environment that go with this change and the initial setup of scripts as tutorials for using different training settings.

### 2.3.0 Experiment, Object, and Graphical Improvements [Major Release]

* [x] Major graphics update to all items
* [x] Goals that decay/ripen/change size
* [x] More items for setting up experiments
* [x] Improved documentation

This update focuses on improving the environment for experimentation. It includes a major graphics update to all items, the addition of goals that decay/ripen/change size, and more items for setting up experiments. This update also includes improved documentation which enhances user experience.

### 3.3.0 Animal-AI 'Version 3' [Major Release]

* [x] Migrate to Unity Editor 2022
* [x] Migrate to ml-agents 0.30.0
* [x] Fix major graphical bugs affecting shadows and object placement
* [x] Add interactive objects to the environment
    - [x] Add new objects to the environment that are interactable (SpawnerButton) by users and Agents
* [x] Add more objects to the RayCast Parser (Unity and Python sides)
* [x] Overhaul documentation and tutorials for the environment (play and training)

This update focuses on migrating to the latest version of Unity Editor and ml-agents. It also includes fixing major graphical bugs affecting shadows and object placement, adding interactive objects to the environment, and adding more objects to the RayCast Parser. This update also includes an overhaul of documentation and tutorials for the environment.

#### Attention: Animal-AI v4.0.0 and Beyond: Iterative Stabilization and Enhancement

_Starting from version 4.0.0, the focus of development will shift towards an iterative process aimed at creating a robust and stable version of Animal-AI. This phase will prioritize fixing all outstanding bugs and addressing existing limitations, with the goal of refining and enhancing the system’s overall stability. The culmination of these efforts will be the release of a stable and reliable version 5.0.0, which will serve as a solid foundation for future developments._

### 4.0.0 Animal-AI 'Version 4' [Major Release] [Stable 1.0]

* [x] Add 'decoy' valenced objects to the environment (no reward values, but can be interacted with like other regular valenced rewards)
* [x] UI overhaul with modern UI elements and components
* [x] Add new UI elements to present YAML configuration-specific information, such as the number of defined arenas and current arena index; total number of spawned objects
* [x] Implement project-specific testing framework
* [x] Add new feature to merge multiple arenas into one

### 4.1.0 Animal-AI [Major Release] [Stable 2.0]

* [x] Make yaml parameters more readable, coherent; informative ('t' and 'pass-Mark' renamed to 'timeLimit' and 'passMark', respectively)
* [x] Launch new feature to collect and log data on arena and Agent (LogToCSV)
* [x] Improve and expand testing framework with more coverage and tests
* [x] Add new game objects (DecoyGoal and HollowBox)
* [x] Improve performance and optimisation across c# codebase
* [x] Rework collision settings on some game objects (i.e. movable/UBlock) for better and more realistic physics

### 4.2.0 Animal-AI [Major Release]

* [x] Allow some game objects to have customisable colors via YAML configurations (colors parameter)
* [x] Add new game objects (BadGoalMulti)
* [x] Add new textures for Light/Heavy Block game objects
* [x] Expand Unity test coverage and improve testing framework

### 4.3.0 Animal-AI [Major Release] [Stable 3.0]

* [ ] Upgrade ML-Agents to 3.0.0
* [ ] Upgrade Unity Editor to at least 2023.x.
* [ ] WebGL version of Animal-AI, hosted on AWS servers
* [ ] Implement Docker container for Animal-AI e2e testing

### 4.4.0 Animal-AI [Major Release] [Stable 4.0]

* [ ] Overhaul Agent settings and dynamics for better performance and adaptability
* [ ] Enable customization of arena dimensions (x and z axes) through YAML configurations (global or local parameter)
* [ ] Fix training mode bug where first episodes are skipped during first batch of arenas

### 4.5.0 Animal-AI [Major Release] [Stable 5.0]

### 5.0.0 Animal-AI [Major Release]