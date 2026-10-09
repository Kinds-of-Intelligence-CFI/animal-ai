# Animal-AI with multiple agents

From AAI version 4.4.0 (with version 6.2.0 of the `animalai` Python package), Animal-AI supports playing the game with multiple independently controlled agents present in the scene.

## Adding multiple agents

Additional agents can be added to AAI in the same way as any other item, as shown in the example below:

```YAML
!ArenaConfig
arenas:
  0: !Arena
    timeLimit: 250
    items:
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 10, y: 0, z: 20}
      rotations: [90]
      skins: ["hedgehog"]
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 30, y: 0, z: 20}
      rotations: [270]
      skins: ["panda"]
    - !Item
      name: GoodGoal
      positions:
      - !Vector3 {x: 20, y: 0, z: 30}
      sizes:
      - !Vector3 {x: 1, y: 1, z: 1}
```

## Ending the episode

An area can be configured to complete when any one agent finishes (`episodeEnd: any`), or when all agents finish (`episodeEnd: all` - an agent that finishes early is frozen until the rest catch up). By default, the episode ends when any agent finishes (`episodeEnd: any`). The example snippet below shows how to configure the episode end behaviour:

```YAML
!ArenaConfig
arenas:
  0: !Arena
    timeLimit: 250
    episodeEnd: all
    items:
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 10, y: 0, z: 20}
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 30, y: 0, z: 20}
```

`episodeEnd` is a per-arena parameter, so different arenas in the same file may use different policies.

## CSV Logging

Each agent writes its own [CSV log](/docs/CSVLoggerGuide.md), named `Observations_<timestamp>_agent<k>.csv`, where `k` is the agent's index (its position among the `Agent` items, `0`, `1`, ...).

## FAQs

**How do I know which agent is which on the Python side?**

By its row. `env.get_steps(behavior_name)` returns a `DecisionSteps`/`TerminalSteps` batch containing one row per agent (the behavior name is `AnimalAI?team=0` unless you use teams; see below), and the rows are always in the order of the `Agent` items in the arena's configuration: row 0 is the first `Agent` item, row 1 the second, and so on. This holds in every arena, including after agents sit out an arena and come back. With teams, each team's batch lists that team's agents in the same order.

```python
decision_steps, terminal_steps = env.get_steps("AnimalAI?team=0")
# Row k is the k-th Agent item in the YAML
for k, obs in enumerate(env.get_obs_dicts(decision_steps.obs)):
    print(k, obs["health"], obs["position"])

# One action row per agent, in the same order
from animalai.actions import AAIActions, stack_actions
actions = AAIActions()
env.set_actions(
    "AnimalAI?team=0",
    stack_actions([actions.FORWARDS for _ in range(len(decision_steps))]),
)
```

`decision_steps.obs` is a list of arrays, one per sensor (camera, raycasts, and a health/velocity/position vector), each with one row per agent. `AnimalAIEnvironment.get_obs_dicts(obs)` (plural) regroups these into one dictionary per agent, with keys `camera`, `rays`, `health`, `velocity` and `position`, in row order; `get_obs_dict(obs, agent_index)` (singular) returns just the dictionary for row `agent_index`. `AAIActions(no_agents=N)` builds an action with one row per agent, and `stack_actions([...])` combines several single-agent actions into a single multi-row action to pass to `set_actions`.

Agents in an arena always finish their episodes on the same step, so `decision_steps`/`terminal_steps` for a team never contains a mix of agents mid-episode and agents that just finished.

**What's an `agent_id`?**

Each row of a batch is also labelled with an integer, in `decision_steps.agent_id` (and `terminal_steps.agent_id`). This is ML-Agents' own ID for the agent. We don't recommend using it to tell agents apart; use the row order instead (see above). The ID isn't the agent's `Agent` item index, even though the two often match in the first arena, but it can change (for example, when an agent sits out an arena).

**How do I set the team the agent is on?**

Unity MLAgents includes the concept of teams. Agents that share a team share a single ML-Agents behavior, named `AnimalAI?team=N` (so with no `teams` specified, everything is on team 0 and there is one behavior, `AnimalAI?team=0`, exactly as with a single agent). Set an agent's team with `teams` on its `Agent` item:

```YAML
    - !Item
      name: Agent
      teams: [1]
```

Configurations that use `teams` produce one such behavior per team, so iterate over `env.behavior_specs` rather than assuming a single name.

```python
behavior_names = list(env.behavior_specs.keys())
# e.g. ["AnimalAI?team=0"], or ["AnimalAI?team=0", "AnimalAI?team=1"] with two teams
```

**Can I use the gymnasium wrappers or LLM scaffolds with multiple agents?**

Not yet. The gymnasium wrappers (`UnityToGymnasiumWrapper`, `AnimalAIGymnasiumWrapper`) and the LLM scaffolds (including the Inspect and Kaggle wrappers) only support a single agent, and raise an error if given a multi-agent arena or a configuration with more than one team. Multi-agent support for these is a planned update; if you would like to use them with multiple agents, please get in touch.

**Can humans play with multiple agents?**

Not directly yet. Player mode (keyboard control) supports a single agent, and Animal-AI raises an error if a player-mode arena has more than one `Agent` item. You can still build human play yourself: run with player mode off (`play=False` from Python) and send each agent's actions from Python, based on each player's keyboard input. If you would like to run a human study with multiple players in Animal-AI, please get in touch.

**Can I run a multi-agent study in the browser?**

Not yet. The browser version of Animal-AI only supports a single agent. If you would like to run a multi-agent study in the browser, please get in touch.

**How do operations work with multiple agents?**

A `GoodGoal`, `DataZone` or `SpawnerButton` reacts to whichever agent touches it. Each operation then acts either on that agent or on the arena, which every agent shares: see the "With several agents" notes in the [Operations guide](/docs/Operations-guide.md).

**Can different arenas have different numbers of agents?**

Different arenas in the same configuration file can have different numbers of agents. Agents beyond the number an arena needs simply sit out that arena. Arenas joined by `mergeNextArena` must have the same number of agents, since the episode carries on across them.

When agents sit out the next arena, the first batch after the reset contains only `terminal_steps` rows for the agents leaving (with `interrupted` set to `False`, like an ordinary episode end), and no `decision_steps` rows. The agents still playing appear after one more `env.step()`.