import math
import numpy as np
from gymnasium.utils import EzPickle
from pettingzoo.utils.conversions import parallel_to_aec_wrapper

import magent2
from magent2.environments.magent_env import magent_parallel_env, make_env

from evolutionary_algorithm import EA_Config, FormationType

default_map_size = 45
max_cycles_default = 1000
KILL_REWARD = 5
minimap_mode_default = False
default_reward_args = dict(
    step_reward=-0.005,
    dead_penalty=-0.1,
    attack_penalty=-0.1,
    attack_opponent_reward=0.2,
)


def parallel_env(
    map_size=default_map_size,
    max_cycles=max_cycles_default,
    minimap_mode=minimap_mode_default,
    extra_features=False,
    render_mode=None,
    seed=None,
    env_data=None,
    **reward_args
):
    env_reward_args = dict(**default_reward_args)
    env_reward_args.update(reward_args)
    return _parallel_env(
        map_size,
        minimap_mode,
        env_reward_args,
        max_cycles,
        extra_features,
        render_mode,
        seed,
        env_data,
    )

def raw_env(
    map_size=default_map_size,
    max_cycles=max_cycles_default,
    minimap_mode=minimap_mode_default,
    env_data=None,
    extra_features=False,
    render_mode=None,
    seed=None,
    **reward_args
):
    return parallel_to_aec_wrapper(
        parallel_env(
            map_size,
            max_cycles,
            minimap_mode,
            extra_features,
            render_mode=render_mode,
            seed=seed,
            env_data=env_data,
            **reward_args
        )
    )

env = make_env(raw_env)

