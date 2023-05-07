import numpy as np
import matplotlib.pyplot as plt
import random

from pettingzoo.utils import random_demo

import custom_combined_arms
from problem_params import ProblemParameters
from environment_data import EnvironmentData

LOG_DIRECTORY = "logs/"
DEBUG = False

class MAP_Elites: 
    def __init__(self, problem_parameters : ProblemParameters):
        # TODO: questi parametri vanno fatti meglio
        self.current_epoch = 0
        self.log_counter = 0
        self.num_dimensions = 1
        self.cells_in_grid = problem_parameters.cells_in_grid
        self.total_agents = problem_parameters.total_agents

        #setting of problem parameters as self
        self.allow_mutation = problem_parameters.allow_mutation
        self.allow_crossover = problem_parameters.allow_crossover
        self.number_of_episodes = problem_parameters.number_of_episodes
        self.number_of_epochs = problem_parameters.number_of_epochs

        # range di valori per EnvironmentData,
        # dicono che non possiamo avere 51 melee se ci sono al max 
        # 50 unità totali per team
        # TODO: integrare questo nella classe EnvironmentData e non qui
        self.cell_dimension = self.total_agents // self.cells_in_grid
        self.cell_boundaries = [i * self.cell_dimension for i in range(self.cells_in_grid)]

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
                print(f"Running: {self.current_epoch}")
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

            self.log("test", as_plot=True)
            self.current_epoch += 1

    def fitness_function(self, env_data):
        if DEBUG:
            print("Evaluating enviroment...")
        # eseguiamo l'environemnt con i parametri passati, 
        # che danno informazioni riguardo a numero di agenti e tipo di agenti
        env = custom_combined_arms.env(env_data=env_data, render_mode='human')
        fitness_score = random_demo(env, render=False, episodes=self.number_of_episodes)

        return fitness_score

    def select_cell(self):
        return random.randint(0, len(self.solution_space_grid)-1)

    def mutation_and_crossover(self, cell_index):
        env_data = self.solution_space_grid[cell_index][0]
        
        if self.allow_mutation:
            env_data.mutate()
        if self.allow_crossover:
            other_cell_index = self.select_cell()
            other_env_data = self.solution_space_grid[other_cell_index][0]
            env_data.crossover(other_env_data)

        return env_data

    def stopping_criteria_met(self):
        return self.current_epoch > self.number_of_epochs
    
    def get_best_solutions(self):
        return [cell[0] for cell in self.solution_space_grid if cell is not None]
    
    def log(self, file=None, as_plot=False): 
        if file is not None: 
            if as_plot:
                agent_count = [(i[0].melee_count, i[0].ranged_count) for i in self.solution_space_grid]
                ls = np.array([[i[1] for i in self.solution_space_grid]])

                plt.imshow(ls, cmap='hot', interpolation='nearest')
                # TODO: testa che questo funzioni
                plt.xticks(np.arange(len(agent_count)), agent_count)
                
                if self.log_counter == 0: 
                    plt.colorbar()
                plt.savefig(LOG_DIRECTORY + file + "_"+ str(self.log_counter))
                self.log_counter += 1
            else: 
                f = open(LOG_DIRECTORY + file, "+a")
                f.write("[")
                for i in self.solution_space_grid: 
                    f.write(f"|{round(i[1], 2)}|")
                f.write("]\n")
        else: 
            print("[", end="")
            for i in self.solution_space_grid: 
                print(f"|{round(i[1], 2)}|", end=" ")
            print("]")
