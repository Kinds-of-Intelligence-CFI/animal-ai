![steampunkFOURcrop](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/assets/65875290/df798f4a-cb2c-416f-a150-093b9382a621)

# Animal-AI

*Animal-Artificial Intelligence*, commonly known as Animal-AI or AAI, serves as a nexus for multi-disciplinary inquiry, aiming to deepen our understanding of cognition in humans, animals, and artificial entities. Its objective is to advance AI research by exploring cognitive abilities and broadening our comprehension of the spectrum of potential minds. AAI is uniquely structured to enable comparative assessments among animals, humans, and artificial intelligences. It encompasses software engineering and research, maintained as an open-source project to foster collaboration.

| ![agent-cyl-fail](project/figs/agent-cyl-fail.gif) | ![agent-cyl-pass](project/figs/agent-cyl-pass.gif) |
|---|---|
| ![animal-cyl-fail](project/figs/animal-cyl-fail.gif) | ![animal-cyl-pass](project/figs/animal-cyl-pass.gif) |


#### Table of Contents
- [Animal-AI](#animal-ai)
      - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Installation](#installation)
  - [Quick Start](#quick-start)
  - [Citing](#citing)
  - [Unity ML-Agents](#unity-ml-agents)
  - [The Animal-AI Community](#the-animal-ai-community)
    - [Notice](#notice)


## Overview

- **Website:** [here](https://animalai.org/)
- **Unity/C# Source Code:** [here](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-unity-project)
- **Python Source Code:** [here](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-package/tree/main/animalai)

This repository serves as the primary hub for essential information and activities related to the Animal-AI environment. It is the exclusive source for all past and forthcoming releases of Animal-AI. To facilitate your initiation, the repository includes a collection of introductory Python scripts for engagement with the environment, alongside an extensive library of over 900 tasks featured in the inaugural Animal-AI Olympics competition. The repository also contains a comprehensive documentation of the environment, including a detailed description of the environment's objects and their properties, as well as a guide to designing experiments with the environment from scratch. More advanced tutorials are also found, such as how to train agents in Animal-AI environments. 

_If you wish to contribute to the project, please familiarize yourself with the [Contributing Guide](contributing.md) and the [Code of Conduct](codeOfConduct.md) first._ A comprehensive documentation of how Animal-AI works is also available [here](docs/Technical-Overview.md.md), where you can understand the inner workings of how the environment is built and how it functions (_csharp_ and _Python_ codebases).

The Animal-AI environment and packages are currently tested on **Windows 11**, **Linux**, and **MacOS**, with **Python 3.9.x** support, but **Python 3.6.x+** has been reported to be working also. **Linux distros** are also working and stable. 


## Features

**Interdisciplinary Research Platform:**
- Facilitates research in human, animal, and artificial cognition.
- Supports cross-disciplinary studies.
- Enables comparative assessments among humans, animals, and artificial intelligences.

**Comprehensive AI Environment:**
- Includes a versatile environment for AI experiments, from basic to advanced configurations.
- Wrap Unity learning environments as a gym environment
- Wrap Unity learning environments as a PettingZoo environment
- Support for several Deep Reinforcement Learning algorithms (PPO, SAC, MA-POCA, self-play).

**Extensive Task Library:**
- Multiple example tasks.
- Over 900 tasks from the Animal-AI Olympics.
- Procedural Generation functionality
- Additional tasks for demonstration and experimentation.

**Unity Game Engine:**
- Utilizes Unity ml-agents.
- Leverages Unity game engine for advanced simulation capabilities.
- Fast and robust wrapper.

**Cross-Platform Compatibility:**
- Compatible with Windows 11, Linux, and MacOS.
- Supports Python 3.6.x and above.

**Control Modes:**
- Player mode for interactive environment control, for human testing.
- Training mode for Reinforcement Learning, with support for tensorflow analysis.
- Supports AI model training across different systems.

**Interactive and Dynamic Environment:**
- Offers interactive elements for complex AI training.
- Supports dynamic environment generation.


## Installation

*See [here](docs\installation\InstallationGuide.md) for a detailed installation guide.*

([latest release](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/releases/tag/v3.1.4)) / ([all releases](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/releases))

For legacy versions of Animal-AI, please see ([legacy releases](project\AAIVersionsArchive.md))


## Quick Start

We've prepared a comprehensive set of tutorials to help you get started with the Animal-AI environment. Your first stop should be the [Getting Started Guide](docs\installation\QuickStart.md), which will guide you on where to start and where to go next depending on your interests and experience.


## Citing

We recently published our new paper on Animal-AI, which you can find [here](https://arxiv.org/abs/2312.11414). If you use Animal-AI in your research, please cite our paper:

 _Voudouris, K., Alhas, I., Schellaert, W., Crosby, M., Holmes, J., Burden, J., Chaubey, N., Donnelly, N., Patel, M., Halina, M,. Hernández-Orallo, J. & Cheke, L. G. (2023). Animal-AI 3: What's New & Why You Should Care. arXiv preprint arXiv:2312.11414._
```
@article{voudouris2023animal,
  title={Animal-AI 3: What's New \& Why You Should Care},
  author={Voudouris, Konstantinos and Alhas, Ibrahim and Schellaert, Wout and Crosby, Matthew and Holmes, Joel and Burden, John and Chaubey, Niharika and Donnelly, Niall and Patel, Matishalin and Halina, Marta and Hernández-Orallo, José and Cheke, Lucy G.},
  journal={arXiv preprint arXiv:2312.11414},
  year={2023}
}
```
For further publications related to Animal-AI, see our website [here](https://sites.google.com/csah.cam.ac.uk/animalai/resources).


## Unity ML-Agents

Juliani, A., Berges, V., Vckay, E., Gao, Y., Henry, H., Mattar, M., Lange, D. (2018). [Unity: A General Platform for Intelligent Agents.](https://arxiv.org/abs/1809.02627) *arXiv preprint arXiv:1809.02627*

Documentation for [ML-Agents](https://github.com/Unity-Technologies/ml-agents) should be consulted if you want additional resources or to make any changes.


## The Animal-AI Community 

Animal-AI has been an open-source research project from the beginning. If you wish to contribute to the project, please refer to the [Contributing Guide](contributing.md) for more information, and to the [Code of Conduct](codeOfConduct.md) for guidelines on how to interact with the community. 


---
### Notice

   _Copyright 2024 Kinds of Intelligence, Centre for the Future of Intelligence, University of Cambridge._
   
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

