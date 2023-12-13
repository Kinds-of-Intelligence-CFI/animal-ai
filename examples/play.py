import sys
import random
import os

from animalai.envs.environment import AnimalAIEnvironment

def load_config_and_play(configuration_file: str) -> None:
    """
    Loads a configuration file for a single arena and lets you play manually
    :param configuration_file: str path to the yaml configuration
    :return: None
    """
    env_path = "../env/AnimalAI"
    port = 5005 + random.randint(
        0, 1000
    )  # use a random port to avoid problems if a previous version exits slowly

    print("Initializing AAI environment")
    environment = AnimalAIEnvironment(
        file_name=env_path,
        base_port=port,
        arenas_configurations=configuration_file,
        play=True,
        timescale = 1,
        targetFrameRate = 60,
        captureFrameRate = 0
    )

    # Run the environment until signal to it is lost
    try:
        while environment._process:
            continue
    except KeyboardInterrupt:
        pass
    finally:
        environment.close()


# If an argument is provided then assume it is path to a configuration and use that
# Otherwise load a random competition config.
if __name__ == "__main__":
    if len(sys.argv) > 1:
        configuration_file = sys.argv[1]
    else:
        competition_folder = "../configs/competition/"
        configuration_files = os.listdir(competition_folder)
        configuration_random = random.randint(0, len(configuration_files))
        configuration_file = competition_folder + configuration_files[configuration_random]
        print(F"Using configuration file {configuration_file}")
    
    load_config_and_play(configuration_file=configuration_file)
