# Agents In Animal-AI

This directory provides some starting points for building a range of agents for interaction with the animal-ai environment. Note that some of the  scripts require additional packages to be installed to use - this should be obvious from the scripts. See the docs directory and the forthcoming Animal-AI Version 3 Paper for more description/explanation.

- `randomWalkers.py` provides an implementation for random walkers using the low-level API.
- `gotToGoodBraitenberg.py` shows off the ml-agents low level python api for interacting with the environment and demonstrates inference with a hand-coded *Braitenberg* agent that navigates towards good goals and away from bad goals.
- `PPOAgent.py` shows how to wrap animalai as a gym environment and train and test a PPO agent on a config.
