# Getting Started Guide

This guide should be your introduction to Animal-AI, which walks through the process of running Animal-AI in `Play` and `Training` modes, with detailed examples. In the near future, it will also cover how to train your own model using various wrappers such as Gym and Stable_Baselines 3. Please visit the Technical Guide [here](docs\Technical-Overview.md) for detailed information on the environment and how Animal-AI works behind-the-scenes.

For this guide, we'll use a few simple congifuration files of the environment, eac with a few variations such as the number of Arenas defined, the objects used, and ulitisation of advanced features such as arena randomisation and probabilistic spawning of rewards upon interaction with spawned gameobjects. If you'd like to find out more about the objects that can be used in the environment, please refer to the [Arena Objects Definitions](Objects.md) guide.

Finally, please note that Animal-AI is built upon _ML-Agents_ by Unity. For more information on ML-Agents, visit their GitHub repository [here](https://github.com/Unity-Technologies/ml-agents).

**Let's get started!**


## Understanding the Environment

An _Agent_ is an autonomous actor that observes and interacts with an _environment_. In the context of Unity, an environment is a scene containing one or more Agent objects, and, of course, the other entities that an agent interacts with.


**Note:** In Unity, the base object of everything in a scene is the
_GameObject_. The GameObject is essentially a container for everything else,
including behaviors, graphics, physics, etc. To see the components that make up
a GameObject, select the GameObject in the Scene window, and open the Inspector
window. The Inspector shows every component on a GameObject.

The first thing you may notice after opening the 3D Balance Ball scene is that
it contains not one, but several agent cubes. Each agent cube in the scene is an
independent agent, but they all share the same Behavior. 3D Balance Ball does
this to speed up training since all twelve agents contribute to training in
parallel.

### Agent

The Agent is the actor that observes and takes actions in the environment. In
the 3D Balance Ball environment, the Agent components are placed on the twelve
"Agent" GameObjects. The base Agent object has a few properties that affect its
behavior:

- **Behavior Parameters** — Every Agent must have a Behavior. The Behavior
  determines how an Agent makes decisions.
- **Max Step** — Defines how many simulation steps can occur before the Agent's
  episode ends. In 3D Balance Ball, an Agent restarts after 5000 steps.

#### Behavior Parameters : Vector Observation Space

Before making a decision, an agent collects its observation about its state in
the world. The vector observation is a vector of floating point numbers which
contain relevant information for the agent to make decisions.

The Behavior Parameters of the 3D Balance Ball example uses a `Space Size` of 8.
This means that the feature vector containing the Agent's observations contains
eight elements: the `x` and `z` components of the agent cube's rotation and the
`x`, `y`, and `z` components of the ball's relative position and velocity.

#### Behavior Parameters : Actions

An Agent is given instructions in the form of actions.
ML-Agents Toolkit classifies actions into two types: continuous and discrete.
The 3D Balance Ball example is programmed to use continuous actions, which
are a vector of floating-point numbers that can vary continuously. More specifically,
it uses a `Space Size` of 2 to control the amount of `x` and `z` rotations to apply to
itself to keep the ball balanced on its head.

