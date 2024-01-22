# Getting Started

This document should be your introductory document to Animal-AI, which outlines the process of getting started with the project, in  recommended order of material exposure. It is essentially a spiderweb connecting the project with the various documentation and resources available.

#### Table of Contents
- [What is Animal-AI?](#what-is-animal-ai)
      - [What is the aim of the project?](#what-is-the-aim-of-the-project)
      - [What is the background of the project?](#what-is-the-background-of-the-project)
- [If you are a researcher](#if-you-are-a-researcher)
  - [Recommended Order of Exposure](#recommended-order-of-exposure)
- [If you are a contributor](#if-you-are-a-contributor)
  - [Next Steps](#next-steps)
  - [Creating an Issue/Feature Request](#creating-an-issuefeature-request)
  - [Pre-Pull Request](#pre-pull-request)
  - [Creating a Pull Request](#creating-a-pull-request)
  - [Review and Merging a Pull Request](#review-and-merging-a-pull-request)
  - [Post-Merge](#post-merge)


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

### Recommended Order of Exposure

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


# If you are a contributor

We assume you have a good understanding of and/or experience with programming languages **chsarp** and **python**. A good level of knowledge/experience is required to contribute to the project in very technical terms, especially on the Unity game engine. Note that having good knowledge/experience in other aspects of development such as 3D prefab model design, animation, and other general game designing is also very welcome. However, having a computer science background is not a requirement, and we welcome contributions from all backgrounds. 

Before you start contributing to the project, you should first familiarize yourself with the project structure and the various components that make up the project. You can find a detailed guide on the project structure [here](/docs/Technical-Overview.md). This documentation will explain the various components of the project, and how they interact with each other. It will also explain how to set up the project for development, and how to run the project in the Unity editor.

Once you are familiar with the project structure, you can start contributing to the project in either or both codebases, located [here](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-unity) (Unity/csharp) and [here](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-python) (Python).

### Next Steps

So you decided on which codebases you want to contribute to...so...what do you do now? 

The next step would be to look at the issues tab of the repository you want to contribute to. The issues tab contains a list of issues that need to be addressed, and is a good place to start if you are new to the project. You can also create your own issues if you have a feature request or a bug report. If you are new to the project, you can start by looking at the issues tagged with the `good first issue` label. These issues are relatively easy to fix, usually with minimal to little testing required. If you are looking for a more challenging issue, you can look at the issues tagged with the `help wanted` label. These issues are more challenging, and may require more effort and time, as well as testing and debugging.

### Creating an Issue/Feature Request
If you have a feature request or a bug report, you can create your own issue in the respective codebase repository. If you are unsure where to submit your issue or request, then choose the codebase repository where the programming language you are using is located. if using both, then choose the codebase repository where the issue is most relevant and make a note of it in the issue description.

Please make sure to follow the issue template, and provide as much information as possible. If you are creating a bug report, please provide the steps to reproduce the bug, as well as the expected and actual behavior. If you are creating a feature request, please provide a detailed description of the feature, as well as the motivation behind the feature. 

_Note well that the feature request may not be accepted, and may be closed if it is not in line with the project goals. Therefore, checking out the Project Roadmap [here](/project/AAI-RoadMap.md) will keep you aligned and oriented._ 

### Pre-Pull Request

Before you create a pull request, there are a few tasks that you should complete. First, you should make sure that your code is well documented, and that you have written unit tests for your code. You should also make sure that your code is well formatted, and that it follows the project style guide. 

We provided a set of sanity check configurations which **must be passed** before creating a pull request. These configurations can be found in the `sanity-checks` folder in the respective codebase repository. You should run these configurations before creating a pull request, and make sure that they pass. If they do not pass, then you should fix the issues before creating a pull request. Additional testing/checks may be beneficial and are welcome. Finally, please state which sanity checks you have run in the pull request description and provide the output of the sanity checks.

### Creating a Pull Request

Once you have fixed an issue or implemented a feature, you can create a pull request to submit your changes. The pull request should be created where the issue or feature request is located and should be linked to the issue or feature request. Please make sure to follow the pull request template, and provide as much information as possible. If you are fixing an issue, please provide the issue number in the pull request description. Please note that a sufficient amount of documentation is required for the pull request to be accepted.

Once you have created the pull request, it will be reviewed by the project maintainers and may request changes. If changes are requested, you should make the requested changes and update the pull request. **Please update any documentation that may be affected by your changes.**

_We kindly ask you to be patient, as it may take some time for your pull request to be reviewed._

### Review and Merging a Pull Request

Once a pull request has been created, it will be reviewed by the _Lead Software Developer_ (alhasacademy@gmail.com). For any questions, feel free to contact him at any time in any stage you are in. 

### Post-Merge

Once your pull request has been merged, you will be added to the list of contributors in the project.


---

Congratulations and thank you so much for contributing to our project and vision. We are very grateful for your contribution and we hope you will continue to contribute to the project in the future.