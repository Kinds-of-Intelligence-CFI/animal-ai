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
import sys
import warnings

from animalai.envs.environment import AnimalAIEnvironment
from collections import deque
from gym_unity.envs import UnityToGymWrapper
from scipy.special import softmax

### Random Action Agent + load config and watch.

"""
Random action class for the animal-ai environment
"""

class RandomActionAgent:
    """Implements a random walker with many changeable parameters"""

    def __init__(self, max_step_length = 10, step_length_distribution = 'fixed', norm_mu = 5, norm_sig = 1, beta_alpha = 2, beta_beta = 2, cauchy_mode = 5, gamma_kappa = 9, gamma_theta = 0.5, weibull_alpha = 2, poisson_lambda = 5, action_biases = [1,1,1,1,1,1,1,1,1], prev_step_bias = 0, remove_prev_step = False):
        self.max_step_length = max_step_length 
        self.step_length_distribution = step_length_distribution
        self.norm_mu = norm_mu
        self.norm_sig = norm_sig
        self.beta_alpha = beta_alpha
        self.beta_beta = beta_beta
        self.cauchy_mode = cauchy_mode
        self.gamma_kappa = gamma_kappa
        self.gamma_theta = gamma_theta
        self.weibull_alpha = weibull_alpha
        self.poisson_lambda = poisson_lambda
        self.action_biases = action_biases
        self.prev_step_bias = prev_step_bias
        self.remove_prev_step = remove_prev_step

    def get_num_steps(self, prev_step: int):
        
        if self.step_length_distribution == 'fixed':
            num_steps = self.max_step_length
        
        elif self.step_length_distribution == 'uniform': 
            num_steps = random.randint(0, self.max_step_length)

        elif self.step_length_distribution == 'normal':
            num_steps = -1
            while num_steps <= 0: # to make sure that num_steps is always a natural number
                num_steps = int(np.random.normal(self.norm_mu, self.norm_sig))

        elif self.step_length_distribution == 'beta':
            num_steps = int(np.random.beta(self.beta_alpha, self.beta_beta) * self.max_step_length) #rescale it to be bounded by 0 and max_step_length rather than by 0 and 1

        elif self.step_length_distribution == 'cauchy':
            num_steps = -1
            while num_steps < 0:
                num_steps = int(np.random.standard_cauchy() + self.cauchy_mode)
        
        elif self.step_length_distribution == 'gamma':
            num_steps = -1
            while num_steps < 0:
                num_steps = int(np.random.gamma(self.gamma_kappa, self.gamma_theta))
        
        elif self.step_length_distribution == 'weibull':
            num_steps = int(np.random.weibull(self.weibull_alpha) * self.max_step_length) #rescale it to be bounded by 0 and max_step_length rather than by 0 and 1
        
        elif self.step_length_distribution == 'poisson':
            num_steps = int(np.random.poisson(self.poisson_lambda))
        
        else:
            raise ValueError("Distribution not recognised.")

        if num_steps > 100:
            warning_string = 'The number of steps chosen is: ' + str(num_steps) + '. Try toggling distribution parameters as your agent might get stuck.'
            warnings.warn(warning_string)

        
        step_list = deque([prev_step]*num_steps)
        return step_list

    def get_new_action(self, prev_step: int):

        """
        Provide a vector of 9 real values, one for each action, which is then softmaxed to provide the probability of selecting that action. Relative differences between the values is what is important. 

        Provide an initial probability of selecting the previous step again. If that action is not selected, then the next step is picked according to the softmaxed action biases. The previous action can be removed
        from the softmaxed biases (by continually sampling until an action is picked that is not the previous action), by changing `remove_prev_step` to `True`.
        """

        assert(len(self.action_biases) == 9), "You must provide biases for all nine (9) actions. A uniform distribution is [1,1,1,1,1,1,1,1,1]"

        assert(self.prev_step_bias >= 0 and self.prev_step_bias <= 1), "The bias towards the previous action must be a scalar value between 0 and 1."

        
        action_is_prev_step = np.random.choice(a = [False,True], size = 1, p = [(1-self.prev_step_bias), self.prev_step_bias]) # should the action be the previous step?

        if action_is_prev_step:
            action = prev_step
        else:
            if self.remove_prev_step:
                action_biases_softmax = softmax(self.action_biases)
                action = prev_step
                while action == prev_step:
                    action = np.random.choice(a = [0,1,2,3,4,5,6,7,8], size = 1, p = action_biases_softmax)
            else:
                action_biases_softmax = softmax(self.action_biases)
                action = np.random.choice(a = [0,1,2,3,4,5,6,7,8], size = 1, p = action_biases_softmax)
        
        action = int(action)

        return action
    
