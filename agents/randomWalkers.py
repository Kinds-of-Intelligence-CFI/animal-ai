"""
Copyright © 2023 Konstantinos Voudouris (@kozzy97)

Author: Konstantinos Voudouris
Date: June 2023
Python Version: 3.10.4
Animal-AI Version: 3.0.2

"""


import argparse
import numpy as np
import os
import random
import warnings

from animalai.envs.environment import AnimalAIEnvironment
from collections import deque
from mlagents_envs.envs.unity_gym_env import UnityToGymWrapper

### Random Walker Agent + load config and watch.

"""
Random walker class for the animal-ai environment
"""

class RandomWalker:
    """Implements a random walker with many changeable parameters.
    The key idea is that a certain number of steps is selected (saccade length), the agent goes forwards for that many steps if positive and backwards if negative, and then
    picks a number of steps (angle) to turn for. 
    If the number of steps is negative, they turn left, if positive, they turn right.
    """

    def __init__(self, 
                 max_saccade_length = 10, 
                 max_angle_steps = 5,
                 saccade_distribution = 'fixed', 
                 angle_distribution = 'fixed',
                 saccade_norm_mu = 5, 
                 saccade_norm_sig = 1, 
                 saccade_beta_alpha = 2, 
                 saccade_beta_beta = 2, 
                 saccade_cauchy_mode = 5, 
                 saccade_gamma_kappa = 9, 
                 saccade_gamma_theta = 0.5, 
                 saccade_weibull_alpha = 2, 
                 saccade_poisson_lambda = 5, 
                 angle_fixed_randomise_turn = True,
                 angle_norm_mu = 5,
                 angle_norm_sig = 1,
                 angle_beta_alpha = 2,
                 angle_beta_beta = 2, 
                 angle_cauchy_mode = 5,
                 angle_gamma_kappa = 9,
                 angle_gamma_theta = 0.5,
                 angle_weibull_alpha = 2,
                 angle_poisson_lambda = 5,
                 angle_correlation = 0,
                 backwards_action = False
                 ):
        self.max_saccade_length = max_saccade_length 
        self.max_angle_steps = max_angle_steps
        self.saccade_distribution = saccade_distribution
        self.angle_distribution = angle_distribution
        self.saccade_norm_mu = saccade_norm_mu
        self.saccade_norm_sig = saccade_norm_sig
        self.saccade_beta_alpha = saccade_beta_alpha
        self.saccade_beta_beta = saccade_beta_beta
        self.saccade_cauchy_mode = saccade_cauchy_mode
        self.saccade_gamma_kappa = saccade_gamma_kappa
        self.saccade_gamma_theta = saccade_gamma_theta
        self.saccade_weibull_alpha = saccade_weibull_alpha
        self.saccade_poisson_lambda = saccade_poisson_lambda
        self.angle_fixed_randomise_turn  = angle_fixed_randomise_turn
        self.angle_norm_mu = angle_norm_mu
        self.angle_norm_sig = angle_norm_sig
        self.angle_beta_alpha = angle_beta_alpha
        self.angle_beta_beta = angle_beta_beta 
        self.angle_cauchy_mode = angle_cauchy_mode
        self.angle_gamma_kappa = angle_gamma_kappa
        self.angle_gamma_theta = angle_gamma_theta
        self.angle_weibull_alpha = angle_weibull_alpha
        self.angle_poisson_lambda = angle_poisson_lambda
        self.angle_correlation = angle_correlation
        self.backwards_action = backwards_action

    def get_num_steps_saccade(self):
        
        if self.saccade_distribution == 'fixed':
            num_steps = int(self.max_saccade_length)

        # The while statements remove the possibility of a 0, so that choices between negative and positive are not biased.
           
        elif self.saccade_distribution == 'uniform': 
            num_steps = 0

            while num_steps == 0:
                num_steps = random.randint(0, self.max_saccade_length)

        elif self.saccade_distribution == 'normal':
            num_steps = 0

            while num_steps == 0:
                num_steps = int(np.random.normal(self.saccade_norm_mu, self.saccade_norm_sig))

        elif self.saccade_distribution == 'beta':
            num_steps = 0

            while num_steps == 0:
                num_steps = int(np.random.beta(self.saccade_beta_alpha, self.saccade_beta_beta) * self.max_saccade_length) #rescale it to be bounded by 0 and max_step_length rather than by 0 and 1

        elif self.saccade_distribution == 'cauchy':
            num_steps = 0

            while num_steps == 0:
                num_steps = int(np.random.standard_cauchy() + self.saccade_cauchy_mode)
        
        elif self.saccade_distribution == 'gamma':
            num_steps = 0

            while num_steps == 0:
                num_steps = int(np.random.gamma(self.saccade_gamma_kappa, self.saccade_gamma_theta))
        
        elif self.saccade_distribution == 'weibull':
            num_steps = 0

            while num_steps == 0:
                num_steps = int(np.random.weibull(self.saccade_weibull_alpha) * self.max_saccade_length) #rescale it to be bounded by 0 and max_step_length rather than by 0 and 1
        
        elif self.saccade_distribution == 'poisson':
            num_steps = 0

            while num_steps == 0:
                num_steps = int(np.random.poisson(self.saccade_poisson_lambda))
        
        else:
            raise ValueError("Distribution not recognised.")

        if num_steps > 100:
            warning_string = 'The number of steps chosen is: ' + str(num_steps) + '. Try toggling distribution parameters as your agent might get stuck.'
            warnings.warn(warning_string)

        if self.backwards_action:
            num_steps = abs(num_steps) #make num_steps a positive number so it only goes forwards.

        if num_steps > 0: #Move forwards
            step_list = deque([3]*abs(num_steps)) 
            step_list.append(0) # add in a stationary movement to reduce effect of momentum on next step.
            step_list.append(0) # add in a stationary movement to reduce effect of momentum on next step.
        
        elif num_steps < 0: #Move backwards
            step_list = deque([6]*abs(num_steps))
            step_list.append(0) # add in a stationary movement to reduce effect of momentum on next step.
            step_list.append(0) # add in a stationary movement to reduce effect of momentum on next step.

        else:
            raise ValueError("Saccade length is 0. Try increasing max_saccade_length.")
        
        return step_list
    
    def get_num_steps_turn(self, prev_angle_central_moment):
        
        if self.angle_distribution == 'fixed':
            if self.angle_fixed_randomise_turn:
                right = bool(random.getrandbits(1))
                if right:
                    num_steps = int(self.max_angle_steps)
                else:
                    num_steps = int(self.max_angle_steps * -1)
            else:
                num_steps = self.max_angle_steps
        
        elif self.angle_distribution == 'uniform': 
            num_steps = 0

            while num_steps == 0:
                if self.angle_fixed_randomise_turn:
                    right = bool(random.getrandbits(1))
                    if right:
                        num_steps = random.randint(0, self.max_angle_steps)
                    else:
                        num_steps = random.randint(0, (self.max_angle_steps)) * -1

        elif self.angle_distribution == 'normal':
            central_moment_difference = prev_angle_central_moment - self.angle_norm_mu 
            central_moment_shift = central_moment_difference * self.angle_correlation

            num_steps = 0

            while num_steps == 0:
                num_steps = int(np.random.normal(central_moment_shift, self.angle_norm_sig))

        elif self.angle_distribution == 'beta':
            num_steps = 0

            while num_steps == 0:
                if self.angle_fixed_randomise_turn:
                    right = bool(random.getrandbits(1))
                    if right:
                        num_steps = int(np.random.beta(self.angle_beta_alpha, self.angle_beta_beta) * self.max_angle_steps) #rescale it to be bounded by 0 and max_step_length rather than by 0 and 1
                    else:
                        num_steps = (int(np.random.beta(self.angle_beta_alpha, self.angle_beta_beta) * self.max_angle_steps) * -1) #rescale it to be bounded by 0 and max_step_length rather than by 0 and 1
                

        elif self.angle_distribution == 'cauchy':
            central_moment_difference = prev_angle_central_moment - self.angle_cauchy_mode 
            central_moment_shift = central_moment_difference * self.angle_correlation

            num_steps = 0

            while num_steps == 0:
                num_steps = int(np.random.standard_cauchy() + central_moment_shift) #affine transform of distribution
        
        elif self.angle_distribution == 'gamma':
            num_steps = 0

            while num_steps == 0:
                if self.angle_fixed_randomise_turn:
                    right = bool(random.getrandbits(1))
                    if right:
                        num_steps = int(np.random.gamma(self.angle_gamma_kappa, self.angle_gamma_theta)) 
                    else:
                        num_steps = (int(np.random.gamma(self.angle_gamma_kappa, self.angle_gamma_theta)) * -1) 
        
        elif self.angle_distribution == 'weibull':
            num_steps = 0

            while num_steps == 0:
                if self.angle_fixed_randomise_turn:
                    right = bool(random.getrandbits(1))
                    if right:
                        num_steps = int(np.random.weibull(self.angle_weibull_alpha)) 
                    else:
                        num_steps = (int(np.random.weibull(self.angle_weibull_alpha)) * -1) 
        
        elif self.angle_distribution == 'poisson':
            num_steps = 0
            
            while num_steps == 0:
                if self.angle_fixed_randomise_turn:
                    right = bool(random.getrandbits(1))
                    if right:
                        num_steps = int(np.random.poisson(self.angle_poisson_lambda)) #
                    else:
                        num_steps = (int(np.random.poisson(self.angle_poisson_lambda)) * -1) 

            while num_steps == 0:
                num_steps = int(np.random.poisson(self.angle_poisson_lambda))
        
        else:
            raise ValueError("Distribution not recognised.")

        if num_steps > 0: #Turn right
            step_list = deque([1]*abs(num_steps))
        
        elif num_steps < 0: #Turn left
            step_list = deque([2]*abs(num_steps))

        else:
            raise ValueError("Angle turn steps is 0. Try increasing max_angle_steps.")
        
        return step_list, num_steps
    
