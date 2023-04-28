
from map_elites import MAP_Elites
from problem_params import ProblemParameters
import os

NO_DISPLAY = True

def main(): 
    if NO_DISPLAY: 
        os.environ["SDL_VIDEODRIVER"] = "dummy"

    params = ProblemParameters()

    algorithm = MAP_Elites(params)
    algorithm.run()

    print("Best solution: ", algorithm.get_best_solutions())

if __name__ == "__main__":
    main()