import numpy as np
import random

from pettingzoo.utils import random_demo

import custom_combined_arms
from problem_params import ProblemParameters
from environment_data import EnvironmentData
from evolutionary_algorithm import EA_Config, CrossoverSelectionStrategy
from logger import Logger

DEBUG = True

class MAP_Elites: 
    def __init__(self, problem_parameters : ProblemParameters):
        self.current_epoch = 0
        self.logger = Logger("map_elites_log.txt")

        #setting of problem parameters as self
        self.cells_in_grid = problem_parameters.cells_in_grid
        self.number_of_episodes = problem_parameters.number_of_episodes
        self.number_of_epochs = problem_parameters.number_of_epochs

        # partiamo con una griglia semplice con una sola dimensione 
        # la griglia contiene coppie (EnvironmentData, fitness)
        # dove enviroment data è il "genotipo" (ex. 5 melee e 5 ranged)
        # TODO: da espandere a più dimensioni (credo almeno due)
        self.solution_space_grid = np.empty(self.cells_in_grid, dtype=object)

        if DEBUG:
            print("--- Initializing grid...")
        self.init_grid(problem_parameters)

    def init_grid(self, problem_parameters): 
        for i in range(self.cells_in_grid):
            envdata = EnvironmentData(problem_parameters, i)
            # e passiamo questa soluzione nel giochino per vedere come performa, 
            # restituisce direttamente il total_reward, quello che dobbiamo massimizzare
            fitness = self.fitness_function(envdata)
            self.solution_space_grid[i] = (envdata, fitness)

    def run(self): 
        # Mutate and repeat until stopping criteria met
        # nel nostro caso per adesso è un numero di epoche arbitrario (100)
        # TODO: aggiungere altri stopping criteria, 
        #   come ad esempio se nessuna soluzione migliora per un tot di epoche
        if DEBUG:
            print("--- Running MAP...")

        while not self.stopping_criteria_met():
            if DEBUG:
                print(f"Running epoch: {self.current_epoch}")
            # Select a cell in the grid based on some selection criteria
            cell_index = self.select_cell()
            # Mutate the solution in the selected cell
            mutated_solution = self.mutation_and_crossover(cell_index)
            # Evaluate the fitness of the mutated solution
            fitness = self.fitness_function(mutated_solution)
            # Aggiorniamo la soluzione nella griglia 
            # solo se la fitness è migliore
            if fitness > self.solution_space_grid[cell_index][1]:
                if DEBUG: 
                    print(f"New best fitness: {fitness} in cell {cell_index}")
                self.solution_space_grid[cell_index] = (mutated_solution, fitness)

            self.logger.to_plot_2d(self.solution_space_grid)
            self.current_epoch += 1

        self.logger.close()

    def fitness_function(self, env_data):
        if DEBUG:
            print("Evaluating enviroment...")
        # eseguiamo l'environemnt con i parametri passati, 
        # che danno informazioni riguardo a numero di agenti e tipo di agenti
        env = custom_combined_arms.env(env_data=env_data, render_mode='human')
        fitness_score = random_demo(env, render=False, episodes=self.number_of_episodes)

        return fitness_score

    def select_cell(self, cell_index=None):
        if EA_Config.CROSSOVER_SELECTION_STRATEGY == CrossoverSelectionStrategy.RANDOM: 
            while True: # necessario per evitare che venga selezionata la stessa cella
                random_index = random.randint(0, len(self.solution_space_grid)-1)
                if random_index != cell_index:
                    return random_index
        elif EA_Config.CROSSOVER_SELECTION_STRATEGY == CrossoverSelectionStrategy.ADJACENT:
            if cell_index is not None:
                if cell_index == 0:
                    return cell_index + 1
                elif cell_index == len(self.solution_space_grid)-1:
                    return cell_index - 1
                else:
                    return cell_index + random.choice([-1, 1])
            else:
                return random.randint(0, len(self.solution_space_grid)-1)
        elif EA_Config.CROSSOVER_SELECTION_STRATEGY == CrossoverSelectionStrategy.BEST:
            # se ho già selezionato una cella, seleziono la migliore tra le altre
            if cell_index is not None: 
                values = [cell[1] for cell in self.solution_space_grid]
                values[cell_index] = -1
                return np.argmax(values)
            # altrimenti seleziono la migliore tra tutte
            else: 
                return np.argmax([cell[1] for cell in self.solution_space_grid])
        else: 
            raise Exception("Invalid crossover selection strategy")
            


    def mutation_and_crossover(self, cell_index):
        env_data = self.solution_space_grid[cell_index][0]
        
        if EA_Config.ALLOW_MUTATION:
            env_data = env_data.mutate()

        if EA_Config.ALLOW_CROSSOVER:
            other_cell_index = self.select_cell(cell_index=cell_index)
            other_env_data = self.solution_space_grid[other_cell_index][0]
            env_data = env_data.crossover(other_env_data)

        return env_data

    def stopping_criteria_met(self):
        return self.current_epoch > self.number_of_epochs
    
    def get_best_solutions(self):
        return [cell[0] for cell in self.solution_space_grid if cell is not None]
    

