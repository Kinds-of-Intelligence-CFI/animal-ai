# CSV Logger Feature Guide

#### Table of Contents

* [Introduction](#introduction)
* [How does the CSV Logger feature work?](#how-does-the-csv-logger-feature-work)
* [What data is logged by the CSV Logger feature?](#what-data-is-logged-by-the-csv-logger-feature)

## Introduction

First introduced in Animal-AI version 4.1.0, the CSV Logger is a tool that allows you to log the results of your experimentations in a CSV file, without any manual labour. It runs in the background whilst Animal-AI is running and turns off when you close the application. This feature is useful for keeping track of the results of your experimentations and for comparing the results of different experimentations. It can be used in Play or Train modes, enabled by default in the Animal-AI environment.

### How does the CSV Logger feature work?

The CSV Logger feature logs the results of your experimentations in a CSV file. The CSV file is saved in the `AnimalAI/ObservationLogs` directory. The CSV file is named `Observations_DD-MM-YEAR_HH-MM.csv`, where `DD-MM-YEAR` is the date and `HH-MM` is the time when the CSV file was created (when Animal-AI is launched). The CSV file contains the following data/columns:

### What data is logged by the CSV Logger feature?

Currently, the CSV Logger feature logs the following data:

- Episode
- Step
- Reward
- Velocity (x, y, z)
- Position (x, y, z)
- Actions Taken (Rotation, Movement, with descriptions)
- Was Agent Frozen?
- Was Success/Failure Notification Shown?
- Was Reward Dispersed? (i,e, was a reward spawned from a dispenser?)
- Dispersed Reward Type (i.e. GoodGoal, BadGoal, etc.)
- Collected Reward Type (i.e. GoodGoal, BadGoal, at step n)
- Was SpawnerButton Triggered? (i.e. was a button pressed to spawn a reward?)
- Combined Spawner Information (i.e. what was dispersed and how many rewards were dispersed by which dispensers)
- Was Agent In DataZone? (i.e. was the Agent in the DataZone at step n)
- Active Camera (i.e. which camera was active at step n)
- Combined Raycast Data (i.e. what was the raycast data at step n)

We can see that the CSV Logger feature logs a lot of information about the the environment and the Agent. This information can be used to analyze the results of the experimentations and to compare the results of different experimentations.
