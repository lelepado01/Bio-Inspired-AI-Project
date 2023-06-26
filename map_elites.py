import numpy as np
import random

from pettingzoo.utils import random_demo

import custom_combined_arms
from map_elites_cell import MapElitesCell
from evolutionary_algorithm import EA_Config, CrossoverSelectionStrategy, StoppingCriteria
from logger import Logger

FITNESS_LABEL = "fitness"

class MAP_Elites: 
    def __init__(self):
        self.current_epoch = 0
        self.logger = Logger("map_elites_log.txt")

        # partiamo con una griglia semplice con una sola dimensione 
        # la griglia contiene coppie (EnvironmentData, fitness)
        # dove enviroment data è il "genotipo" (ex. 5 melee e 5 ranged)
        if EA_Config.DEBUG:
            print("--- Initializing grid...")
        self.primary_grid = self.init_grid()
        self.old_best_primary_fitnesses = self.get_best_fitness(self.primary_grid)
        if EA_Config.USE_ADVERSARIAL_GRID:
            self.adversarial_grid = self.init_grid()
            self.old_best_adversarial_fitnesses = self.get_best_fitness(self.adversarial_grid)

    def init_grid(self): 
        grid = np.empty(EA_Config.CELLS_IN_GRID, dtype=object)
        for i in range(EA_Config.CELLS_IN_GRID):
            envdata = MapElitesCell(i)
            # e passiamo questa soluzione nel giochino per vedere come performa, 
            # restituisce direttamente il total_reward, quello che dobbiamo massimizzare
            fitness = self.fitness_function(envdata)
            grid[i] = (envdata, fitness)
        return grid
    
    def run_iteration_on_grid(self, grid):
        cell_index = self.select_cell()
        # Mutate the solution in the selected cell
        mutated_solution = self.mutation_and_crossover(cell_index)
        # Evaluate the fitness of the mutated solution
        fitness = self.fitness_function(mutated_solution)
        # Aggiorniamo la soluzione nella griglia 
        # solo se la fitness è migliore
        if fitness >= grid[cell_index][1]:
            if EA_Config.DEBUG: 
                print(f"New best fitness: {fitness} in cell {cell_index}")
            grid[cell_index] = (mutated_solution, fitness)
            return (mutated_solution, fitness), cell_index
        else: 
            if EA_Config.DEBUG: 
                print(f"Fitness not improved: {fitness} in cell {cell_index}")
            return None, None

    def run(self): 
        if EA_Config.DEBUG:
            print("--- Running MAP...")

        while True:
            print(f" --- Running epoch: {self.current_epoch} --- ")

            modified_cell, index = self.run_iteration_on_grid(self.primary_grid)
            if modified_cell is not None:
                self.primary_grid[index] = modified_cell
            self.logger.to_plot_2d(self.primary_grid, label="primary")
            self.logger.add_primary_fitness(self.get_best_fitness(self.primary_grid))

            if EA_Config.USE_ADVERSARIAL_GRID:
                modified_cell, index = self.run_iteration_on_grid(self.adversarial_grid)
                if modified_cell is not None:
                    self.adversarial_grid[index] = modified_cell
                self.logger.to_plot_2d(self.adversarial_grid, label="adversarial")
                self.logger.add_adversarial_fitness(self.get_best_fitness(self.adversarial_grid))


            self.current_epoch += 1

            if self.stopping_criteria_met():
                print("Best primary fitnesses: ")
                print(self.get_best_fitness(self.primary_grid))
                if EA_Config.USE_ADVERSARIAL_GRID:
                    print("Best adversarial fitnesses: ")
                    print(self.get_best_fitness(self.adversarial_grid))
                break
        
        self.logger.plot_fitness(FITNESS_LABEL)
        self.logger.close()

    def fitness_function(self, env_data):
        if EA_Config.DEBUG:
            print("Evaluating enviroment...")
        # eseguiamo l'environemnt con i parametri passati, 
        # che danno informazioni riguardo a numero di agenti e tipo di agenti
        env = custom_combined_arms.env(env_data=env_data, render_mode='human')
        fitness_score = random_demo(env, render=False, episodes=EA_Config.MAX_NUMBER_OF_EPISODES)
        return fitness_score

    def select_cell(self, cell_index=None):
        """
        Seleziona una cella della griglia in base alla strategia di selezione 
        """

        if EA_Config.CROSSOVER_SELECTION_STRATEGY == CrossoverSelectionStrategy.RANDOM: 
            while True: # necessario per evitare che venga selezionata la stessa cella
                random_index = random.randint(0, len(self.primary_grid)-1)
                if random_index != cell_index:
                    if EA_Config.DEBUG:
                        print(f"Selected cell: {random_index}")
                    return random_index
        elif EA_Config.CROSSOVER_SELECTION_STRATEGY == CrossoverSelectionStrategy.ADJACENT:
            selected_index = None
            if cell_index is not None:
                if cell_index == 0:
                    selected_index = cell_index + 1
                elif cell_index == len(self.primary_grid)-1:
                    selected_index = cell_index - 1
                else:
                    selected_index = cell_index + random.choice([-1, 1])
            else:
                selected_index = random.randint(0, len(self.primary_grid)-1)

            if EA_Config.DEBUG:
                print(f"Selected cell: {selected_index}")
            return selected_index
        
        elif EA_Config.CROSSOVER_SELECTION_STRATEGY == CrossoverSelectionStrategy.BEST:
            # se ho già selezionato una cella, seleziono la migliore tra le altre
            selected_index = None
            values = [cell[1] for cell in self.primary_grid]
            if cell_index is not None: 
                values[cell_index] = -10000000000

            selected_index = np.argmax(values)
            if EA_Config.DEBUG:
                print(f"Selected cell: {selected_index}")
            return selected_index
            
        elif EA_Config.CROSSOVER_SELECTION_STRATEGY == CrossoverSelectionStrategy.GAUSSIAN_BEST:    
            # se ho già selezionato una cella, seleziono la migliore tra le altre
            probs = [abs(cell[1]) for cell in self.primary_grid]
            if cell_index is not None: 
                # tolgo la cella già scelta
                probs[cell_index] = 0.0
            probs /= np.sum(probs)

            selected_index = np.random.choice(len(probs), p=probs)
            if EA_Config.DEBUG:
                print(f"Selected cell: {selected_index}")
            return selected_index
            
        else: 
            raise Exception("Invalid crossover selection strategy")
            

    def mutation_and_crossover(self, cell_index):
        selected_cell = self.primary_grid[cell_index][0]
        
        if EA_Config.ALLOW_MUTATION:
            old_cell = selected_cell
            selected_cell.mutate()
            if EA_Config.DEBUG and old_cell != selected_cell:
                print("Mutated cell: ", selected_cell)

        if EA_Config.ALLOW_CROSSOVER:
            other_cell_index = self.select_cell(cell_index=cell_index)
            other_env_data = self.primary_grid[other_cell_index][0]

            old_cell = selected_cell
            selected_cell.crossover(other_env_data)
            if EA_Config.DEBUG and old_cell != selected_cell:
                print("Crossover cell: ", old_cell)

        return selected_cell


    def stopping_criteria_met(self):

        if EA_Config.STOPPING_CRITERIA == StoppingCriteria.GENERATIONS:
            if EA_Config.DEBUG:
                print("Max number of epochs reached")
            return self.current_epoch > EA_Config.MAX_NUMBER_OF_EPOCHS
        
        elif EA_Config.STOPPING_CRITERIA == StoppingCriteria.GENERATIONS_WITHOUT_IMPROVEMENT: 
            if self.current_epoch > EA_Config.MAX_NUMBER_OF_EPOCHS: # se abbiamo superato il numero massimo di epoche allora stoppiamo
                if EA_Config.DEBUG:
                    print("Max number of epochs reached")
                return True
            else: # se non ci sono soluzioni migliori da almeno 10 epoche allora stoppiamo
                # TODO: gestire per adversarial grid
                current_best_fitnesses = self.get_best_fitness(self.primary_grid)

                if all([x >= y for x, y in zip(self.old_best_primary_fitnesses, current_best_fitnesses)]):
                    EA_Config.CURRENT_NUMBER_OF_EPOCHS_WITHOUT_IMPROVEMENT += 1
                else:
                    EA_Config.CURRENT_NUMBER_OF_EPOCHS_WITHOUT_IMPROVEMENT = 0

                self.old_best_primary_fitnesses = current_best_fitnesses

                if EA_Config.DEBUG:
                    print(f"Epochs without improvement: {EA_Config.CURRENT_NUMBER_OF_EPOCHS_WITHOUT_IMPROVEMENT}")
                return EA_Config.CURRENT_NUMBER_OF_EPOCHS_WITHOUT_IMPROVEMENT > EA_Config.MAX_NUMBER_OF_EPOCHS_WITHOUT_IMPROVEMENT
    
    def get_best_solutions(self, grid):
        return [cell[0] for cell in grid if cell is not None]
    
    def get_best_fitness(self, grid):
        return [cell[1] for cell in grid if cell is not None]
    

