
class EnvironmentData:
    def __init__(self, total_units):
        self.melee = total_units * 0.5
        self.ranged = total_units - self.melee

    def mutate(self): 
        pass

    def crossover(self, other):
        pass