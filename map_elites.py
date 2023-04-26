import numpy as np
import random
from pettingzoo.utils import random_demo

import custom_combined_arms
from environment_data import EnvironmentData

NUMBER_OF_EPISODES = 1
NUMBER_OF_EPOCHS = 10

# TODO: questi sono parametri dell'algoritmo, 
#   vanno spostati nella classe e decisi nel main
ALLOW_MUTATION = True
ALLOW_CROSSOVER = True

class MAP_Elites: 
    def __init__(self):
        # TODO: questi parametri vanno fatti meglio
        self.current_epoch = 0
        self.num_dimensions = 1
        self.num_cells = 5
        # range di valori per EnvironmentData,
        # dicono che non possiamo avere 51 melee se ci sono al max 
        # 50 unità totali per team
        # TODO: integrare questo nella classe EnvironmentData e non qui
        self.dimension_range = (0, 10)

        # partiamo con una griglia semplice con una sola dimensione 
        # la griglia contiene coppie (EnvironmentData, fitness)
        # dove enviroment data è il "genotipo" (ex. 5 melee e 5 ranged)
        # TODO: da espandere a più dimensioni (credo almeno due)
        self.solution_space_grid = np.empty(self.num_cells, dtype=object)

        print("--- Initializing grid...")
        self.init_grid()

    def init_grid(self): 
        for i in range(self.num_cells):
            # Per ogni item nella griglia inizializzaimo una soluzjone random
            low, high = self.dimension_range
            solution = np.random.uniform(low=low, high=high, size=self.num_dimensions)

            envdata = EnvironmentData(50)

            # e passiamo questa soluzione nel giochino per vedere come performa, 
            # restituisce direttamente il total_reward, quello che dobbiamo massimizzare
            fitness = self.fitness_function(envdata)
            self.solution_space_grid[i] = (envdata, fitness)

    def run(self): 
        # Mutate and repeat until stopping criteria met
        # nel nostro caso per adesso è un numero di epoche arbitrario (100)
        # TODO: aggiungere altri stopping criteria, 
        #   come ad esempio se nessuna soluzione migliora per un tot di epoche
        print("--- Running MAP...")
        while not self.stopping_criteria_met():
            print(f"Running: {self.current_epoch}")
            print("Grid is: ")
            print(self.solution_space_grid)
            # Select a cell in the grid based on some selection criteria
            cell_index = self.select_cell()
            # Mutate the solution in the selected cell
            mutated_solution = self.mutation_and_crossover(cell_index)
            # Evaluate the fitness of the mutated solution
            fitness = self.fitness_function(mutated_solution)
            # Aggiorniamo la soluzione nella griglia 
            # solo se la fitness è migliore
            if fitness > self.solution_space_grid[cell_index][1]:
                self.solution_space_grid[cell_index] = (mutated_solution, fitness)

            self.current_epoch += 1

    def fitness_function(self, solution):
        # execute environment with current ratio of melee and ranged units
        print("Evaluating enviroment...")
        env = custom_combined_arms.env(render_mode='human')
        fitness_score = random_demo(env, render=False, episodes=NUMBER_OF_EPISODES)

        return fitness_score

    def select_cell(self):
        # select random cell
        return random.randint(0, len(self.solution_space_grid)-1)

    def mutation_and_crossover(self, cell_index):
        env_data = self.solution_space_grid[cell_index][0]
        
        if ALLOW_MUTATION:
            env_data.mutate()
        if ALLOW_CROSSOVER:
            other_cell_index = self.select_cell()
            other_env_data = self.solution_space_grid[other_cell_index][0]
            env_data.crossover(other_env_data)

        return env_data

    def stopping_criteria_met(self):
        # Check if stopping criteria met
        return self.current_epoch > NUMBER_OF_EPOCHS
    
    def get_best_solutions(self):
        # Select the best solutions from each cell in the grid
        best_solutions = [cell[0] for cell in self.solution_space_grid if cell is not None]
        return best_solutions