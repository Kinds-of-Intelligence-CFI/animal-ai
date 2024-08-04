# Getting Started

Welcome to Animal-AI! This document serves as your introductory guide, outlining the recommended steps to begin working with the project. It acts as a central hub, linking you to various documentation and resources essential for a comprehensive understanding of Animal-AI. Follow this guide to navigate through the project efficiently and make the most of the available resources.

#### Table of Contents

* [What is Animal-AI?](#what-is-animal-ai)
  - [What is the aim of the project?](#what-is-the-aim-of-the-project)
  - [What is the background of the project?](#what-is-the-background-of-the-project)
* [If you are a researcher](#if-you-are-a-researcher)
  + [Recommended Order of Exposure](#recommended-order-of-exposure)
* [If you are a contributor](#if-you-are-a-contributor)


# What is Animal-AI?

Animal-AI is an advanced platform for training and evaluating AI agents and human participants on diverse tasks that require a nuanced understanding of their environment. Built on the Unity game engine and utilizing the ML-Agents Toolkit for backend functionality, Animal-AI is both extensible and user-friendly.

The platform supports comparative studies of cognitive capabilities across humans, animals, and AI agents through a range of tasks and experiments. It is designed to cater to both researchers and developers:

- **Researchers:** Use Animal-AI to train and test AI agents on various tasks. You can also leverage these tasks as computer games to assess cognitive abilities in humans.
- **Developers:** Contribute to the platform by adding new tasks, environments, and features to enhance its capabilities.

As an open-source project, Animal-AI encourages collaboration and innovation from the community.

#### What is the aim of the project?

The aim of the Animal-AI project is to create a unified platform that allows researchers to study cognitive capabilities across humans, animals, and AI agents using a common set of tasks. These tasks are designed to be cognitively informative and meaningful, enabling researchers to triangulate performance patterns and develop comprehensive "cognitive profiles."

This approach facilitates direct comparison of cognitive profiles across different types of minds. For AI, it translates to a robust evaluation of underlying capabilities, aiding in the prediction and development of AI systems based on their capabilities. For cognitive scientists, it provides a direct method for exploring theories of cognition and identifying key tasks that are useful for distinguishing between different cognitive theories.

**You can find the project Roadmap [here](/project/AAI-RoadMap.md).**

#### What is the background of the project?

The Animal-AI project originated from the Kinds of Intelligence (KOI) programme within the Leverhulme Centre for the Future of Intelligence (LCFI). It began as a collaborative effort between the Cambridge branch (Dr. Lucy Cheke, Dr. Marta Halina) and the Imperial branch (Dr. Matthew Crosby, Prof. Murray Shanahan) of the centre. The project has since expanded into an open and collaborative initiative, involving additional institutions such as Universitat Politècnica de València (Prof. José Hernández-Orallo) and others.

Please check our website for more information on the team [here](https://sites.google.com/csah.cam.ac.uk/animalai/).

# If you are a researcher

If you have a basic understanding of Python programming and are familiar with Artificial Intelligence (particularly Reinforcement Learning), Animal-AI offers a user-friendly platform for training and testing AI agents on various tasks, even if you have limited experience in game development. Built on the Unity game engine, Animal-AI provides a range of example tasks through configuration files. These files, written in YAML, are the primary means of interacting with the platform. YAML is a human-readable data serialization language, so minimal programming experience is needed to use the platform effectively.

To get started, follow the recommended order of exposure below to ensure a smooth introduction and comprehensive understanding of the platform:

### Recommended Order of Exposure

To get started with Animal-AI, follow the recommended steps below. These guides will help you install, launch, and make the most out of the platform:

1. **Install the Platform**  
   If you haven't installed Animal-AI yet, start with the detailed installation guide:
   * [Installation Guide](/docs/gettingStarted/Installation-Guide.md)

2. **Launch the Platform**  
   Learn how to launch Animal-AI and run your first configuration file:
   * [Launching Animal-AI](/docs/gettingStarted/Launching-AAI.md)

3. **Explore an Example Configuration File**  
   Download or copy an example configuration file to get a practical sense of how things work:
   * [Example Configuration File](/docs/configGuide/Example-YAML-File.yaml)

4. **Understand the Arena Environment**  
   Get an introduction to the Arena Environment and the Agent:
   * [Arena Environment Guide](/docs/Arena-Environment-Guide.md)

5. **Learn About Arena Objects**  
   Dive into the comprehensive guide on available objects and their properties to enhance your understanding of the Arena Environment:
   * [Arena Objects Guide](/docs/Arena-Object-Definitions.md)

6. **Create Your Own Configuration Files**  
   Once you are familiar with the Arena Environment and objects, proceed to learn how to create your own configuration files:

   - If you're new to YAML, start here:
     * [Background on YAML](/docs/Background-YAML.md)
   - Next, review the guide on using YAML specifically in Animal-AI:
     * [YAML Configuration Guide](/docs/configGuide/YAML-Config-Syntax.md)

7. **Explore Integration Options**  
   If you're interested in integrating Animal-AI with other AI libraries, refer to the integration guide:
   * [Using Animal-AI with Stable-Baselines3 and Dreamerv3](/docs/integration/Integrate-AAI.md)

Feel free to follow this order or adjust according to your interests and needs. The guides are designed to facilitate a smooth learning process but are not mandatory to follow in sequence.

# If you are a Contributor

We expect contributors to have a solid understanding of and/or experience with programming languages such as **C#** and **Python**. Experience with the Unity game engine is particularly valuable. Additionally, expertise in related areas such as 3D prefab model design, animation, and general game design is highly welcome. However, a computer science background is not a requirement, and we encourage contributions from individuals with diverse backgrounds.

### Getting Started

1. **Understand the Project Structure**  
   Familiarize yourself with the project's structure and components. A detailed guide is available [here](/docs/Technical-Overview.md). This documentation will explain the various components of the project, how they interact, and how to set up and run the project in the Unity editor.

2. **Explore the Codebases**  
   Contributions can be made to either or both codebases:
   - **Unity/C#**: [Animal-AI Unity Repository](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-unity)
   - **Python**: [Animal-AI Python Repository](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-python)

3. **Review the Contributing Guide**  
   For detailed guidelines on how to contribute, please refer to the [Contributing Guide](/CONTRIBUTING.md).

We appreciate your interest in contributing to Animal-AI and look forward to your valuable input.