def get_config(
    map_size,
    minimap_mode,
    seed,
    env_data,
    step_reward,
    dead_penalty,
    attack_penalty,
    attack_opponent_reward,
):
    gw = magent2.gridworld
    cfg = gw.Config()

    cfg.set({"map_width": map_size, "map_height": map_size})
    cfg.set({"minimap_mode": minimap_mode})

    cfg.set({"embedding_size": 10})
    if seed is not None:
        cfg.set({"seed": seed})

    options = {
        "width": 1,
        "length": 1,
        "hp": 10,
        "speed": 1,
        "view_range": gw.CircleRange(6),
        "attack_range": gw.CircleRange(1),
        "damage": 2,
        "step_recover": 0.1,
        "attack_in_group": True,
        "step_reward": step_reward,
        "dead_penalty": dead_penalty,
        "attack_penalty": attack_penalty,
    }

    melee = cfg.register_agent_type("melee", options)

    options = {
        "width": 1,
        "length": 1,
        "hp": 3,
        "speed": 2,
        "view_range": gw.CircleRange(6),
        "attack_range": gw.CircleRange(2),
        "damage": 2,
        "step_recover": 0.1,
        "attack_in_group": True,
        "step_reward": step_reward,
        "dead_penalty": dead_penalty,
        "attack_penalty": attack_penalty,
    }

    ranged = cfg.register_agent_type("ranged", options)

    g0_melee = cfg.add_group(melee)
    g0_ranged = cfg.add_group(ranged)
    g1_melee = cfg.add_group(melee)
    g1_ranged = cfg.add_group(ranged)

    arm0_melee = gw.AgentSymbol(g0_melee, index="any")
    arm0_ranged = gw.AgentSymbol(g0_ranged, index="any")
    arm1_melee = gw.AgentSymbol(g1_melee, index="any")
    arm1_ranged = gw.AgentSymbol(g1_ranged, index="any")

    # reward shaping
    cfg.add_reward_rule(
        gw.Event(arm0_melee, "attack", arm1_melee),
        receiver=arm0_melee,
        value=attack_opponent_reward,
    )
    cfg.add_reward_rule(
        gw.Event(arm0_melee, "attack", arm1_ranged),
        receiver=arm0_melee,
        value=attack_opponent_reward,
    )
    cfg.add_reward_rule(
        gw.Event(arm0_ranged, "attack", arm1_melee),
        receiver=arm0_ranged,
        value=attack_opponent_reward,
    )
    cfg.add_reward_rule(
        gw.Event(arm0_ranged, "attack", arm1_ranged),
        receiver=arm0_ranged,
        value=attack_opponent_reward,
    )

    cfg.add_reward_rule(
        gw.Event(arm1_melee, "attack", arm0_melee),
        receiver=arm1_melee,
        value=attack_opponent_reward,
    )
    cfg.add_reward_rule(
        gw.Event(arm1_ranged, "attack", arm0_melee),
        receiver=arm1_ranged,
        value=attack_opponent_reward,
    )
    cfg.add_reward_rule(
        gw.Event(arm1_melee, "attack", arm0_ranged),
        receiver=arm1_melee,
        value=attack_opponent_reward,
    )
    cfg.add_reward_rule(
        gw.Event(arm1_ranged, "attack", arm0_ranged),
        receiver=arm1_ranged,
        value=attack_opponent_reward,
    )

    # kill reward
    cfg.add_reward_rule(
        gw.Event(arm0_melee, "kill", arm1_melee), receiver=arm0_melee, value=KILL_REWARD
    )
    cfg.add_reward_rule(
        gw.Event(arm0_melee, "kill", arm1_ranged), receiver=arm0_melee, value=KILL_REWARD
    )
    cfg.add_reward_rule(
        gw.Event(arm0_ranged, "kill", arm1_melee), receiver=arm0_ranged, value=KILL_REWARD
    )
    cfg.add_reward_rule(
        gw.Event(arm0_ranged, "kill", arm1_ranged), receiver=arm0_ranged, value=KILL_REWARD
    )

    cfg.add_reward_rule(
        gw.Event(arm1_melee, "kill", arm0_melee), receiver=arm1_melee, value=KILL_REWARD
    )
    cfg.add_reward_rule(
        gw.Event(arm1_melee, "kill", arm0_ranged), receiver=arm1_melee, value=KILL_REWARD
    )
    cfg.add_reward_rule(
        gw.Event(arm1_ranged, "kill", arm0_melee), receiver=arm1_ranged, value=KILL_REWARD
    )
    cfg.add_reward_rule(
        gw.Event(arm1_ranged, "kill", arm0_ranged), receiver=arm1_ranged, value=KILL_REWARD
    )

    return cfg

def sanity_check(melee_pos, ranged_pos, width, height):
    for x, y in melee_pos + ranged_pos:
        if not (0 < x < width - 1 and 0 < y < height - 1):
            assert False

