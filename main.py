
from map_elites import MapElites

def main(): 
    algorithm = MapElites()
    algorithm.run()

    print("Best solution: ", algorithm.get_best_solutions())

if __name__ == "__main__":
    main()