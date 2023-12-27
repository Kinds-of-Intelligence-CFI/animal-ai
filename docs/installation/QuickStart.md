# Quick Start Guide

## Table of Contents
1. [Running the Standalone Arena](#running-the-standalone-arena)
2. [Controls in Play Mode](#controls-in-play-mode)
3. [Running and Designing Specific Configurations](#running-and-designing-specific-configurations)
4. [Additional Resources](#additional-resources)

## Running the Standalone Arena

You can run the executable for your system directly. This will load a single arena with all the possible objects in AnimalAI randomly resized and positioned. The environment will load in `play` mode, meaning that you will be able to control the agent directly. This initial exploration environment is quite chaotic but serves as a good starting point. For more structured environments and agent training, refer to other tutorials.

## Controls in Play Mode

In play mode, you can switch the camera view and control the agent using the following keyboard commands:

| Keyboard Key  | Action               |
| ------------- | -------------------- |
| W             | Move agent forwards  |
| S             | Move agent backwards |
| A             | Turn agent left      |
| D             | Turn agent right     |
| C             | Switch camera view   |
| R             | Reset environment    |
| Q             | Quit application     |

Toggle the camera between first-person, third-person, and bird's eye view using the `C` key. The agent can be controlled using `W`, `A`, `S`, `D`. Hitting `R` or collecting certain rewards (green or red) will reset the arena.

## Running and Designing Specific Configurations

Once you are familiar with the environment, you can start creating and visualizing your own configurations. Assuming you've followed the [installation instructions](../README.md#requirements), navigate to the `examples/` folder and run `python play.py`. This script loads a random configuration from the 2019 competition.

Explore the [configuration files](../configs/competition) folder for all competition configurations. Configuration files allow you to select or randomize objects, their size, location, rotation, and color. For more details:
 - Refer to the [configuration file documentation page](configFile.md) for writing configuration files.
 - Check the [definitions of objects page](definitionsOfObjects.md) for a detailed list of all objects and their properties.

---

