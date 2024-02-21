# Animal-AI RoadMap

#### Table of Contents

* [Project Overview](#overview)
* [Roadmap](#roadmap)


# Project Overview

We wish to enable the possibility of interdisciplinary research to better understand human, animal, and artificial cognition. We also want it to be a useful resource for making AI progress on these unsolved problems and also act as a way of tracking such progress so that we can stay on top of any AI breakthroughs that may have important societal implications.

# - - - Roadmap - - - 

## 2.1 Initial Port + RayCasts  [Major Release]

* [x] Port Unity Environment from ml-agents 0.15 to 2.0
* [x] Port basic python scripts from ml-agents 0.15 to 2.0
* [x] Add RayCast observations

The environment was ported to ml-agents 2.0. Raycast observations added and ensured to be roughly backwards compatible with 2.0.

## 2.2 Health and Basic Scripts  [Major Release]

* [x] Switched from reward system to health system (from DRL perspective functionally similar but unlocks more tasks and better integration with a continual learning setting)
* [x] Added decaying rewards
* [x] Improved Hotzone/Deathzone graphics and allow scaling
* [x] Added/improved python wrappers for all main usecases (play, openAIgym, lowlevelAPI, mlagents-learn)
* [x] Added heuristic agent for testing/debugging
* [x] Improved play mode overlay

Previous setting had an abstract system where food = +ve reward and time = -ve reward. This will be converted to decaying health that must be maintained by seeking our reward. Many tasks are functionally identical, but this setup is better for future tasks and also persistent survival. Other additions are improvements to the environment that go with this change and the initial setup of scripts as tutorials for using different training settings.

## 2.3 Experiment, Object, and Graphical Improvements  [Major Release]

* [x] Major graphics update to all items
* [x] Goals that decay/ripen/change size
* [x] More items for setting up experiments
* [x] Improved documentation

This update is focused on improving the environment for experimentation. This includes a major graphics update to all items, the addition of goals that decay/ripen/change size, and more items for setting up experiments. This update also includes improved documentation which enhances user experience.

## 3.3 Animal-AI 'Version 3' [Major Release]

* [x] Migrate to Unity Editor 2022
* [x] Migrate to ml-agents 0.30.0
* [x] Fix major graphical bugs affecting shadows and object placement
* [x] Add interactive objects to environment
    - [x] Add new objects to the environment that are interactable (SpawnerButton) by user and agents
* [x] Add more objects to the RayCast Parser (Unity and Python sides) 
* [x] Overhaul documentation and tutorials for the environment (play and training)

This update is focused on migrating to the latest version of Unity Editor and ml-agents. It also includes fixing major graphical bugs affecting shadows and object placement, adding interactive objects to the environment, and adding more objects to the RayCast Parser. This update also includes an overhaul of documentation and tutorials for the environment.

## 4.0 Animal-AI 'Version 4' [Major Release] [Stable 1.0]

* [x] Add 'decoy' valenced objects to the environment (no reward, but can be interacted with)
* [x] ...



---

_N.B: This roadmap is subject to change and is currently a work in progress._
