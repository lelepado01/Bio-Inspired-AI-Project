
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

LOG_DIRECTORY = "logs/"
PLT2D = "plt2d/"
PLT3D = "plt3d/"

class Logger(): 
    """
    Classe ausiliaria per il logging dei dati
    - logga su file
    - plot 2d e 3d
    - plot fitness
    """

    def __init__(self, filename):
        self.file = open(LOG_DIRECTORY + filename, "+a")
        self.primary_fitnesses = []
        self.adversarial_fitnesses = []
        self.log_counter = 0

    def log(self, epoch, loss, accuracy):
        self.file.write('{},{},{}\n'.format(epoch, loss, accuracy))

    def close(self):
        self.file.close()

    def log_activity_grid(self, grid, label=""):
        ls = np.array([[i for i in grid]])
        plt.clf()
        plt.imshow(ls, cmap='hot', interpolation='nearest', vmin=0, vmax=max(grid))
        plt.xlabel("(Number of Melee, Number of Ranged)")
        plt.colorbar()

        plt.savefig(LOG_DIRECTORY + PLT2D + label + "_epoch_"+ str(self.log_counter))


    def to_plot_2d(self, grid, label=""): 
        agent_count = [(i[0].number_of_melee, i[0].number_of_ranged) for i in grid]
        ls = np.array([[i[1] for i in grid]])

        # for i in range(len(ls[0])):
        #     color = "black" if ls[0][i] == max([v for v in ls[0]]) else "w"
        #     plt.text(i, 0, str(round(ls[0][i], 2)), ha="center", va="center", color=color)

        plt.clf()
        plt.imshow(ls, cmap='hot', interpolation='nearest', vmin=-4000, vmax=4000)
        plt.xlabel("(Number of Melee, Number of Ranged)")
        plt.xticks(np.arange(len(agent_count)), agent_count, rotation=90)
        plt.colorbar()
        
        plt.savefig(LOG_DIRECTORY + PLT2D + label + "_epoch_"+ str(self.log_counter))
        self.log_counter += 1

    def to_plot_3d(self, grid, label=""):
        agent_count = [(i[0].number_of_melee, i[0].number_of_ranged) for i in grid]
        ls = [i[1] for i in grid]

        plt.clf()
        fig = plt.figure(figsize=(8, 8))
        ax1 = fig.add_subplot(111, projection='3d')
        ax1.bar3d(np.arange(len(ls)), 0, 0, 1, 1, ls, shade=True)
        plt.xlabel("(Number of Melee, Number of Ranged)")
        plt.xticks(np.arange(len(agent_count)), agent_count)

        plt.savefig(LOG_DIRECTORY + PLT3D + label + "_epoch_"+ str(self.log_counter))
        self.log_counter += 1


    def to_file(self, grid):
        self.file.write("[")
        for i in grid: 
            self.file.write(f"|{round(i[1], 2)}|")
        self.file.write("]\n")

    def to_console(self, grid):
        print("[", end="")
        for i in grid: 
            print(f"|{round(i[1], 2)}|", end=" ")
        print("]")

    def add_primary_fitness(self, fitnesses):
        fitness = sum(fitnesses) / len(fitnesses)
        self.primary_fitnesses.append(fitness)

    def add_adversarial_fitness(self, fitnesses):
        fitness = sum(fitnesses) / len(fitnesses)
        self.adversarial_fitnesses.append(fitness)

    def plot_fitness(self, label=""):
        plt.clf()
        if len(self.adversarial_fitnesses) == 0:
            plt.plot(self.primary_fitnesses, label="Fitness")
        else:
            df = pd.DataFrame({"Primary Fitness": self.primary_fitnesses, "Adversarial Fitness": self.adversarial_fitnesses})
            df.plot()
        plt.xlabel("Epoch")
        plt.ylabel("Fitness")
        plt.legend()
        plt.tight_layout()
        plt.savefig(LOG_DIRECTORY + label + ".png")