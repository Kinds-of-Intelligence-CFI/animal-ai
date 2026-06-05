# Large Language Models in Animal-AI

Animal-AI (AAI) can be used as a testbed for experiments involving Large Language Models (LLMs). Following two studies ([here](https://arxiv.org/abs/2410.23242) and [here](https://www.kaggle.com/competitions/kaggle-measuring-agi/writeups/new-writeup-1775378504699#3436053)) that examined LLMs in AAI, we have added support to simplify the process of using LLMs with AAI.

At a high level, using LLMs in AAI consists of two components; a **scaffold** and a **wrapper**. 

## Scaffolds

The scaffold determines how the model should be allowed to interact with the environment: This involves the prompts the model receives, how the model formats its commands for the AAI environment, and how responses from the environment are provided to the model. The default scaffold we provide is the [FrameByFrameScaffold](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-python/blob/main/animalai/LLM_scaffolds/environment_scaffolds.py#L108), which allows the model to provide a basic input for every frame (or every n frames). A higher-level alternative researchers may like to explore would be to allow the model to write scripts that control the agent such as `Go(10);Turn(90);Go(10)`, as in [this](https://arxiv.org/abs/2410.23242) study.

## Wrappers

To avoid having to adapt their code for different models, researchers should use a standardised framework to run their experiments. We recommend that researchers use the [Inspect](https://inspect.aisi.org.uk/) framework and provide a wrapper for using LLMs in AAI with the inspect framework [here](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-python/blob/main/animalai/LLM_scaffolds/inspect_wrapper.py). We also provide an experimental framework to support using LLMs in AAI with the [Kaggle Benchmarks]() framework [here](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-python/blob/main/animalai/LLM_scaffolds/kaggle_wrapper.py). If researchers would like to use an alternative framework, they can build a wrapper to support it by following the example of the two wrappers we provide.

## Example

This is a minimal example of running an LLM experiment in AAI with the FrameByFrame scaffold and our Inspect wrapper:
```
import os

from inspect_ai import Task, eval as inspect_eval, task
from inspect_ai.solver import Solver, basic_agent, system_message
from inspect_ai.dataset import MemoryDataset, Sample

from animalai.LLM_scaffolds.environment_scaffolds import FrameByFrameScaffold
from animalai.LLM_scaffolds.inspect_wrapper import add_act_tool, close_environment, start_animalai, total_reward_scorer

CONFIG_FILE_PATH = os.path.join("my_folder", "my_config_file.yml")

@task
def basic_arena_task(agent_solver: Solver | None = None) -> Task:
    dataset = MemoryDataset(samples=[
        Sample(
            input="Please go to the green goal.",
            metadata={
                "arenas_configurations": CONFIG_FILE_PATH,
            },
        )
    ])

    solver_chain = [
        system_message(FrameByFrameScaffold.get_default_system_prompt()),
        start_animalai(scaffold_type=FrameByFrameScaffold),
        add_act_tool(scaffold_type=FrameByFrameScaffold),
        agent_solver or basic_agent(),
    ]

    return Task(
        dataset=dataset,
        solver=solver_chain,
        scorer=total_reward_scorer(),
        cleanup=close_environment,
        message_limit=30,
    )


if __name__ == "__main__":
    inspect_eval(
        [basic_arena_task()],
        model="anthropic/claude-sonnet-4-6",
    )
```