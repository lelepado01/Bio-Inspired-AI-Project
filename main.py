
from map_elites import MAP_Elites
import os

# TODO: fare la parte dell'enviroment, 
#   capire se si possono passare tutti i parametri alla funzione env
# TODO: funzioni di mutation e crossover in environment_data.py
# TODO: inizializzazione di EnvironmentData in base ai parametri passati
# TODO: fare in modo che MAP_Elites non stampi sempre tutto tutto
# TODO: magari si puù fare più di un algoritmo... non sembra così tanto lavoro
# TODO: c'è anche da fare il readme di github

def main(): 
    os.environ["SDL_VIDEODRIVER"] = "dummy"

    algorithm = MAP_Elites()
    algorithm.run()

    print("Best solution: ", algorithm.get_best_solutions())

if __name__ == "__main__":
    main()