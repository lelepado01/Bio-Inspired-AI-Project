
from map_elites import MAP_Elites
import os

NO_DISPLAY = True

def main(): 
    if NO_DISPLAY: 
        os.environ["SDL_VIDEODRIVER"] = "dummy"

    algorithm = MAP_Elites()
    algorithm.run()

if __name__ == "__main__":
    main()
