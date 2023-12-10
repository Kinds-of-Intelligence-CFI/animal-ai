# Quick Start Guide

## Running the standalone arena

You can run the executable for your system directly. This will load a single arena with all the possible objects in AnimalAI randomly resized and positioned. The environment will load in `play` mode, meaning that you will be able to control the agent directly. Of course, this is a very messy environment to work with and only useful for initial exploration. See other tutorials for how to design and run configuration files and how to train agents.

In play mode you can toggle the camera between first person, third person and Bird's eye view using the `C` key on your keyboard. The agent can then be controlled using `W,A,S,D` on your keyboard. Hitting `R` or collecting certain rewards (green or red) will reset the arena.

| Keyboard Key  | Action    |
| --- | --- |
| W   | move agent forwards |
| S   | move agent backwards|
| A   | turn agent left     |
| D   | turn agent right    |
| C   | switch camera       |
| R   | reset environment   |

## Running and designing specific configurations

Once you are familiarized with the environment and its physics, you can start building and visualizing your own. Assuming you followed the [installation instruction](../README.md#requirements), go to the `examples/` folder and run `python play.py`. This loads a random configuration from the competition we ran in 2019.

The [configuration files](../configs/competition) folder contains all the configurations from the competition. In a configuration you can select (or randomise) objects, their size, location, rotation and color. For more details on the configuration options and syntax please read the relevant documentation:
 - The [configuration file documentation page](configFile.md) explains how to write the configuration files.
 - The [definitions of objects page](definitionsOfObjects.md) contains a detailed list of all the objects and their properties.
