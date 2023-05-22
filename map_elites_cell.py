
import random
from evolutionary_algorithm import EA_Config, MutationStrategy, CrossoverStrategy

class MapElitesCell:
    def __init__(self, cell_index):
        self.cell_index = cell_index

        self.num_dimensions = 1
        self.cells_in_grid = EA_Config.CELLS_IN_GRID
        self.total_agents = EA_Config.TOTAL_NUMBER_OF_AGENTS
        
        self.cell_dimension = self.total_agents // self.cells_in_grid
        self.cell_boundary_low = self.cell_index * self.cell_dimension
        self.cell_boundary_high = (self.cell_index+1) * self.cell_dimension - 1
        self.current_value = random.randint(self.cell_boundary_low, self.cell_boundary_high)

        self.update_agent_numbers()

    # mantengo il valore corrente della cella all'interno dei limiti
    def constrain_cell_value(self):
        if self.current_value < self.cell_boundary_low:
            self.current_value = self.cell_boundary_low
        elif self.current_value > self.cell_boundary_high:
            self.current_value = self.cell_boundary_high

    def update_agent_numbers(self):
        self.number_of_melee = int(self.current_value)
        self.number_of_ranged = int(self.total_agents - self.current_value)

    def mutate(self): 
        if EA_Config.MUTATION_STRATEGY == MutationStrategy.RANDOM:
            val = random.randint(self.cell_boundary_low, self.cell_boundary_high)
            print("Mutated cell: ", val, " from ", self.current_value)
            self.current_value = val
        elif EA_Config.MUTATION_STRATEGY == MutationStrategy.GAUSSIAN:
            gauss_val = random.gauss(0, 1) * (self.cell_boundary_high - self.cell_boundary_low)
            self.current_value = int(self.current_value + gauss_val)
            self.constrain_cell_value()
        else:
            raise Exception("Invalid mutation strategy")
        
        self.update_agent_numbers()

    def crossover(self, other):
        if EA_Config.CROSSOVER_STRATEGY == CrossoverStrategy.MEAN:
            self.current_value = (self.current_value + other.current_value * EA_Config.CROSSOVER_WEIGHT) // 2
            self.constrain_cell_value()
        else:
            raise Exception("Invalid crossover strategy")
        
        self.update_agent_numbers()