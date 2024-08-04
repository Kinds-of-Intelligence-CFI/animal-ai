# Animal-AI w/ RL Libraries

## Animal-AI w/ Stable Baselines3

[Stable Baselines3](https://stable-baselines3.readthedocs.io/en/master/) works with the [Gymnasium](https://gymnasium.farama.org/) interface, while Animal-AI uses an older (<0.26) [Gym](https://github.com/openai/gym/releases/tag/v0.21.0) interface ([compatibility notes](https://gymnasium.farama.org/content/migration-guide/)).

Stable Baselines3 will automatically convert between the two interfaces using [Shimmy](https://shimmy.farama.org/), which needs to be installed separately.

Install your dependencies `pip install animalai stable-baselines3 shimmy` , and use following code:

```python
# Import the necessary environment wrappers.
import animalai
import animalai.envs.environment
import mlagents_envs # Provided by animalai
import mlagents_envs.envs.unity_gym_env
import stable_baselines3

env = animalai.envs.environment.AnimalAIEnvironment(...)

# Make it compatible with legacy Gym v0.21 API
env = mlagents_envs.envs.unity_gym_env.UnityToGymWrapper(
    env,
    uint8_visual=True,
    flatten_branched=True,  # Necessary if the agent doesn't support MultiDiscrete action space.
)

# Stable Baselines3 A2C model
# Will automatically use Shimmy to convert the legacy Gym v0.21 API to the Gymnasium API
model = stable_baselines3.A2C(
    "MlpPolicy",
    env,  # type: ignore
    device="cpu",
    verbose=1,
)
model.learn(total_timesteps=10_000)
```

See [here](https://github.com/Kinds-of-Intelligence-CFI/animal-ai-stablebaselines3) for a complete example of using Animal-AI with Stable Baselines3.

## Animal-AI w/ DreamerV3

There is a template repository for using AnimalAI with DreamerV3 [here](https://github.com/Kinds-of-Intelligence-CFI/dreamerv3-animalai).
