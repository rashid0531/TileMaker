# The following default values will be used if not provided from the command line arguments.
import argparse
from verify_param import VerifyParameters
from Task import TaskRunner

DEFAULT_IMAGE_PATH = None
DEFAULT_TILE_SIZE = 224
DEFAULT_SAVE_PATH = None

ap = argparse.ArgumentParser(description="Script to split a given image into multiple tiles.")

ap.add_argument("-t", "--task", required=True, help="Name of the Task")
ap.add_argument("-ip", "--image_path", required=True, help="Path to the input image")
ap.add_argument("-ts", "--tile_size", required=True, help="Size of each tile")
ap.add_argument("-sp", "--save_path", required=True, help="Path to the save the tiled image")
ap.add_argument("-corA", "--Ath_coordinate", required=True, help="Coordinate of point A in the input image.")
ap.add_argument("-corB", "--Bth_coordinate", required=True, help="Coordinate of point B in the input image.")
ap.add_argument("-corC", "--Cth_coordinate", required=True, help="Coordinate of point C in the input image.")
ap.add_argument("-corD", "--Dth_coordinate", required=True, help="Coordinate of point D in the input image.")

args = vars(ap.parse_args())
isVerified, task_Setup = VerifyParameters.create_appropriate_app_verification(args)
if isVerified:
    TaskRunner.run_task(task_Setup)


'''
140, 182	1052, 182
140, 630	1052, 630

python __main__.py -ip "frame000700.jpg" -ts 224,224 -sp "./here" -corA 140,182 -corB 1052,182 -corC 1052,630 -corD 140,630

Todo:
1. Build a single core version.
2. Create a logger to show the progress.
3. Build a concurrent version.

'''
