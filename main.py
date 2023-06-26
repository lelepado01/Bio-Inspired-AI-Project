
from map_elites import MAP_Elites
from evolutionary_algorithm import EA_Config
from argparse import ArgumentParser
import os

def main(): 
    
    parser = ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-nd", "--no-display", action="store_true", help="Disable pygame display")

    args = parser.parse_args()
    if args.debug:
        EA_Config.DEBUG = True
    if not args.no_display:
        EA_Config.NO_DISPLAY = True

    if EA_Config.NO_DISPLAY: 
        os.environ["SDL_VIDEODRIVER"] = "dummy"

    algorithm = MAP_Elites()
    algorithm.run()

if __name__ == "__main__":
    main()
