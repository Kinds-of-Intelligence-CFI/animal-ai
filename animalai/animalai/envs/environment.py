import uuid
from typing import NamedTuple, Dict, Optional, List
from mlagents_envs.environment import UnityEnvironment
from mlagents_envs.rpc_communicator import UnityTimeOutException
from mlagents_envs.side_channel.raw_bytes_channel import RawBytesChannel
from mlagents_envs.side_channel.side_channel import SideChannel
from mlagents_envs.side_channel.engine_configuration_channel import (
    EngineConfig,
    EngineConfigurationChannel,
)

class PlayTrain(NamedTuple):
    play: int
    train: int

class AnimalAIEnvironment(UnityEnvironment):
    """Extends UnityEnvironment with options specific for AnimalAI
    see https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Python-API.md for documentation
    and the animalai observations doc for explanation of the AnimalAI-specific parameters."""

    # Default values for configuration parameters of the environment, can be changed if needed.
    WINDOW_WIDTH = PlayTrain(play=1200, train=32)
    WINDOW_HEIGHT = PlayTrain(play=800, train=32)
    QUALITY_LEVEL = PlayTrain(play=1, train=1)
    ARENA_CONFIG_SC_UUID = "9c36c837-cad5-498a-b675-bc19c9370072"
    YAML_SC_UUID = "20b62eb2-cde3-4f5f-a8e5-af8d9677971d"

    def __init__(
        self,
        additional_args: List[str] = None,
        log_folder: str = "",
        file_name: Optional[str] = None,
        worker_id: int = 0,
        base_port: int = 5005,
        seed: int = 0,
        play: bool = False,
        arenas_configurations: str = "",
        inference: bool = False,
        useCamera: bool = True,
        resolution: int = None,
        grayscale: bool = False,
        useRayCasts: bool = False,
        raysPerSide: int = 2,
        rayMaxDegrees: int = 60,       
        decisionPeriod: int = 3, 
        side_channels: Optional[List[SideChannel]] = None,
        no_graphics: bool = False,
        use_YAML: bool = True,
        timescale: int = 1,
        targetFrameRate: int = 60,
        captureFrameRate: int = 0,
        ):
        """
        Parameters
        ----------
        additional_args : List[str]
            Currently not supported anymore. TODO.
        log_folder : str
            Optional folder to write the Unity Player log file into. Requires absolute path.
        file_name : Optional[str]
            Path to the Unity environment binary.
        worker_id : int
            Offset from base_port. Used for training multiple environments simultaneously.
        base_port : int
            Base port to connect to Unity environment over. worker_id increments over this.
            If no environment is specified (i.e. file_name is None), the DEFAULT_EDITOR_PORT will be used.
        seed : int
            Random seed used for the environment.
        play : bool
            Whether to run the Unity simulator in play mode.
        arenas_configurations : str
            Path to the YAML file containing the arena configurations.
        inference : bool
            Sets the window size to the same as play mode to allow observing the agent.
        useCamera : bool
            Whether to use the camera observations.
        resolution : int
            Resolution of the camera observations.
        grayscale : bool
            Whether to use grayscale camera observations.
        useRayCasts : bool
            Whether to use the raycast observations.
        raysPerSide : int
            Number of rays per side.
        rayMaxDegrees : int
            Maximum degrees of the raycast observations.
        decisionPeriod : int
            [DEPRECATED] Number of steps to take before the agent gets a decision. TODO.
        side_channels : Optional[List[SideChannel]]
            Additional side channel for no-rl communication with Unity.
        no_graphics : bool
            Whether to run the Unity simulator in no-graphics mode. 
            Not compatible with useCamera, as all observations will empty.
        use_YAML :
            [DEPRECATED]. TODO.
        timescale : int
            Defines the multiplier for the deltatime in the simulation. Default is 1.
            If set to a higher value, time will pass faster in the simulation
            and might speed of training but the physics might break.
            A value of 1 is real time, 2 is double speed, 0.5 is half speed.
            WARNING: Make sure that the observations your agent can receive 
            per second is adequate for the set timescale.
            For example, with an average observations per second 60, a timescale
            of 60 will cause your agent to only observe 1 frame per in-simulation second.
            Especially important with time-sensitive environments, 
            e.g. decaying or growing goals, falling or rolling objects...
        targetFrameRate : int
            Instructs simulation to try to render at a specified frame rate. 
            A value of -1 will attempt to render as fast as possible, recommended
            when timescale is set to a value higher than 1.
        captureFrameRate : int
            Instructs the simulation to consider time between updates to always be constant, regardless of the actual frame rate.
        """

        self.obsdict = {
            "camera": [],
            "rays": [],
            "health": [],
            "velocity": [],
            "position": [],
        }
        self.useCamera = useCamera
        self.useRayCasts = useRayCasts
        args = self.executable_args( 
            play,
            useCamera, 
            resolution, 
            grayscale, 
            useRayCasts, 
            raysPerSide, 
            rayMaxDegrees, 
            decisionPeriod)
        self.play = play
        self.inference = inference
        self.timeout = 10 if play else 60
        self.side_channels = side_channels if side_channels else []
        self.arenas_parameters_side_channel = None
        self.use_YAML = use_YAML
        self.timescale = timescale
        self.captureFrameRate = captureFrameRate
        self.targetFrameRate = targetFrameRate

        self.configure_side_channels(self.side_channels)

        super().__init__(
            file_name=file_name,
            worker_id=worker_id,
            base_port=base_port,
            seed=seed,
            no_graphics=no_graphics,
            timeout_wait=self.timeout,
            additional_args=args,
            side_channels=self.side_channels,
            log_folder=log_folder,
        )
        self.reset(arenas_configurations)

    def configure_side_channels(self, side_channels: List[SideChannel]) -> None:

        contains_engine_config_sc = any(
            [isinstance(sc, EngineConfigurationChannel) for sc in side_channels]
        )
        if not contains_engine_config_sc:
            self.side_channels.append(self.create_engine_config_side_channel())
        contains_arena_config_sc = any(
            [sc.channel_id == self.ARENA_CONFIG_SC_UUID for sc in side_channels]
        )
        if not contains_arena_config_sc:
            self.arenas_parameters_side_channel = RawBytesChannel(
                channel_id=uuid.UUID(self.ARENA_CONFIG_SC_UUID)
            )
            self.side_channels.append(self.arenas_parameters_side_channel)

    def create_engine_config_side_channel(self) -> EngineConfigurationChannel:
        if self.play or self.inference:
            width, height, quality_level = (
                self.WINDOW_WIDTH.play,
                self.WINDOW_HEIGHT.play,
                self.QUALITY_LEVEL.play,
            )
        else:
            width, height, quality_level = (
                self.WINDOW_WIDTH.train,
                self.WINDOW_HEIGHT.train,
                self.QUALITY_LEVEL.train,
            )
        engine_configuration = EngineConfig(
            width=width,
            height=height,
            quality_level=quality_level,
            time_scale = self.timescale,
            target_frame_rate = self.targetFrameRate,
            capture_frame_rate = self.captureFrameRate
        )
        engine_configuration_channel = EngineConfigurationChannel()
        engine_configuration_channel.set_configuration(engine_configuration)
        return engine_configuration_channel

    def get_obs_dict(self, obs) -> Dict:
        """Parse the observation:
        input: the observation directly from AAI
        output: a dictionary with keys: ["camera", "rays", "health", "velocity", "position"] """
        intrinsicobs = 0
        if(self.useCamera):
            intrinsicobs = intrinsicobs+1
            self.obsdict["camera"] = obs[0][0]
            if(self.useRayCasts):
                intrinsicobs = intrinsicobs+1
                self.obsdict["rays"] = obs[1][0]
        elif(self.useRayCasts):
            intrinsicobs = intrinsicobs+1
            self.obsdict["rays"] = obs[0][0]
        
        self.obsdict["health"] = obs[intrinsicobs][0][0]
        self.obsdict["velocity"] = obs[intrinsicobs][0][1:4]
        self.obsdict["position"] = obs[intrinsicobs][0][4:7]
        return self.obsdict

    def reset(self, arenas_configurations="") -> None:
        if arenas_configurations != "":
            f = open(arenas_configurations, "r")
            d = f.read()
            f.close()
            self.arenas_parameters_side_channel.send_raw_data(bytearray(d, encoding="utf-8"))
        try:
            super().reset()
        except UnityTimeOutException as timeoutException:
            if self.play:
                pass
            else:
                raise timeoutException

    @staticmethod
    def executable_args(
        play: bool = False,
        useCamera: bool = True,
        resolution: int = 150,
        grayscale: bool = False,
        useRayCasts: bool = True,
        raysPerSide: int = 2,
        rayMaxDegrees: int = 60,
        decisionPeriod: int = 3,
    ) -> List[str]:
        args = ["--playerMode"]
        if play:
            args.append("1")
        else:
            args.append("0")
        if useCamera:
            args.append("--useCamera")
        if resolution:
            args.append("--resolution")
            args.append(str(resolution))
        if grayscale:
            args.append("--grayscale")
        if useRayCasts:
            args.append("--useRayCasts")
        args.append("--raysPerSide")
        args.append(str(raysPerSide))
        args.append("--rayMaxDegrees")
        args.append(str(rayMaxDegrees))
        args.append("--decisionPeriod")
        args.append(str(decisionPeriod))
        return args