def watch_random_action_agent_single_config(configuration_file: str, agent: RandomActionAgent):
    
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
    initialActionAgent = agent
    initialActionAgent.prev_step_bias = 0 #select a random action according to the biases. There is no previous step bias as there is no previous step at the start of an episode!

    previous_action = initialActionAgent.get_new_action(prev_step=0) 

    while not done:

        step_list = agent.get_num_steps(prev_step = previous_action)
        
        for action in step_list:
            
            obs, reward, done, info = env.step(int(action))
            episodeReward += reward
            env.render()

            previous_action = action

            if done:
                print(F"Episode Reward: {episodeReward}")
                obs=env.reset()
                env.close()
                break

        ## get new action for one step before repeating while loop.

        action = agent.get_new_action(prev_step = previous_action)
        
        obs, reward, done, info = env.step(int(action))
        
        episodeReward += reward
        env.render()

        previous_action = action

        if done:
            print(F"Episode Reward: {episodeReward}")
            obs=env.reset()
            env.close()
            break #to be sure.

        
    
        




if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--config_file", 
                        type=str, 
                        help="What config file should be run? Defaults to a random file from the competition folder.")
    
    parser.add_argument("--max_step_length", 
                        type=int, 
                        help="What is the maximum step length you want. This applies to fixed-step walkers (where the walker takes `max_step_length` steps before making another choice), and walkers that sample step length from uniform, beta, and weibull distributions. It provides the upper bound for these distributions, with 0 as the lower bound. Defaults to 10.",
                        default = 10)
    parser.add_argument("--step_length_distribution", 
                        type=str, 
                        help = "What is the distribution you want to sample step length from? The options are 'fixed', 'uniform', 'normal', 'cauchy', 'gamma', 'weibull', and 'poisson'. Defaults to 'fixed'.",
                        default = 'fixed')
    parser.add_argument("--norm_mu", 
                        type=float, 
                        help = "What is the mean of the normal distribution for step length sampling. This is ignored if `step_length_distribution` is anything other than 'normal'. Defaults to 5.",
                        default = 5)
    parser.add_argument("--norm_sig", 
                        type=float, 
                        help = "What is the standard deviation of the normal distribution for step length sampling. This is ignored if `step_length_distribution` is anything other than 'normal'. Defaults to 1.",
                        default = 1)
    parser.add_argument("--beta_alpha", 
                        type=float, 
                        help = "What is the alpha parameter of the beta distribution for step length sampling. This is ignored if `step_length_distribution` is anything other than 'beta'. Defaults to 2.",
                        default = 2)
    parser.add_argument("--beta_beta", 
                        type=float, 
                        help = "What is the beta parameter of the beta distribution for step length sampling. This is ignored if `step_length_distribution` is anything other than 'beta'. Defaults to 2.",
                        default = 2)
    parser.add_argument("--cauchy_mode", 
                        type=float, 
                        help = "What is the mode of the standard cauchy distribution for step length sampling. This is ignored if `step_length_distribution` is anything other than 'cauchy'. Defaults to 5.",
                        default = 5)
    parser.add_argument("--gamma_kappa", 
                        type=float, 
                        help = "What is the kappa parameter of the gamma distribution for step length sampling. This is ignored if `step_length_distribution` is anything other than 'gamma'. Defaults to 9.",
                        default = 9)
    parser.add_argument("--gamma_theta", 
                        type=float, 
                        help = "What is the theta parameter of the gamma distribution for step length sampling. This is ignored if `step_length_distribution` is anything other than 'gamma'. Defaults to 0.5.",
                        default = 0.5)
    parser.add_argument("--weibull_alpha", 
                        type=float, 
                        help = "What is the alpha parameter of the weibull distribution for step length sampling. This is ignored if `step_length_distribution` is anything other than 'weibull'. Defaults to 2.",
                        default = 2)
    parser.add_argument("--poisson_lambda", 
                        type=float, 
                        help = "What is the lambda parameter of the poisson distribution for step length sampling. This is ignored if `step_length_distribution` is anything other than 'poisson'. Defaults to 5.",
                        default = 5)
    parser.add_argument("--action_biases", 
                    nargs='+',
                    type=float,
                    help="Provide a series of 9 real values, one for each action, which is then softmaxed to provide the probability of selecting that action. Relative differences between the values is what is important. 0=stationary-action, 1=right-turn, 2=left-turn, 3=forwards, 4=forwards-right, 5=forwards-left, 6=backwards, 7=backwards-left, 8=backwards-right. Defaults to a value of 1 for all actions.",
                    default=[1, 1, 1, 1, 1, 1, 1, 1, 1])
    parser.add_argument("--prev_step_bias",
                      type=float,
                      help="Provide the initial probability that the previous action will be selected again at a choice point. Defaults to 0.",
                      default=0)
    parser.add_argument("--remove_prev_step",
                       type=bool,
                       help="Should the previous action be removed when selecting the next action. If True and `prev_step_bias` is 0, then a new action is selected that is not the old action. If True and there is some bias, then the bias is applied first, and if the previous step is not reselected, then the next action is guaranteed to not include the previous action. Defaults to False",
                       default=False)
    
    args = parser.parse_args()

    max_step_length = args.max_step_length 
    step_length_distribution = args.step_length_distribution
    norm_mu = args.norm_mu
    norm_sig = args.norm_sig
    beta_alpha = args.beta_alpha
    beta_beta = args.beta_beta
    cauchy_mode = args.cauchy_mode
    gamma_kappa = args.gamma_kappa
    gamma_theta = args.gamma_theta
    weibull_alpha = args.weibull_alpha
    poisson_lambda = args.poisson_lambda
    action_biases = np.array(args.action_biases)
    prev_step_bias = args.prev_step_bias
    remove_prev_step = args.remove_prev_step

    if args.config_file is not None:
        configuration_file = args.config_file
    else:
        competition_folder = "../configs/competition/"
        configuration_files = os.listdir(competition_folder)
        configuration_random = random.randint(0, len(configuration_files))
        configuration_file = competition_folder + configuration_files[configuration_random]
        print(F"Using configuration file {configuration_file}")

    singleEpisodeRandomaActionAgent = RandomActionAgent(max_step_length=max_step_length,
                                             step_length_distribution=step_length_distribution,
                                             norm_mu=norm_mu,
                                             norm_sig=norm_sig,
                                             beta_alpha=beta_alpha,
                                             beta_beta=beta_beta,
                                             cauchy_mode=cauchy_mode,
                                             gamma_kappa=gamma_kappa,
                                             gamma_theta=gamma_theta,
                                             weibull_alpha = weibull_alpha,
                                             poisson_lambda=poisson_lambda,
                                             action_biases=action_biases,
                                             prev_step_bias=prev_step_bias,
                                             remove_prev_step=remove_prev_step)
    
    watch_random_action_agent_single_config(configuration_file=configuration_file, agent = singleEpisodeRandomaActionAgent)