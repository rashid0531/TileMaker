# The following default values will be used if not provided from the command line argums.
import argparse
import os

from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


def format_string(input_str):
    input_values = input_str.split(',')
    for index, value in enumerate(input_values):
        input_values[index] = int(value)
    return input_values


def make_tiles(arguments):
    try:
        img_path = os.path.abspath(arguments['image_path'])
        if os.path.isfile(img_path):
            img = Image.open(img_path)
        else:
            print('Not a valid file')
        cnn_input_size = format_string(arguments['tile_size'])
        cnn_input_width = cnn_input_size[0]
        cnn_input_height = cnn_input_size[1]
        output_directory = str(arguments['save_path'])
        a = format_string(arguments['Ath_coordinate'])
        b = format_string(arguments['Bth_coordinate'])
        c = format_string(arguments['Cth_coordinate'])
        d = format_string(arguments['Dth_coordinate'])

    except KeyError as e:
        err_str = "No such argument called {}".format(e)
        print(err_str)
        exit()

    abscissa_idx = 0
    ordinate_idx = 1
    tiles_per_row = int((b[abscissa_idx] - a[abscissa_idx]) / cnn_input_width)
    tiles_per_column = int((c[ordinate_idx] - b[ordinate_idx]) / cnn_input_height)
    cropped_img_abscissa_min = a[abscissa_idx]
    cropped_img_ordinate_min = a[ordinate_idx]

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    # Naming convention for tiled images.
    prefix = str(img.filename.split("/")[-1])
    prefix = str(prefix.split(".")[0])

    for i in range(0, tiles_per_column):
        for j in range(0, tiles_per_row):
            left = cropped_img_abscissa_min + j * cnn_input_width
            right = cropped_img_abscissa_min + (j + 1) * cnn_input_width
            upper = cropped_img_ordinate_min + i * cnn_input_height
            lower = cropped_img_ordinate_min + (i + 1) * cnn_input_height

            points = (left, upper, right, lower)
            tile = img.crop(points)
            tile.save(output_directory + "/" + prefix + "_" + str(i) + "_" + str(j) + ".jpg")


if __name__ == "__main__":
    '''
    Considering the following coordinates are given for an input image 
        
        140, 182	1052, 182
        140, 630	1052, 630
        
    Use the following command to run the script.
        python tile_maker.py -ip "frame000700.jpg" -ts 224,224 -sp "./here" -corA 140,182 -corB 1052,182 -corC 1052,630 -corD 140,630

    '''

    DEFAULT_IMAGE_PATH = None
    DEFAULT_TILE_SIZE = 224
    DEFAULT_SAVE_PATH = None

    ap = argparse.ArgumentParser(description="Script to split a given image into multiple tiles.")

    ap.add_argument("-ip", "--image_path", required=True, help="Path to the input image")
    ap.add_argument("-ts", "--tile_size", required=True, help="Size of each tile")
    ap.add_argument("-sp", "--save_path", required=True, help="Path to the save the tiled image")
    ap.add_argument("-corA", "--Ath_coordinate", required=True, help="Coordinate of point A in the input image.")
    ap.add_argument("-corB", "--Bth_coordinate", required=True, help="Coordinate of point B in the input image.")
    ap.add_argument("-corC", "--Cth_coordinate", required=True, help="Coordinate of point C in the input image.")
    ap.add_argument("-corD", "--Dth_coordinate", required=True, help="Coordinate of point D in the input image.")
    arguments = vars(ap.parse_args())

    make_tiles(arguments)