def generate_map(env, map_size, handles, env_data):
    width = map_size
    height = map_size

    init_num = map_size * map_size * 0.04

    if EA_Config.INITIAL_FORMATION_TYPE == FormationType.RANDOM:
        env.add_agents(handles[0], method="random", n=env_data.number_of_melee)
        env.add_agents(handles[1], method="random", n=env_data.number_of_ranged)
        env.add_agents(handles[2], method="random", n=env_data.number_of_melee)
        env.add_agents(handles[3], method="random", n=env_data.number_of_ranged)
    elif EA_Config.INITIAL_FORMATION_TYPE == FormationType.DEFAULT:
        gap = 1
        # left
        n = init_num
        side = int(math.sqrt(n)) * 2
        melee_pos = []
        ranged_pos = []
        agent_index = 0
        for x in range(max(width // 2 - gap - side, 1), width // 2 - gap, 2):
            for y in range((height - side) // 2, (height - side) // 2 + side, 2):
                if agent_index % 2 == 0:
                    melee_pos.append([x, y])
                else:
                    ranged_pos.append([x, y])
            agent_index += 1

        max_index = agent_index
        sanity_check(melee_pos, ranged_pos, width, height)
        env.add_agents(handles[0], method="custom", pos=melee_pos)
        env.add_agents(handles[1], method="custom", pos=ranged_pos)

        # right
        n = init_num
        side = int(math.sqrt(n)) * 2
        melee_pos = []
        ranged_pos = []
        agent_index = 0
        for x in range(width // 2 + gap, min(width // 2 + gap + side, height - 1), 2):
            for y in range(
                (height - side) // 2, min((height - side) // 2 + side, height - 1), 2
            ):
                if agent_index % 2 == 0:
                    melee_pos.append([x, y])
                else:
                    ranged_pos.append([x, y])
            agent_index += 1
            if max_index <= agent_index:
                break

        sanity_check(melee_pos, ranged_pos, width, height)
        env.add_agents(handles[2], method="custom", pos=melee_pos)
        env.add_agents(handles[3], method="custom", pos=ranged_pos)

    elif EA_Config.INITIAL_FORMATION_TYPE == FormationType.SQUARE:
        gap = 1
        # left
        side = width // 2
        melee_pos = []
        ranged_pos = []
        agent_index = 0
        current_pos_x = gap
        current_pos_y = gap
        while agent_index < env_data.number_of_melee + env_data.number_of_ranged: 
            if agent_index < env_data.number_of_ranged:
                # aggiungi prima ranged (a sinistra)
                ranged_pos.append([current_pos_x, current_pos_y])
            else:
                # poi i melee (a destra)
                melee_pos.append([current_pos_x, current_pos_y])
            agent_index += 1
            current_pos_y += 2
            if current_pos_y >= side:
                current_pos_y = gap
                current_pos_x += 2

        sanity_check(melee_pos, ranged_pos, width, height)
        env.add_agents(handles[0], method="custom", pos=melee_pos)
        env.add_agents(handles[1], method="custom", pos=ranged_pos)

        # right
        side = width
        melee_pos = []
        ranged_pos = []
        agent_index = 0
        current_pos_x = gap + width // 2
        current_pos_y = gap
        while agent_index < env_data.number_of_melee + env_data.number_of_ranged: 
            if agent_index < env_data.number_of_melee:
                # aggiungi prima melee (a sinistra) (opposto rispetto a prima)
                melee_pos.append([current_pos_x, current_pos_y])
            else:
                # poi i ranged (a destra)
                ranged_pos.append([current_pos_x, current_pos_y])
            agent_index += 1
            current_pos_y += 2
            if current_pos_y >= side:
                current_pos_y = gap + width // 2
                current_pos_x += 2

        sanity_check(melee_pos, ranged_pos, width, height)
        env.add_agents(handles[2], method="custom", pos=melee_pos)
        env.add_agents(handles[3], method="custom", pos=ranged_pos)

class _parallel_env(magent_parallel_env, EzPickle):
    metadata = {
        "render_modes": ["human", "rgb_array"],
        "name": "combined_arms_v6",
        "render_fps": 5,
    }

    def __init__(
        self,
        map_size,
        minimap_mode,
        reward_args,
        max_cycles,
        extra_features,
        render_mode=None,
        seed=None,
        env_data=None,
    ):
        EzPickle.__init__(
            self,
            map_size,
            minimap_mode,
            reward_args,
            max_cycles,
            extra_features,
            render_mode,
            seed,
        )
        assert map_size >= 16, "size of map must be at least 16"
        self.env_data = env_data
        env = magent2.GridWorld(get_config(map_size, minimap_mode, seed, env_data, **reward_args))
        reward_vals = np.array([KILL_REWARD] + list(reward_args.values()))
        reward_range = [
            np.minimum(reward_vals, 0).sum(),
            np.maximum(reward_vals, 0).sum(),
        ]
        names = ["redmelee", "redranged", "bluemele", "blueranged"]
        super().__init__(
            env,
            env.get_handles(),
            names,
            map_size,
            max_cycles,
            reward_range,
            minimap_mode,
            extra_features,
            render_mode,
        )

    def generate_map(self):
        generate_map(self.env, self.map_size, self.handles, self.env_data)
