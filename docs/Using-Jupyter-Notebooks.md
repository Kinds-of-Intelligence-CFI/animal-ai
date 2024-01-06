
# Using Jupyter Notebooks with Animal-AI

## Table of Contents

- [Introduction to Jupyter Notebooks](#introduction-to-jupyter-notebooks)
- [Setting Up Jupyter Notebooks](#setting-up-jupyter-notebooks)
- [Using Jupyter Notebooks with Animal-AI](#using-jupyter-notebooks-with-animal-ai)
  - [Creating a New Notebook](#creating-a-new-notebook)
  - [Importing Animal-AI Package](#importing-animal-ai-package)
  - [Writing Interactive Scripts](#writing-interactive-scripts)
- [Advantages of Using Jupyter Notebooks](#advantages-of-using-jupyter-notebooks)
- [Tips for Using Jupyter with Animal-AI](#tips-for-using-jupyter-with-animal-ai)

## Introduction to Jupyter Notebooks

_Jupyter Notebooks_ are interactive documents combining live code, output, explanatory text, and visualizations, widely used in data science and machine learning.

## Setting Up Jupyter Notebooks

1. **Install Jupyter**:
   Use pip to install Jupyter:
   ```bash
   pip install notebook
   ```
2. **Start Jupyter Notebook**:
   - Run `jupyter notebook` in the terminal.
   - Or use JupyterLab (`pip install jupyterlab` and `jupyter lab`).
3. **Navigate to Animal-AI (Root) Folder**:
   - Open the folder where your Animal-AI project is located in the Jupyter interface.

## Using Jupyter Notebooks with Animal-AI

### Creating a New Notebook
In the Jupyter interface, create a new Python notebook in your project directory.

### Importing Animal-AI Package
```python
from animalai.envs.environment import AnimalAIEnvironment
# Other necessary imports for your script
```

### Writing Interactive Scripts
- **Initialize Environment**: Set up the Animal-AI environment.
- **Run Experiments**: Write code for experiments, training, or visualization.
- **Visualize Outputs**: Display results using Jupyter's capabilities.

## Advantages of Using Jupyter Notebooks
- **Interactivity**: Test code in small, independent blocks.
- **Documentation**: Combine code with rich text and visualizations.
- **Experimentation**: Ideal for testing new ideas and visualizing data.

## Tips for Using Jupyter with Animal-AI
- **Manage Resources**: Be aware of resource usage, especially when running complex simulations.
- **Kernel Management**: Restart the Jupyter kernel to clear memory and state if needed.
- **Version Control**: Export code to Python scripts for version control in larger projects.
