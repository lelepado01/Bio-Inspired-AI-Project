
import random

class FormationType:
    RANDOM = 0
    DEFAULT = 1
    SQUARE = 1
    TRIANGLE = 2

class EnvironmentData:
    def __init__(self, problem_parameters, cell_index):
        self.cell_index = cell_index

        self.num_dimensions = 1
        self.cells_in_grid = problem_parameters.cells_in_grid
        self.total_agents = problem_parameters.total_agents
        
        self.cell_dimension = self.total_agents // self.cells_in_grid
        self.cell_boundary_low = self.cell_index * self.cell_dimension
        self.cell_boundary_high = (self.cell_index+1) * self.cell_dimension - 1
        self.current_value = random.randint(self.cell_boundary_low, self.cell_boundary_high)

        self.number_of_melee = self.current_value
        self.number_of_ranged = self.total_agents - self.current_value

        self.initial_formation = FormationType.RANDOM

    def mutate(self): 
        pass

    def crossover(self, other):
        pass