
from map_elites import MAP_Elites
from evolutionary_algorithm import EA_Config
import os

def main(): 
    if EA_Config.NO_DISPLAY: 
        os.environ["SDL_VIDEODRIVER"] = "dummy"

    algorithm = MAP_Elites()
    algorithm.run()

if __name__ == "__main__":
    main()
