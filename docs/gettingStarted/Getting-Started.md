# Getting Started

This document should be your introductory document to Animal-AI, which outlines the process of getting started with the project, in  recommended order of material exposure. It is essentially a spiderweb connecting the project with the various documentation and resources available.


#### Table of Contents

- [What is Animal-AI?](#what-is-animal-ai)
      - [What is the aim of the project?](#what-is-the-aim-of-the-project)
      - [What is the background of the project?](#what-is-the-background-of-the-project)
- [If you are a researcher](#if-you-are-a-researcher)


# What is Animal-AI?

Animal-AI is a platform for training and testing AI agents and human participants on a variety of tasks that require a rich understanding of the environment. The platform is built upon the Unity game engine, with Ml-Agents Toolkit used for backend functionality for training, and is designed to be extensible and easy to use. The platform is being used to study the development of intelligence in animals and AI agents comparatively in a variety of tasks and experiments. Our hypothesis is that current AI agents are not as intelligent as animals, with agents performing poorly on even some of the most basic tasks that animals can perform with ease.

The platform is designed to be used by both researchers and developers as an open-source project. If you are a researcher, you can use the platform to train and test your own AI agents on a variety of tasks, as well as perform sophisticated experiments designed for human interaction. If you are a developer, you can contribute to the platform by adding new tasks, environments, and features.

#### What is the aim of the project?

The aim of the project is to create a platform that enables researchers to train and test their own AI agents on a variety of tasks that require a rich understanding of the environment. The platform is designed to be extensible and easy to use, and is built upon the Unity game engine. The platform is currently in development, and is being used to study the development of intelligence in animals.

**You can find the project Roadmap [here](/project/AAI-RoadMap.md).**

#### What is the background of the project?

The project is a collaboration between the University of Cambridge researchers, and is funded by the Leverhulme Trust. The project is led by Dr. Lucy Cheeke (University of Cambridge) and Marta Halina (University of Cambridge), and formerly by Matthew Crosby (Imperial College London). Please check our website for more information on the team [here](https://sites.google.com/csah.cam.ac.uk/animalai/).

# If you are a researcher

We assume you have basic understanding and/or experience of Python programming and Artificial Intelligence paradigms (pariticularly Reinforcement Learning). Animal-AI enables researchers with little to no experience in game development to train and test their own AI agents on a variety of tasks. The platform is designed to be easy to use, and is built upon the Unity game engine. We provide a number of example tasks known as configuration files, which are the main way of interacting with the platform. These configuration files can be used to train and test your own AI agents, and can be easily modified to create new tasks. These configuratuion files are written in YAML, which is a human-readable data serialization language, meaning little to no programming experience is required to use the platform.

_You can start your journey in the recommended order of exposure below, which will facilitate a smooth introduction and understanding of the platform:_


--- 

Assuming you haven't already, you can install the platform by following the detailed installation guide here:
- [Installation Guide](/docs/gettingStarted/Installation-Guide.md) 
  
You may then proceed to an introduction on the Arena Environment and the Agent here:
- [Arena Environment Guide](/docs/gettingStarted/Arena-Environment-Guide.md)

Furthermore, a comprehensive guide on the available objects and their properties can be found here which will enhance ytou understanding of the Arena Environment and it's many objects:

- [Arena Objects Guide](/docs/Arena-Object-Definitions.md)

Once you are familiar with the Arena Environment and the objects you can use to populate your custom environments, you can proceed to the following guides which will guide you on creating your own configuration files:

If you would like a brief introduction to YAML, you can find it here (If you have experience or are familiar with YAML, bypass this step):
- [Background on YAML](/docs/Background-YAML.md)


You may then proceed to the guide on using YAML in Animal-AI, which is tailored to the platform:
- [YAML Congifuration Guide](/docs/configGuide/YAML-Config-Syntax.md)


You are now ready to launch the platform and run your first configuration file. The next guide will show you how to do this from downloading the platform for your operating system to running your first configuration file:

- [Launching Animal-AI](/docs/gettingStarted/Launching-Animal-AI.md)

An example of a configuration file can be found here where you can simply download/copy:

- [Example Configuration File](/docs/configGuide/Example-YAML-File.yaml)
