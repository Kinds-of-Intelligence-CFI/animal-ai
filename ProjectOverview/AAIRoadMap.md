# AnimalAI RoadMap to 3.0 (last updated 23/08/2021)

A (tentative) roadmap for AnimalAI (AAI) to get from where it is now to a tool for supporting and tracking AI progress towards currently unsolved cognitive capabilities. We want AAI to support interdisciplinary research to help better understand human, animal, and artificial cognition. We also want it to be a useful resource for making AI progress on these unsolved problems and also act as a way of tracking such progress so that we can stay on top of any AI breakthroughs that may have important societal implications.

## 2.1 Initial Port + RayCasts (Released 01/07/2021)

- [x] Port Unity Environment from ml-agents 0.15 to 2.0
- [x] Port basic python scripts from ml-agents 0.15 to 2.0
- [x] Add RayCast observations

The environment was ported to ml-agents 2.0. Raycast observations added and ensured to be roughly backwards compatible with 2.0.

## 2.2 Health and Basic Scripts (Released 13/07/2021)

- [x] Switched from reward system to health system (from DRL perspective functionally similar but unlocks more tasks and better integration with a continual learning setting)
- [x] Added decaying rewards
- [x] Improved Hotzone/Deathzone graphics and allow scaling
- [x] Added/improved python wrappers for all main usecases (play, openAIgym, lowlevelAPI, mlagents-learn)
- [x] Added heuristic agent for testing/debugging
- [x] Improved play mode overlay

Previous setting had an abstract system where food = +ve reward and time = -ve reward. This will be converted to decaying health that must be maintained by seeking our reward. Many tasks are functionally identical, but this setup is better for future tasks and also persistent survival. Other additions are improvements to the environment that go with this change and the initial setup of scripts as tutorials for using different training settings.

## 2.3 Experiment, Object, and Graphical Improvements (In Progress)

- [x] Major graphics update to all items
- [x] Goals that decay/ripen/change size.
- [x] More items for setting up experiments
- [ ] Can set number of observation frames before agent can move
- [ ] Can change starting velocities of objects
- [ ] Better support for randomisation of starting values in config files
- [ ] Flag for 'test-only' where physics can be broken
- [ ] Test-only objects appearing/changing after given times
- [ ] Textures on objects
- [ ] Containers (with/without wheels)
- [ ] Adjustable arena size
- [ ] This release may also incorporate some of the changes originally scheduled for 2.5.

One of the golden rules of AAI2 was that it should never be possible to break physics just for the sake of setting up an experiment. This was quite limiting for setting up psychology experiments that test for violation of expectations. We will add an extra flag for test environments to mark them as 'test-only' and support some methods for setting up these experiments. We will also add a number of features for improving the types of experiments that AAI can be used for.


## 2.4 Training, Debugging, and Testing Improvements

- [ ] Proper FPS testing - for analysis of the impact of new features and running multiple agents at once.
- [ ] Improved support for running multiple agents in the same environment (or in multiple envs if better).
- [ ] Implementations and documentation for running a number of different baselines.
- [ ] Automatic testing scripts for running a series of baseline agents on the existing (public & private) configs.
- [ ] Incorporation of testing and debugging inside the Unity Environment editory for easier further development. 
- [ ] Dockers to make the environment easier to use (if useful). 
- [ ] More options for the Gym Wrapper to use different types of observations (and multi-obs for SB3)

Most of the methods for training agents are directly using ml-agents implementations (for algorithms or wrappers). Yet, this may not be the most useful for many use-cases given the number of different ways it is possible to use the environment. This update will improve on the methods for analysing environment performance and also provide methods and tutorials for getting the most out of the environment. It will also include many internal changes that will improve future development and maintenence.

## 2.5 Behavioural Analysis

- [ ] Better format for storing experiment data for analysis.
- [ ] Automatic annotated task screenshots with agent trajectories.
- [ ] Ability to watch back agents easily regardless of interaction method.
- [ ] Automatically output an events log that details certain interactions that happened within a run.

For use as a proper comparison with Comparative Cognition and other animal cognition work, it is important to analyse agent (and human behaviour). We could do this with 2.0 to some extent, as [this paper](https://psyarxiv.com/me3xy) shows. The [web version](http://animalaiolympics.com/AAI/) allows for testing and playing back and directly comparing human and AI solutions. However, we currently do not utilise the wealth of extra analysis possibilities that working in a simulated environment allows for. This release plans to add some functionality in this direction.

## 2.6 Object Interactions

- [ ] Add the ability to pickup objects and interact with them in more ways than just bumping into them.

Not having any ways to interact with objects was a design choice to keep the environment as simple as possible whilst still allowing for a lot of tasks. However, a simple interaction mechanism would unlock a lot of currently impossible tasks without increasing the environment complexity too much.

## 2.7 WebGL Version

- [ ] Release updated version on [animalaiolympics.com](http://animalaiolympics.com/AAI/)
- [ ] Improve look and feel of AAI-as-game for human players.
- [ ] Add backend support for running psychology experiments.

A key part of AAI is the ability to compare humans, animals, and AI. The previous web-based setup was very useful for running human experiments. We plan to improve it for the new version.

## 2.8 Multiagent

- [ ] Add other agents to the environment that act independently.
- [ ] Support training multiple agents in same environment. 

Multiagent support is a very obvious area of cognitive intelligence that is currently missing from AAI. 

## 2.x

There are many other features/possibilities on the private ToDo list and in the possibility space that could be added depending on progress, interest, collaborations, and funding.

## 3.0 Bounties.

- [ ] Setup testing server where anyone can upload agents to run on private tests.
- [ ] Release bounties for particular hidden test sets that could be markers for progress in AI that is important from both a research and societal implications perspective. 

As we approach 3.0, we will transition from improving the capabilities of AnimalAI to improving its use as a public tool to support and track AI progress on currently missing components of general cognitive problem solving. 

