# Animal-AI RL Libraries

#### Table of Contents
- [Animal-AI w/ Stable Baselines3](#animal-ai-w-stable-baselines3)
- [Animal-AI w/ DreamerV3](#animal-ai-w-dreamerv3)

## Animal-AI w/ Stable Baselines3

Many existing tools for reinforcement learning (such as StableBaselines3) use specific frameworks to wrap the environment and handle the interactions between the environment and the agent. To help with this we provide a Unity to Gymnasium wrapper `AnimalAIGymnasiumWrapper` which converts the regular animal ai environment into a Gymnasium environment that these tools accept.


```python
# Import the necessary environment wrappers.
import animalai
import animalai.envs.environment
from animalai.wrappers.animalai_gymnasium import AnimalAIGymnasiumWrapper
import stable_baselines3

env = animalai.envs.environment.AnimalAIEnvironment(...)

# Wrap with the gymnasium wrapper
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

## Multiple Envs

To scale up the training even further it is possible to create multiple environments in parallel and have agents interact with each of them, yielding significant speedups. For this purpose Gymnasium provides a specific environment class `gymnasium.vector.VectorEnv`, it is possible to create one yourself and fill it with environments however we provide a helper method `make_animalai_vec_env` which we recommend using as there are some edge cases, such as spawning multiple environments in windows needs to be done sequentially, which the helper method handles for you.

```python
from animalai.wrappers import make_animalai_vec_env

num_envs = 4
venv = make_animalai_vec_env(
        num_envs,
        vectorization_mode="async",
        base_port=5005,
        worker_id_start=0,
        arenas_configurations="./arenas/benchmark_config.yaml",
    )
for _ in range(10000):
    venv.step(venv.action_space.sample())
venv.close()
```

## Animal-AI w/ DreamerV3

There is a template repository for using AnimalAI with DreamerV3 [here](https://github.com/Kinds-of-Intelligence-CFI/dreamerv3-animalai).
