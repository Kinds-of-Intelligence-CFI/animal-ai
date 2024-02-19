# Getting Started

This document should be your introductory document to Animal-AI, which outlines the process of getting started with the project, in  recommended order of material exposure. It is essentially a spiderweb connecting the project with the various documentation and resources available.

#### Table of Contents

* [What is Animal-AI?](#what-is-animal-ai)
      - [What is the aim of the project?](#what-is-the-aim-of-the-project)
      - [What is the background of the project?](#what-is-the-background-of-the-project)
* [If you are a researcher](#if-you-are-a-researcher)
  + [Recommended Order of Exposure](#recommended-order-of-exposure)
* [If you are a contributor](#if-you-are-a-contributor)

  
# What is Animal-AI?

Animal-AI is a platform for training and testing AI agents and human participants on a variety of tasks that require a rich understanding of the environment. The platform is built upon the Unity game engine, with Ml-Agents Toolkit used for backend functionality for training, and is designed to be extensible and easy to use. The platform is being used to study cognitive capabilities across humans, animals and AI agents comparatively across a variety of tasks and experiments. 

The platform is designed to be used by both researchers and developers as an open-source project. If you are a researcher, you can use the platform to train and test your own AI agents on a variety of tasks, as well as use the same tasks as computer games to assess cognitive capablities in humans. If you are a developer, you can contribute to the platform by adding new tasks, environments, and features.

#### What is the aim of the project?

The aim of the project is to create a platform that enables researchers to study cognitive capabilities across humans, animals and AI agents using the same tasks. These tasks are designed to be cognitively informative and meaningful such that pattern of performance across tasks can be triangulated and brought together into a "cognitive profile". This approach enables direct comparison of the cognitive profile of different kinds of mind. For AI this translates to robust evaluation of underlying capabilities, facilitating preditability and capabilites-oriented development. For cognitive scientists this allows the direct exploration of theories of cognition as well as identifying key tasks useful in distinguisihing them.

**You can find the project Roadmap [here](/project/AAI-RoadMap.md).**

#### What is the background of the project?

The project originates from the Kinds of Intelligence (KOI) programme within the Leverhulme Centre for the Future of Intelligence (LCFI). It started as a collaboration between the Cambridge (Dr Lucy Cheke, Dr Marta Halina) and Imperial (Dr Matthew Crosby, Prof Murray Shanahan) branches of the centre, and continues as an open and collaborative venture across these institutions and more (e.g. Universitat Politècnica de València; Prof Jose Hernendez-Orallo).

Please check our website for more information on the team [here](https://sites.google.com/csah.cam.ac.uk/animalai/).

# If you are a researcher

We assume you have basic understanding and/or experience of Python programming and Artificial Intelligence paradigms (pariticularly Reinforcement Learning). Animal-AI enables researchers with little to no experience in game development to train and test their own AI agents on a variety of tasks. The platform is designed to be easy to use, and is built upon the Unity game engine. We provide a number of example tasks known as configuration files, which are the main way of interacting with the platform. These configuration files can be used to train and test your own AI agents, and can be easily modified to create new tasks. These configuratuion files are written in YAML, which is a human-readable data serialization language, meaning little to no programming experience is required to use the platform.

_You can start your journey in the recommended order of exposure below, which will facilitate a smooth introduction and understanding of the platform:_

### Recommended Order of Exposure

Assuming you haven't already, you can install the platform by following the detailed installation guide here:

* [Installation Guide](/docs/gettingStarted/Installation-Guide.md)
  
You are now ready to launch the platform and run your first configuration file. The next guide will show you how to do this from downloading the platform for your operating system to running your first configuration file:

* [Launching Animal-AI](/docs/gettingStarted/Launching-AAI.md)

An example of a configuration file can be found here where you can simply download/copy to your IDE of choice and run it:

* [Example Configuration File](/docs/configGuide/Example-YAML-File.yaml)
  
You may then proceed to an introduction on the Arena Environment and the Agent here:

* [Arena Environment Guide](/docs/gettingStarted/Arena-Environment-Guide.md)

Furthermore, a comprehensive guide on the available objects and their properties can be found here which will enhance ytou understanding of the Arena Environment and it's many objects:

* [Arena Objects Guide](/docs/Arena-Object-Definitions.md)

Once you are familiar with the Arena Environment and the objects you can use to populate your custom environments, you can proceed to the following guides which will guide you on creating your own configuration files:

If you would like a brief introduction to YAML, you can find it here (If you have experience or are familiar with YAML, bypass this step):

* [Background on YAML](/docs/Background-YAML.md)

You may then proceed to the guide on using YAML in Animal-AI, which is tailored to the platform:

* [YAML Configuration Guide](/docs/configGuide/YAML-Config-Syntax.md)

Keep in mind that this order is recommended and not mandatory to follow - you may skip or choose what you wish to learn or discover freely.

If you are interested in integrating Animal-AI with other AI libraries, you can find a guide on how to do so here:

* [Using Animal-AI w/ Stable-Baselines3 and Dreamerv3](/docs/integration/Integrate-AAI.md)

# If you are a contributor

We assume you have a good understanding of and/or experience with programming languages **chsarp** and **python**. A good level of knowledge/experience is required to contribute to the project in very technical terms, especially on the Unity game engine. Note that having good knowledge/experience in other aspects of development such as 3D prefab model design, animation, and other general game designing is also very welcome. However, having a computer science background is not a requirement, and we welcome contributions from all backgrounds. 

Before you start contributing to the project, you should first familiarize yourself with the project structure and the various components that make up the project. You can find a detailed guide on the project structure [here](/docs/Technical-Overview.md). This documentation will explain the various components of the project, and how they interact with each other. It will also explain how to set up the project for development, and how to run the project in the Unity editor.

Once you are familiar with the project structure, you can start contributing to the project in either or both codebases, located [here](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-unity) (Unity/csharp) and [here](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-python) (Python).

For a detailed guide on acceptable contributions, see the [Contributing Guide](/docs/Contributing-Guide.md).
