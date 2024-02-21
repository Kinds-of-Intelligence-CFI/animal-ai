# Useful Scripts/Code

#### Table of Contents

1. [Introduction](#introduction)
2. [Extract Configuration File Objects (Python)](#extract-configuration-file-objects-python)

## Introduction

This document contains useful scripts and code snippets that can be used to perform various tasks.

## Extract Configuration File Objects (Python)

The following Python script can be used to extract the positions of objects from the configuration file of the AAI environment. It saves the laboursome effort of maunally writing down the objects and their various positions. The script uses the `PyYAML` library to parse the YAML file and extract the positions of the objects. 

The script first defines a custom constructor to handle unknown YAML tags, and then uses this constructor to parse the YAML file and extract the positions of the objects. The positions are stored in a dictionary where the keys are the names of the objects and the values are lists of positions. 

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
