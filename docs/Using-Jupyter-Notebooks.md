# Using Jupyter Notebooks for Animal-AI

This guide combines instructions on creating a custom kernel for Jupyter Notebooks and specific steps for using Jupyter Notebooks with the Animal-AI environment. It is advised that you either create a python virtual environment or Anaconda for easier project management. See [Using-Virtual-Environments](/docs/Using-Virtual-Environment.md) for more information on creating and using a virtual environment. For more information on Jupyter Notebooks, refer to the [official documentation](https://jupyter-notebook.readthedocs.io/en/stable/)

#### Table of Contents

* [Creating a Kernel for Jupyter Notebooks](#creating-a-kernel-for-jupyter-notebooks)
* [Using Jupyter Notebooks with Animal-AI](#using-jupyter-notebooks-with-animal-ai)
* [Advantages of Using Jupyter Notebooks](#advantages-of-using-jupyter-notebooks)
* [Tips for Effective Jupyter Notebook Use](#tips-for-effective-jupyter-notebook-use)

## Creating a Kernel for Jupyter Notebooks

### Step-by-Step Guide

1. **Install the IPython Kernel**: 
   

```bash
   pip install ipykernel
   ```

2. **Create a New Python Environment**:
   - Using venv: 

     

```bash
     python -m venv /path/to/new/virtual/environment
     ```

   - Using Conda:

     

```bash
     conda create -n myenv python=3.x
     ```

3. **Activate the Environment**:
   - Using venv:

     

```bash
     source /path/to/new/virtual/environment/bin/activate
     ```

   - Using Conda:

     

```bash
     conda activate myenv
     ```

4. **Install Necessary Packages**:
   

```bash
   pip install numpy pandas matplotlib
   ```

5. **Add Your Kernel to Jupyter**:
   

```bash
   ipython kernel install --name "myenv" --user
   ```

6. **Launch Jupyter Notebook**:
   

```bash
   jupyter notebook
   ```

7. **Select Your Kernel**:
   Choose "myenv" from the kernel list in Jupyter.

### Notes

* Replace placeholders with your desired directory and environment name.
* Adjust Python version as needed.

## Using Jupyter Notebooks with Animal-AI

### Introduction

_Jupyter Notebooks_ are interactive documents that combine live code, output, text, and visualizations.

### Setup

1. **Install Jupyter**:
   

```bash
   pip install notebook
   ```

2. **Start Jupyter Notebook**:
   - Use `jupyter notebook` or JupyterLab ( `jupyter lab` ).

### Using with Animal-AI

* **Create a New Notebook**: In your project directory.
* **Import Animal-AI Package**:
  

```python
  from animalai.envs.environment import AnimalAIEnvironment
  # Other necessary imports for your script
  ```

### Writing Interactive Scripts

* **Initialize Environment**: Set up the Animal-AI environment.
* **Run Experiments**: Write code for experiments, training, or visualization.
* **Visualize Outputs**: Display results using Jupyter's capabilities.

## Advantages of Using Jupyter Notebooks

* **Interactivity**: Test code in small, independent blocks.
* **Documentation**: Combine code with rich text and visualizations.
* **Experimentation**: Ideal for testing new ideas and visualizing data.

## Tips for Effective Jupyter Notebook Use

* **Manage Resources**: Be aware of resource usage, especially when running complex simulations.
* **Kernel Management**: Restart the Jupyter kernel to clear memory and state if needed.
* **Version Control**: Export code to Python scripts for version control in larger projects.
