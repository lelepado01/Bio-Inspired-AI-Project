from pettingzoo.classic import connect_four_v3
from pettingzoo.utils import random_demo
import rock_paper_scissors

env = rock_paper_scissors.env(render_mode='human')
random_demo(env, render=False, episodes=10)