def watch_random_walker_single_config(configuration_file: str, agent: RandomWalker):
    
    port = 4000 + random.randint(
    0, 1000
    )  # use a random port to avoid problems if a previous version exits slowly
    
    aai_env = AnimalAIEnvironment( 
    inference=True, #Set true when watching the agent
    seed = 123,
    worker_id=random.randint(0, 65500),
    file_name="../env/AnimalAI",
    arenas_configurations=configuration_file,
    base_port=port,
    useCamera=False,
    resolution=36,
    useRayCasts=False,
    )

    env = UnityToGymWrapper(aai_env, uint8_visual=False, allow_multiple_obs=True, flatten_branched=True)

    obs = env.reset()
     
    done = False
    episodeReward = 0
    
    while not done:

        saccade_list = agent.get_num_steps_saccade()
        
        for action in saccade_list:
            
            obs, reward, done, info = env.step(int(action))
            episodeReward += reward
            env.render()
            
            if done:
                print(F"Episode Reward: {episodeReward}")
                obs=env.reset()
                env.close()
                break
        
        if not done:
            if 'num_angle_steps' not in locals() and agent.angle_distribution == 'normal': #if no turns have been done yet and using normal distribution, then set the central moment to be the prespecified normal_mu
                prev_angle_central_moment = agent.angle_norm_mu
            elif 'num_angle_steps' not in locals() and agent.angle_distribution == 'cauchy': #as above
                prev_angle_central_moment = agent.angle_cauchy_mode
            elif 'num_angle_steps' in locals():
                prev_angle_central_moment = num_angle_steps #if turns have been done, then the central moment is whatever number of steps was provided before.
            else:
                prev_angle_central_moment = 0

            angle_list, num_angle_steps = agent.get_num_steps_turn(prev_angle_central_moment)
        
            for action in angle_list:
            
                obs, reward, done, info = env.step(int(action))

                episodeReward += reward

                env.render()
            
                if done:
                    print(F"Episode Reward: {episodeReward}")
                    env.close()
                    break
        
    
        




