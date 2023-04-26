import numpy as np
import random
import custom_combined_arms
from pettingzoo.utils import random_demo

NUMBER_OF_EPISODES = 10

class EnvironmentData:
    def __init__(self, total_units):
        self.melee = total_units * 0.5
        self.ranged = total_units - self.melee

    def mutate(self): 
        pass

    def crossover(self, other):
        pass


def fitness_function(solution):
    # execute environment with current ratio of melee and ranged units
    env = custom_combined_arms.env(render_mode='human')
    fitness_score = random_demo(env, render=False, episodes=NUMBER_OF_EPISODES)

    return fitness_score

def select_cell(grid):
    # select random cell
    cell_index = random.randint(0, len(grid))
    return cell_index

def mutate(solution):
    # Mutate the solution
    return mutated_solution

def stopping_criteria_met():
    # Check if stopping criteria met
    return False

# Set the number of dimensions and the range of values for each dimension
num_dimensions = 2
dimension_ranges = [(0, 10), (0, 10)]

# Set the number of cells in the grid
num_cells = 100

# Initialize the grid
grid = np.empty(num_cells, dtype=object)

# Generate and evaluate solutions
for i in range(num_cells):
    # Generate a random solution in the parameter space
    solution = np.random.uniform(low=dimension_ranges[0][0], high=dimension_ranges[0][1], size=num_dimensions)
    # Evaluate the fitness of the solution
    fitness = fitness_function(solution)
    # Store the solution in the grid
    grid[i] = (solution, fitness)

# Mutate and repeat until stopping criteria met
while not stopping_criteria_met():
    # Select a cell in the grid based on some selection criteria
    cell_index = select_cell(grid)
    # Mutate the solution in the selected cell
    solution = mutate(grid[cell_index][0])
    # Evaluate the fitness of the mutated solution
    fitness = fitness_function(solution)
    # Store the new solution in the grid if it is better than the old solution
    if fitness > grid[cell_index][1]:
        grid[cell_index] = (solution, fitness)

# Select the best solutions from each cell in the grid
best_solutions = [cell[0] for cell in grid if cell is not None]