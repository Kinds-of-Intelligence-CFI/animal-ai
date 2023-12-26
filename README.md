![steampunkFOURcrop](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/assets/65875290/df798f4a-cb2c-416f-a150-093b9382a621)

# Animal-AI

*Animal-Artificial Intelligence*, commonly known as Animal-AI or AAI, serves as a nexus for multi-disciplinary inquiry, aiming to deepen our understanding of cognition in humans, animals, and artificial entities. Its objective is to advance AI research by exploring cognitive abilities and broadening our comprehension of the spectrum of potential minds. AAI is uniquely structured to enable comparative assessments among animals, humans, and artificial intelligences. It encompasses both software engineering and research, maintained as an open-source project to foster collaborative progress.

| ![](project\figs\agent-cyl-fail.gif) | ![](project\figs\agent-cyl-pass.gif) |
|---|---|
| ![](project\figs\animal-cyl-fail.gif) | ![](project\figs\animal-cyl-pass.gif) |


### Table of Contents
1. [Features](#features)
2. [Quick Install](#quick-install)
3. [Tutorials and Examples](#tutorials-and-examples)
4. [Citing Animal-AI](#citing-animal-ai)
5. [Unity ML-Agents](#unity-ml-agents)
6. [Animal-AI and the community](#animal-ai-and-the-community)
7. [License Notice](#license-notice)

- **Website:** [here](https://animalai.org/)
- **Unity Source Code:** [here](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-unity-project)
- **Python Source Code:** [here](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-package/tree/main/animalai)

This repository serves as the primary hub for essential information and activities related to the AnimalAI environment. It is the exclusive source for all past and forthcoming releases of Animal-AI. To facilitate your initiation, the repository includes a collection of introductory Python scripts for engagement with the environment, alongside an extensive library of over 900 tasks featured in the inaugural Animal-AI Olympics competition. The repository also contains a comprehensive documentation of the environment, including a detailed description of the environment's objects and their properties, as well as a guide to designing experiments with the environment.

The Animal-AI environment and packages are currently tested on **Windows 11**, **Linux**, and **MacOS**, with minimum **Python 3.9.x**, but Python 3.6+ has been reported to be working also. **Linux distros** are also working and stable.


## Features

**Interdisciplinary Research Platform:**
- Facilitates research in human, animal, and artificial cognition.
- Supports cross-disciplinary studies.

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
- Player mode for interactive environment control, for manual testing.
- Training mode for Reinforcement Learning, with support for tensorflow analysis.
- Supports AI model training across different systems.

**Interactive and Dynamic Environment:**
- Offers interactive elements for complex AI training.
- Supports dynamic environment generation.


## Quick Install

*See [here](docs\installation\InstallationGuide.md) for a more detailed installation guide.*

([latest release](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/releases/tag/v3.1.4)) / ([all releases](https://github.com/Kinds-of-Intelligence-CFI/animal-ai/releases))

For legacy versions of Animal-AI, please see ([legacy releases](project\AAIVersionsArchive.md))


## Tutorials and Examples

Some example scripts to get started can be found in the `docs/configGuide` folder. The following docs provide information for some common uses of the environment.

- [Getting started with the environment](docs\installation\QuickStart.md)
- [Using the ML-Agents Low-Level API: A hand-coded Braitenberg Vehicle baseline](docs/lowLevelAPI.md)
- [Designing Experiments](docs/configFile.md)
- [Training examples](docs/training.md)


## Citing

If you use the Animal-AI environment in your work you can cite the environment paper:

 Crosby, M., Beyret, B., Shanahan, M., Hernández-Orallo, J., Cheke, L. & Halina, M.. (2020). The Animal-AI Testbed and Competition. Proceedings of the NeurIPS 2019 Competition and Demonstration Track, in Proceedings of Machine Learning Research 123:164-176 Available [here](http://proceedings.mlr.press/v123/crosby20a.html).
```
 @InProceedings{pmlr-v123-crosby20a, 
    title = {The Animal-AI Testbed and Competition}, 
    author = {Crosby, Matthew and Beyret, Benjamin and Shanahan, Murray and Hern\'{a}ndez-Orallo, Jos\'{e} and Cheke, Lucy and Halina, Marta}, 
    booktitle = {Proceedings of the NeurIPS 2019 Competition and Demonstration Track}, 
    pages = {164--176}, 
    year = {2020}, 
    editor = {Hugo Jair Escalante and Raia Hadsell}, 
    volume = {123}, 
    series = {Proceedings of Machine Learning Research}, 
    month = {08--14 Dec}, 
    publisher = {PMLR}, 
} 
```


## Unity ML-Agents

Animal-AI as well as The Animal-AI Olympics is built using [Unity's ML-Agents Toolkit.](https://github.com/Unity-Technologies/ml-agents)

Juliani, A., Berges, V., Vckay, E., Gao, Y., Henry, H., Mattar, M., Lange, D. (2018). [Unity: A General Platform for Intelligent Agents.](https://arxiv.org/abs/1809.02627) *arXiv preprint arXiv:1809.02627*

Further the documentation for [mlagents](https://github.com/Unity-Technologies/ml-agents) should be consulted if you want to make any changes.


## Animal-AI and the community

Animal-AI has been an open-source research project from the beginning. If you wish to contribute to the project, please refer to the [Contributing Guide](contributing.md) for more information, and to the [Code of Conduct](codeOfConduct.md) for guidelines on how to interact with the community. 

---
- v3.1.3
  - Resolved Spawner Tree Clock and Multiple Arenas cycling issues
  - Enhanced multiple arenas randomization via the randomizeArenas parameter in YAML
    - Adjusted code to handle arenas with negative IDs by converting them to positive
    - Added more robust error-checking for arena ID's and arena cycling
  - Addressed Unity native warning in Training Arena script
  - Rectified the invisibility issue of the Sign Poster game object
  - Conducted unit tests on TrainingArena.cs and ArenaParameters.cs
  - Shortened end-of-episode notification to 2.5 seconds; also added visual elements of paired reinforcing cues such as colours and short GIFs for better visual understanding for the 'user'
  - Undertook minor Unity script optimizations
- v3.1.2
  - Implemented hot fix for an undiscovered and new bug that affected the Spawner Tree
- v3.1.1
  - Introduced a new feature: "End of Episode Notification." When activated, the episode concludes with a notification for the user/player if their cumulative reward meets or exceeds the threshold set in the config file.
  - Fixed bug that affected the Spawner Tree
- v3.1.0
  - Introduced the "Interactive Button" feature, allowing the player/agent to engage with a button that, through a probabilistic algorithm, may generate a reward.
  - Fixed various bugs.
  - "Headless" mode is tested and supported unofficially - can be used for training agents (works with Raycasting).
  - Further performance improvements to overall project.
- v3.0.2
  - Upgraded Mlagents to 2.3.0-exp3 (mlagents python version 0.30.0)
- v3.0.1
  - Added Agent Freezing Parameter, enabling you to freeze the agent for no reward decrement at the start of an episode, while other objects continue to move around.
- v3.0 **Note that due to the changes to controls and graphics agents trained on previous versions might not preform the same**
  - Updated agent handling. The agent now comes to a stop more quickly when not moving forwards or backwards and accelerates slightly faster.
  - Added new objects, spawners, signs, goal types (see [doc](docs/definitionsOfObjects.md)).
  - Added 3 animal skins to the player character.
  - Updated graphics for many objects. Default shading on many previously plain objects make it easier to determine location(s)/velocity.
  - Made the Unity Environment available (see link on main page).
  - Many improvements to documentation and examples.
  - Upgraded to Mlagents 2.1.0-exp.1 (ml-agents python version 0.27.0).
  - Fixed various bugs.
- v2.2.3
  - Now you can specify multiple different arenas in a single yml config file ant the environment will cycle through them each time it resets.
- v2.2.2 
  - Low quality version with improved fps. (will work on further improvments to graphics & fps later).
- v2.2.1
  - Improve UI scaling wrt. screen size.
  - Fixed an issue with cardbox objects spawning at the wrong sizes.
  - Fixed an issue where the environment would time out after the time period even when health > 0 (no longer intended behaviour).
  - Improved Death Zone shader for weird Zone sizes.
- v2.2.0 Health and Basic Scripts.
  - Switched to health-based system (rewards remain the same).
  - Updated overlay in play mode.
  - Allow 3D hot zones and death zones and make them 3D by default in old configs.
  - Added rewards that grow/decay (currently not configurable but will be added in next update).
  - Added basic Gym Wrapper.
  - Added basic heuristic agent for benchmarking and testing.
  - Improved all other python scripts.
  - Fixed a reset environment bug when resetting during training.
  - Added the ability to set the DecisionPeriod (frameskip) when instantiating and environment.
- v2.1.1 bugfix
  - Fixed raycast length being less then diagonal length of standard arena.
- v2.1 beta release
  - Upgraded to ML-Agents release 2 (0.26.0).
  - New features:
    - Added raycast observations
    - Added agent global position to observations


### Notice

   Copyright 2023 Kinds of Intelligence, Centre for the Future of Intelligence, University of Cambridge
   
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