if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--config_file", 
                        type=str, 
                        help="What config file should be run? Defaults to a random file from the competition folder.")   
    parser.add_argument("--max_saccade_length", 
                        type=int, 
                        help="What is the maximum saccade length you want. This applies to fixed-step walkers (where the walker takes `max_saccade_length` steps before making turning), and walkers that sample saccade length from uniform, beta, and weibull distributions. It provides the upper bound for these distributions, with 0 as the lower bound. Defaults to 10. You can use negative numbers if you want the walker to go backwards rather than forwards.",
                        default = 10)
    parser.add_argument("--max_angle_steps", 
                        type=int, 
                        help="What is the maximum number of steps that the walker will turn for? This applies to fixed-step walkers (where the walker turns for `max_saccade_length` steps before moving forwards/backwards), and walkers that sample angle steps from uniform, beta, and weibull distributions. It provides the upper bound for these distributions, with 0 as the lower bound. Defaults to 5. You can use negative numbers if you want the walker to go backwards rather than forwards.",
                        default = 5)
    parser.add_argument("--saccade_distribution", 
                        type=str, 
                        help = "What is the distribution you want to sample saccade length from? The options are 'fixed', 'uniform', 'normal', 'cauchy', 'gamma', 'weibull', and 'poisson'. Defaults to 'fixed'.",
                        default = 'fixed')
    parser.add_argument("--angle_distribution", 
                        type=str, 
                        help = "What is the distribution you want to sample number of steps to turn from? The options are 'fixed', 'uniform', 'normal', 'cauchy', 'gamma', 'weibull', and 'poisson'. Defaults to 'fixed'.",
                        default = 'fixed')
    parser.add_argument("--angle_fixed_randomise_turn",
                        type=bool,
                        help = "Should a random walker that turns for a fixed number of steps pick at random between left and right? If True, then there is a 0.5 probability of picking left and a 0.5 probability of picking right. This is ignored if `angle_distribution` is anything other than 'fixed'. Defaults to true.",
                        default = True)
    parser.add_argument("--saccade_norm_mu", 
                        type=float, 
                        help = "What is the mean of the normal distribution for saccade length sampling. This is ignored if `saccade_distribution` is anything other than 'normal'. Defaults to 5.",
                        default = 5)
    parser.add_argument("--saccade_norm_sig", 
                        type=float, 
                        help = "What is the standard deviation of the normal distribution for saccade length sampling. This is ignored if `saccade_distribution` is anything other than 'normal'. Defaults to 1.",
                        default = 1)
    parser.add_argument("--angle_norm_mu", 
                        type=float, 
                        help = "What is the mean of the normal distribution for angle step sampling. This is ignored if `angle_distribution` is anything other than 'normal'. Defaults to 5.",
                        default = 5)
    parser.add_argument("--angle_norm_sig", 
                        type=float, 
                        help = "What is the standard deviation of the normal distribution for angle step sampling. This is ignored if `angle_distribution` is anything other than 'normal'. Defaults to 1.",
                        default = 1)
    parser.add_argument("--saccade_beta_alpha", 
                        type=float, 
                        help = "What is the alpha parameter of the beta distribution for saccade length sampling. This is ignored if `saccade_distribution` is anything other than 'beta'. Defaults to 2.",
                        default = 2)
    parser.add_argument("--saccade_beta_beta", 
                        type=float, 
                        help = "What is the beta parameter of the beta distribution for saccade length sampling. This is ignored if `saccade_distribution` is anything other than 'beta'. Defaults to 2.",
                        default = 2)
    parser.add_argument("--angle_beta_alpha", 
                        type=float, 
                        help = "What is the alpha parameter of the beta distribution for angle step sampling. This is ignored if `angle_distribution` is anything other than 'beta'. Defaults to 2.",
                        default = 2)
    parser.add_argument("--angle_beta_beta", 
                        type=float, 
                        help = "What is the beta parameter of the beta distribution for angle step sampling. This is ignored if `angle_distribution` is anything other than 'beta'. Defaults to 2.",
                        default = 2)
    parser.add_argument("--saccade_cauchy_mode", 
                        type=float, 
                        help = "What is the mode of the standard cauchy distribution for saccade length sampling. This is ignored if `saccade_distribution` is anything other than 'cauchy'. Defaults to 5.",
                        default = 5)
    parser.add_argument("--angle_cauchy_mode", 
                        type=float, 
                        help = "What is the mode of the standard cauchy distribution for angle step sampling. This is ignored if `angle_distribution` is anything other than 'cauchy'. Defaults to 5.",
                        default = 5)
    parser.add_argument("--saccade_gamma_kappa", 
                        type=float, 
                        help = "What is the kappa parameter of the gamma distribution for saccade length sampling. This is ignored if `saccade_distribution` is anything other than 'gamma'. Defaults to 9.",
                        default = 9)
    parser.add_argument("--saccade_gamma_theta", 
                        type=float, 
                        help = "What is the theta parameter of the gamma distribution for saccade length sampling. This is ignored if `saccade_distribution` is anything other than 'gamma'. Defaults to 0.5.",
                        default = 0.5)
    parser.add_argument("--angle_gamma_kappa", 
                        type=float, 
                        help = "What is the kappa parameter of the gamma distribution for angle step sampling. This is ignored if `angle_distribution` is anything other than 'gamma'. Defaults to 9.",
                        default = 9)
    parser.add_argument("--angle_gamma_theta", 
                        type=float, 
                        help = "What is the theta parameter of the gamma distribution for angle step sampling. This is ignored if `angle_distribution` is anything other than 'gamma'. Defaults to 0.5.",
                        default = 0.5)
    parser.add_argument("--saccade_weibull_alpha", 
                        type=float, 
                        help = "What is the alpha parameter of the weibull distribution for saccade length sampling. This is ignored if `saccade_distribution` is anything other than 'weibull'. Defaults to 2.",
                        default = 2)
    parser.add_argument("--angle_weibull_alpha", 
                        type=float, 
                        help = "What is the alpha parameter of the weibull distribution for angle step sampling. This is ignored if `angle_distribution` is anything other than 'weibull'. Defaults to 2.",
                        default = 2)
    parser.add_argument("--saccade_poisson_lambda", 
                        type=float, 
                        help = "What is the lambda parameter of the poisson distribution for saccade length sampling. This is ignored if `saccade_distribution` is anything other than 'poisson'. Defaults to 5.",
                        default = 5)
    parser.add_argument("--angle_poisson_lambda", 
                        type=float, 
                        help = "What is the lambda parameter of the poisson distribution for angle step sampling. This is ignored if `angle_distribution` is anything other than 'poisson'. Defaults to 5.",
                        default = 5)
    parser.add_argument("--angle_correlation",
                        type=float,
                        help = "What correlation is there with selecting the turn angle on the current step with the previous turn angle? This only applies at the moment to normal and cauchy distributed angles. Add a value from 0 to 1 and this will push the mass of the distributions towards the value previously chosen. Defaults to 0.",
                        default = 0)
    parser.add_argument("--backwards_action",
                        type=bool,
                        help = "Can the agent go backwards? If `True`, the agent will go symmetrically forwards and backwards. If `False`, the agent will only go forwards. Defaults to `False`.",
                        default = False)
    
    args = parser.parse_args()

    max_saccade_length = args.max_saccade_length
    max_angle_steps = args.max_angle_steps
    saccade_distribution = args.saccade_distribution
    angle_distribution = args.angle_distribution
    saccade_norm_mu = args.saccade_norm_mu 
    saccade_norm_sig = args.saccade_norm_sig 
    saccade_beta_alpha = args.saccade_beta_alpha 
    saccade_beta_beta = args.saccade_beta_beta 
    saccade_cauchy_mode = args.saccade_cauchy_mode 
    saccade_gamma_kappa = args.saccade_gamma_kappa
    saccade_gamma_theta = args.saccade_gamma_theta 
    saccade_weibull_alpha = args.saccade_weibull_alpha
    saccade_poisson_lambda = args.saccade_poisson_lambda 
    angle_fixed_randomise_turn = args.angle_fixed_randomise_turn
    angle_norm_mu = args.angle_norm_mu
    angle_norm_sig = args.angle_norm_sig
    angle_beta_alpha = args.angle_beta_alpha
    angle_beta_beta = args.angle_beta_beta
    angle_cauchy_mode = args.angle_cauchy_mode
    angle_gamma_kappa = args.angle_gamma_kappa
    angle_gamma_theta = args.angle_gamma_theta
    angle_weibull_alpha = args.angle_weibull_alpha
    angle_poisson_lambda = args.angle_poisson_lambda
    angle_correlation = args.angle_correlation
    backwards_action = args.backwards_action


    if args.config_file is not None:
        configuration_file = args.config_file
    else:
        competition_folder = "../configs/competition/"
        configuration_files = os.listdir(competition_folder)
        configuration_random = random.randint(0, len(configuration_files))
        configuration_file = competition_folder + configuration_files[configuration_random]
        print(F"Using configuration file {configuration_file}")

    singleEpisodeRandomWalker = RandomWalker(max_saccade_length = max_saccade_length, 
                 max_angle_steps = max_angle_steps,
                 saccade_distribution = saccade_distribution, 
                 angle_distribution = angle_distribution,
                 saccade_norm_mu = saccade_norm_mu, 
                 saccade_norm_sig = saccade_norm_sig, 
                 saccade_beta_alpha = saccade_beta_alpha, 
                 saccade_beta_beta = saccade_beta_beta, 
                 saccade_cauchy_mode = saccade_cauchy_mode, 
                 saccade_gamma_kappa = saccade_gamma_kappa, 
                 saccade_gamma_theta = saccade_gamma_theta, 
                 saccade_weibull_alpha = saccade_weibull_alpha, 
                 saccade_poisson_lambda = saccade_poisson_lambda, 
                 angle_fixed_randomise_turn = angle_fixed_randomise_turn,
                 angle_norm_mu = angle_norm_mu,
                 angle_norm_sig = angle_norm_sig,
                 angle_beta_alpha = angle_beta_alpha,
                 angle_beta_beta = angle_beta_beta, 
                 angle_cauchy_mode = angle_cauchy_mode,
                 angle_gamma_kappa = angle_gamma_kappa,
                 angle_gamma_theta = angle_gamma_theta,
                 angle_weibull_alpha = angle_weibull_alpha,
                 angle_poisson_lambda = angle_poisson_lambda,
                 angle_correlation = angle_correlation,
                 backwards_action = backwards_action)
    
    watch_random_walker_single_config(configuration_file=configuration_file, agent = singleEpisodeRandomWalker)