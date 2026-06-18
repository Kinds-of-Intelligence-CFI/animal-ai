# Animal-AI RL Libraries

#### Table of Contents
- [Animal-AI w/ Stable Baselines3](#animal-ai-w-stable-baselines3)
- [Animal-AI w/ DreamerV3](#animal-ai-w-dreamerv3)

## Animal-AI w/ Stable Baselines3

Many existing tools for reinforcement learning (such as StableBaselines3) use specific frameworks to wrap the environment and handle the interactions between the environment and the agent. To help with this we provide a Unity to Gymnasium wrapper which converts the regular animal ai environment into a Gymnasium environment that these tools accept.

We actually provide two different wrappers one generic one which can wrap any unity environment `UnityToGymnasiumWrapper` as a backup and an Animal-AI specific wrapper `AnimalAIGymnasiumWrapper` which we recommend you use as it labels the observations for you. 

```python
# Import the necessary environment wrappers.
import animalai
import animalai.envs.environment
from animalai.wrappers.animalai_gymnasium import AnimalAIGymnasiumWrapper
import stable_baselines3

env = animalai.envs.environment.AnimalAIEnvironment(...)

# wrap with the gymnasium wrapper
env_wrapped = AnimalAIGymnasiumWrapper(
    env,
    uint8_visual=True,
    flatten_branched=True,  # Necessary if the agent doesn't support MultiDiscrete action space.
)

# Stable Baselines3 A2C model
model = stable_baselines3.A2C(
    "MlpPolicy",
    env_wrapped,  # type: ignore
    device="cpu",
    verbose=1,
)
model.learn(total_timesteps=10_000)
```

See [here](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-stablebaselines3) for a complete example of using Animal-AI with old gym environments using Stable Baselines3.

## Animal-AI w/ DreamerV3

There is a template repository for using AnimalAI with DreamerV3 [here](https://github.com/Kinds-of-Intelligence-CFI/dreamerv3-animalai).
