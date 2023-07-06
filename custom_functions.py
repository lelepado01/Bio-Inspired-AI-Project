import random
import numpy as np

from evolutionary_algorithm import EA_Config


def random_demo(env, render=False, episodes=1):
    """Runs an env object with random actions."""
    total_reward = 0
    completed_episodes = 0
    best_reward = 0

    while completed_episodes < episodes:
        env.reset()
        for agent in env.agent_iter():
            if render:
                env.render()

            obs, reward, termination, truncation, _ = env.last()
            total_reward += reward

            if reward > best_reward:
                best_reward = reward
            
            if termination or truncation:
                action = None
            elif isinstance(obs, dict) and "action_mask" in obs:
                action = random.choice(np.flatnonzero(obs["action_mask"]))
            else:
                action = env.action_space(agent).sample()
            env.step(action)

        completed_episodes += 1
        
    if render:
        env.close()

    if EA_Config.DEBUG:
        print("Average total reward", total_reward / episodes)

    return total_reward, best_reward


def average_total_reward(env, max_episodes=100, max_steps=10000000000):
    """Calculates the average total reward over the episodes.

    Runs an env object with random actions until either max_episodes or
    max_steps is reached.
    Reward is summed across all agents, making it unsuited for use in zero-sum
    games.
    """
    total_reward = 0
    total_steps = 0
    num_episodes = 0
    best_reward = 0

    for episode in range(max_episodes):
        if EA_Config.DEBUG:
            print("Episode", episode)
        if total_steps >= max_steps:
            break

        env.reset()
        for agent in env.agent_iter():
            obs, reward, termination, truncation, _ = env.last(observe=False)
            total_reward += reward
            total_steps += 1

            if reward > best_reward:
                best_reward = reward


            if termination or truncation:
                action = None
            elif isinstance(obs, dict) and "action_mask" in obs:
                action = random.choice(np.flatnonzero(obs["action_mask"]))
            else:
                action = env.action_space(agent).sample()
            env.step(action)

        num_episodes = episode + 1
    
    if EA_Config.DEBUG:
        print("Average total reward", total_reward / num_episodes)

    return total_reward / num_episodes
