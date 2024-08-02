# Animal-AI RoadMap

#### Table of Contents

* [Project Overview](#project-overview)
* [Roadmap](#roadmap)

_Note: This roadmap is subject to change and is a work in progress._

## Project Overview

We aim to enable interdisciplinary research to better understand human, animal, and artificial cognition. Additionally, we want the project to be a valuable resource for advancing AI in these challenging areas and to track progress, allowing us to stay informed about AI breakthroughs with significant societal implications.

## Roadmap

### 2.1 Initial Port + RayCasts [Major Release]

* [x] Port Unity Environment from ml-agents 0.15 to 2.0
* [x] Port basic Python scripts from ml-agents 0.15 to 2.0
* [x] Add RayCast observations

The environment was ported to ml-agents 2.0. Raycast observations were added and ensured to be roughly backwards compatible with 2.0.

### 2.2 Health and Basic Scripts [Major Release]

* [x] Switch from reward system to health system (functionally similar from a DRL perspective but unlocks more tasks and better integration with a continual learning setting)
* [x] Add decaying rewards
* [x] Improve Hotzone/Deathzone graphics and allow scaling
* [x] Add/improve Python wrappers for all main use cases (play, OpenAI Gym, low-level API, mlagents-learn)
* [x] Add heuristic agent for testing/debugging
* [x] Improve play mode overlay

The previous setting had an abstract system where food = +ve reward and time = -ve reward. This was converted to decaying health that must be maintained by seeking out rewards. Many tasks are functionally identical, but this setup is better for future tasks and persistent survival. Other additions include improvements to the environment that go with this change and the initial setup of scripts as tutorials for using different training settings.

### 2.3 Experiment, Object, and Graphical Improvements [Major Release]

* [x] Major graphics update to all items
* [x] Goals that decay/ripen/change size
* [x] More items for setting up experiments
* [x] Improved documentation

This update focuses on improving the environment for experimentation. It includes a major graphics update to all items, the addition of goals that decay/ripen/change size, and more items for setting up experiments. This update also includes improved documentation which enhances user experience.

### 3.3 Animal-AI 'Version 3' [Major Release]

* [x] Migrate to Unity Editor 2022
* [x] Migrate to ml-agents 0.30.0
* [x] Fix major graphical bugs affecting shadows and object placement
* [x] Add interactive objects to the environment
    - [x] Add new objects to the environment that are interactable (SpawnerButton) by users and agents
* [x] Add more objects to the RayCast Parser (Unity and Python sides)
* [x] Overhaul documentation and tutorials for the environment (play and training)

This update focuses on migrating to the latest version of Unity Editor and ml-agents. It also includes fixing major graphical bugs affecting shadows and object placement, adding interactive objects to the environment, and adding more objects to the RayCast Parser. This update also includes an overhaul of documentation and tutorials for the environment.

### 4.0 Animal-AI 'Version 4' [Major Release] [Stable 1.0]

* [x] Add 'decoy' valenced objects to the environment (no reward values, but can be interacted with like other regular valenced rewards)
* [x] UI overhaul with modern UI elements and components
* [x] Add new UI elements to present YAML configuration-specific information, such as the number of defined arenas and current arena index; total number of spawned objects
* [x] Implement project-specific testing framework
