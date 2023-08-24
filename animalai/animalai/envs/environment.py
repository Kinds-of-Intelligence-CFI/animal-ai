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

    # Default values for configuration parameters of the environment, can be changed if needed
    # Increasing the timescale value for training might speed up the process on powerful machines
    # but take care as the higher the timescale the more likely the physics might break
    WINDOW_WIDTH = PlayTrain(play=1200, train=32)
    WINDOW_HEIGHT = PlayTrain(play=800, train=32)
    QUALITY_LEVEL = PlayTrain(play=1, train=1)
    #TIMESCALE = PlayTrain(play=1, train=300)
    #TARGET_FRAME_RATE = PlayTrain(play=60, train=-1)
    #CAPTURE_FRAME_RATE = PlayTrain(play=60, train=0)
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
            engine_configuration = EngineConfig(
                width=self.WINDOW_WIDTH.play,
                height=self.WINDOW_HEIGHT.play,
                quality_level=self.QUALITY_LEVEL.play,
                # time_scale=self.TIMESCALE.play,
                # target_frame_rate=self.TARGET_FRAME_RATE.play,
                # capture_frame_rate=self.CAPTURE_FRAME_RATE.play,
                time_scale = self.timescale,
                target_frame_rate = self.targetFrameRate,
                capture_frame_rate = self.captureFrameRate
            )
        else:
            engine_configuration = EngineConfig(
                width=self.WINDOW_WIDTH.train,
                height=self.WINDOW_HEIGHT.train,
                quality_level=self.QUALITY_LEVEL.train,
                # time_scale=self.TIMESCALE.train,
                # target_frame_rate=self.TARGET_FRAME_RATE.train,
                # capture_frame_rate=self.CAPTURE_FRAME_RATE.train,
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