
from map_elites import MAP_Elites
from evolutionary_algorithm import EA_Config
from argparse import ArgumentParser
import os

def main(): 
    
    parser = ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", default=False, help="Enable debug mode")
    parser.add_argument("-nd", "--no-display", action="store_true", default=True, help="Disable pygame display")
    args = parser.parse_args()

    EA_Config.DEBUG = args.debug
    if args.no_display: 
        os.environ["SDL_VIDEODRIVER"] = "dummy"

    algorithm = MAP_Elites()
    algorithm.run()

if __name__ == "__main__":
    main()
