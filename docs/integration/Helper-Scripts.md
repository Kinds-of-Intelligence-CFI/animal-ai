# Useful Scripts/Code

#### Table of Contents

  - [Introduction](#introduction)
  - [Extract Configuration File Objects (Python)](#extract-configuration-file-objects-python)
  - [Randomize Object Positions (Python)](#randomize-object-positions-python)
  - [Replace Old Parameters w/ New Ones (Python)](#replace-old-parameters-w-new-ones-python)
  - [Animal-AI Config Assistant Tool](#animal-ai-config-assistant-tool)

## Introduction

This document provides useful scripts and code snippets for various tasks. Developed in Python versions `3.9.9` and `3.10.0`, these scripts may require additional libraries.

## Extract Configuration File Objects (Python)

The following Python script extracts the positions of objects from an AAI environment configuration file. This automation saves the effort of manually recording objects and their positions. The script uses the `PyYAML` library to parse the YAML file and extract the positions of the objects.

The script first defines a custom constructor to handle unknown YAML tags. Then, it uses this constructor to parse the YAML file and extract the positions of the objects. The positions are stored in a dictionary where the keys are the names of the objects and the values are lists of positions.

The script can be used as follows:

```python

import yaml

# Custom constructor for handling unknown YAML tags (needed to avoid errors when loading the YAML file for AAI)
def custom_constructor(loader, tag_suffix, node):
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    elif isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    return None


yaml.add_multi_constructor("", custom_constructor)


def parse_config_file(file_path):
    with open(file_path, "r") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        return config


def extract_objects_positions(config):
    objects_positions = {}
    for arena_id, arena in config["arenas"].items():
        for item in arena["items"]:
            object_name = f"{item['name']}_arena{arena_id}"
            positions = item.get("positions", [])
            if object_name not in objects_positions:
                objects_positions[object_name] = []
            objects_positions[object_name].extend(positions)
    return objects_positions


# Specify the file path here
file_path = "test.yml"
config = parse_config_file(file_path)
objects_positions = extract_objects_positions(config)
print(objects_positions)
```

## Randomize Object Positions (Python)

The following Python script randomizes the positions of objects in an AAI environment configuration file. It reads the configuration file, shuffles the object positions, and writes the updated configuration to a new file. This script is useful for generating variations of the environment with different object positions.

The script uses the `PyYAML` library to parse the YAML file and update the positions of the objects. It shuffles the positions of each object in each arena and then writes the updated configuration to a new file.

The script can be used as follows:

```python
# IMPORTANT! Please install ruamel.yaml package before running this script. You can do so by running the following command:
# pip install ruamel.yaml

from ruamel.yaml import YAML
import random

# Randomize positions of all items in the configuration file.
def randomize_positions(data):
    for arena in data['arenas'].values():
        for item in arena['items']:
            for position in item['positions']: # Randomize all positions, or just the axis you'd like within the boundary of the arena.
                position['x'] = random.randint(1, 40)  # Randomize x
                position['y'] = random.randint(1, 15)  # Randomize y
                position['z'] = random.randint(1, 40)  # Randomize z

# Load the configuration file. Please adjust the file path to match your configuration file.
file_path = 'location-of-your-config-file.yaml'
output_path = 'where-to-save-the-new-config-file.yaml'

yaml = YAML()
yaml.preserve_quotes = True

with open(file_path, 'r') as f:
    data = yaml.load(f)

randomize_positions(data)

with open(output_path, 'w') as f:
    yaml.dump(data, f)

print("Updated YAML configuration saved. Please check the output file.")
```

Simply adjust the `file_path` and `output_path` variables to point to your configuration file and the location where you want to save the updated configuration file, respectively. The script will randomize the positions of all items in the configuration file and save the updated configuration to the specified output file.

**_Note that the script overrites the original file, so it is recommended to make a backup of the original file before running the script._**

## Replace Old Parameters w/ New Ones (Python)

The following Python script can be used to replace old parameters with new ones in the configuration file of the AAI environment. It reads the configuration file, replaces the old parameters with new ones, particularly `"t"` & `"pass_mark"` with `"timeLimit"` & `"passMark"` respectively. It then writes the updated configuration file to a new file. This script can be useful for updating the configuration file with new parameters.

This script was developed to mitigate the need to manually replace these parameters in the configuration file, helpful if you have many configs to update.

The script can be used as follows:

```python
# Replace old parameters with new ones in the configuration file.
import os

# Replace old parameters with new ones in the configuration file.
def replace_yaml_keys(file_path, replacements):
    try:
        # Reads the original YAML file
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Replaces keys based on the replacements dictionary
        for old_key, new_key in replacements.items():
            content = content.replace(f'{old_key}:', f'{new_key}:')
        
        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(content)
        
        print(f'YAML parameters replaced successfully in {file_path}!')
    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except Exception as e:
        print(f'An error occurred while processing {file_path}: {str(e)}')

# Define the folder path containing the YAML files
folder_path = '/Users/vanguard/Desktop/configs/competition'

replacements = {
    't': 'timeLimit',
    'pass_mark': 'passMark'
}

# Check if the folder exists
if not os.path.exists(folder_path):
    print(f'Folder not found: {folder_path}')
else:
    # Iterate over each file in the folder
    yaml_files = [filename for filename in os.listdir(folder_path) if filename.endswith('.yaml')]
    
    if len(yaml_files) == 0:
        print(f'No YAML files found in {folder_path}')
    else:
        for filename in yaml_files:
            file_path = os.path.join(folder_path, filename)
            
            # Call the function to implement the changes for each file
            replace_yaml_keys(file_path, replacements)
```

Simply adjust the `file_path` variable to point to your configuration file. The script will replace the old parameters with the new ones in the configuration file and save the updated configuration to the same file. 

**_Note that the script overrites the original file, so it is recommended to make a backup of the original file before running the script._**

## Animal-AI Config Assistant Tool

The Animal-AI Config Assistant Tool is a Python helper-tool that helps you create, manage, debug, and visualise configuration files for Animal-AI environments. It provides a user-friendly interface to generate configuration files for different environments, without the need to manually edit the configuration files in YAML.

<p align="center">
  <img height="250" src="/docs/figs/ConfigCompanionFigure.png">
</p>

Visit our [GitHub repository](https://github.com/Kinds-of-Intelligence-CFI/aai-config-assist) for more information and to download the tool.