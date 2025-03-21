# CSV Logger Feature Guide

#### Table of Contents

* [Introduction](#introduction)
* [How does the CSV Logger feature work?](#how-does-the-csv-logger-work)
* [What data is logged?](#what-data-is-logged)
* [Notes/Limitations](#notes-limitations)

## Introduction

The CSV Logger, introduced in Animal-AI version 4.1.0, automatically records experiment results into a CSV file, eliminating manual effort. This feature runs in the background during Animal-AI sessions and stops when the application closes. It is particularly useful for tracking and comparing experiment outcomes, and it is enabled by default in both Play and Train modes.

Note that you may need to give Animal-AI permission to write via the terminal (macOS and Linux only). If you encounter an error, please run the following command in the terminal:

```bash
chmod +x env/AnimalAI.x86_64 or chmod 777 -R -W AnimalAI.app
```

### How does the CSV Logger work?

The CSV Logger saves experiment data to a CSV file located in the `AnimalAI/ObservationLogs` directory. The file is named `Observations_DD-MM-YEAR_HH-MM.csv` , where the date and time correspond to when Animal-AI was launched. The CSV file captures detailed data for analysis.

To access the .`csv file`, navigate to the `AnimalAI/ObservationLogs` directory and open the CSV file in a spreadsheet application like Excel or Google Sheets.

### What data is logged?

Currently, the CSV Logger records the following data:

* **Episode**
* **Step** (the below data is logged at each step)
* **Health**
* **Reward**
* **Velocity** (x, y, z)
* **Position** (x, y, z)
* **Actions Taken** (Rotation, Movement, with descriptions)
* **Was Agent Frozen?**
* **Was Success/Failure Notification Shown?**
* **Was Reward Dispersed?** (i, e, was a reward spawned from a dispenser?)
* **Dispersed Reward Type** (i.e. GoodGoal, BadGoal, etc.)
* **Collected Reward Type** (i.e. GoodGoal, BadGoal, at step n)
* **Was SpawnerButton Triggered?** (i.e. was a button pressed to spawn a reward?)
* **Combined Spawner Information** (i.e. what was dispersed and how many rewards were dispersed by which dispensers)
* **Was Agent In DataZone?** (i.e. was the Agent in the DataZone at step n)
* **Active Camera** (i.e. which camera was active at step n)
* **Combined Raycast Data** (i.e. what was the raycast data at step n)

The above data is logged at each step, providing a detailed record of the experiment. This data can be used to analyze agent behavior, track progress, and compare results across different experiments.

Additionally, the following summaries are added to the CSV file after each episode
* **Positive Goals Collected** This is the count of positive goals collected during the episode

### Notes/Limitations

* There is no way to disable writing the CSV file currently. A feature for this will be added, but please get in touch if it is causing you issues and we can prioritise adding this feature.
* Due to a bug during training, the first and second episodes are not logged. This issue is to be being addressed in a future release. However, this is only a problem during training, and the CSV Logger works as expected in Play mode.
* The .csv file can't be saved anywhere else. It is saved in the `AnimalAI/ObservationLogs` directory by default.
* Multiple `.csv files` can't be generated at the same time. The CSV Logger generates a single .csv file for each Animal-AI session. This is to prevent data from being overwritten or lost.
* The name of the .csv file is based on the date and time when Animal-AI was launched. This naming convention helps to identify the file easily. It is recommended to rename the file if you want to keep multiple files for comparison.