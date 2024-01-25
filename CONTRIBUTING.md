# How to Contribute to Animal-AI

Welcome! We are glad that you want to contribute to Animal-AI! This document will help you get started.

#### Table of Contents

* [Introduction](#introduction)
* [Ways to Contribute](#ways-to-contribute)
* [1. Fork the repository](#1-fork-the-repository)
* [2. Set up your development environment](#2-set-up-your-development-environment)
* [3. Contribution Workflow](#3-contribution-workflow)
  + [Creating an Issue/Feature Request](#creating-an-issuefeature-request)
  + [Pre-Pull Request](#pre-pull-request)
  + [Creating a Pull Request](#creating-a-pull-request)
  + [Review and Merging a Pull Request](#review-and-merging-a-pull-request)
  + [Post-Merge](#post-merge)

## Introduction

As you get started, you are in the best position to give us feedback on areas of our project that we need help with including:

* Problems found during setting up a new developer environment
* Gaps in our Getting Started Guide or documentation
* Bugs in our automation scripts

If anything doesn't make sense, or doesn't work when you run it, please open a bug report and let us know!

## Ways to Contribute

We welcome many different types of contributions including:

* New features
* Builds, CI/CD
* Bug fixes
* Documentation
* Issue Triage

## 1. Fork the repository

Fork the respective Animal-AI 'sister' repositories (Unity/C# and/or Ml-agents/Python) by clicking on the "Fork" button in the top right corner of the repositories, located here: [Unity](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-unity-project) and [Python](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-package).

## 2. Set up your development environment

Clone the forked repository to your local machine using Git. Install the necessary dependencies (pip install animalai) and follow the instructions provided in the documentation to set up your development environment properly. Create a new branch for your changes and start working on your contribution.

So you decided on which codebases you want to contribute to...so...what do you do now? 

The next step would be to look at the issues tab of the repository you want to contribute to. The issues tab contains a list of issues that need to be addressed, and is a good place to start if you are new to the project. You can also create your own issues if you have a feature request or a bug report. If you are new to the project, you can start by looking at the issues tagged with the `good first issue` label. These issues are relatively easy to fix, usually with minimal to little testing required. If you are looking for a more challenging issue, you can look at the issues tagged with the `help wanted` label. These issues are more challenging, and may require more effort and time, as well as testing and debugging.

## 3. Contribution Workflow

### Creating an Issue/Feature Request

If you have a feature request or a bug report, you can create your own issue in the respective codebase repository. If you are unsure where to submit your issue or request, then choose the codebase repository where the programming language you are using is located. If using both, then choose the codebase repository where the issue is most relevant and make a note of it in the issue description.

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

**Remember to always adhere to the project's code of conduct, be respectful, and follow any specific contribution guidelines provided by the Animal-AI project.**

**Happy contributing!**
