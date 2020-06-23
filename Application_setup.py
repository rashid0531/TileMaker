import AppVerification
import Task
from SubParserSettings import ArgumentSubParser

# Application name and responsibilities.
APP_NAME = 'TileMaker'
APP_DESCRIPTION = 'A python application that split input images into tiles'

# This script should contain information about all the possible parameters for a given task.
TILE_SINGLE_PICTURE = 'single_picture'
TILE_MULTIPLE_PICTURES = 'multiple_pictures'

# Need to automate finding the appropriate class. Watch the Pluralsight video.
TASKS = {TILE_SINGLE_PICTURE: AppVerification.ParamVerificationSinglePicture,
         TILE_MULTIPLE_PICTURES: AppVerification.ParamVerificationMultiplePictures}

TASKS_RUNNER = {TILE_SINGLE_PICTURE: Task.TileSinglePicture,
                TILE_MULTIPLE_PICTURES: Task.TileMultiplePictures}

SINGLE_PICTURE_ARGUMENTS = ('image_path',
                            'tile_size',
                            'save_path',
                            'Ath_coordinate',
                            'Bth_coordinate',
                            'Cth_coordinate',
                            'Dth_coordinate')

PARSER_SINGLE_PICTURE = {'name': TILE_SINGLE_PICTURE,
                         'description': 'Create tiles from a single image.',
                         'arguments': [ArgumentSubParser(name_arg='--image_path',
                                                         number_of_args=1,
                                                         type_arg=str,
                                                         required_arg=True,
                                                         destination_arg='image_path'),
                                       ArgumentSubParser(name_arg='--tile_size',
                                                         number_of_args=2,
                                                         type_arg=int,
                                                         required_arg=True,
                                                         destination_arg='tile_size'),
                                       ArgumentSubParser(name_arg='--save_path',
                                                         number_of_args=1,
                                                         type_arg=str,
                                                         required_arg=True,
                                                         destination_arg='save_path'),
                                       ArgumentSubParser(name_arg='--Ath_coordinate',
                                                         number_of_args=2,
                                                         type_arg=int,
                                                         required_arg=True,
                                                         destination_arg='Ath_coordinate'),
                                       ArgumentSubParser(name_arg='--Bth_coordinate',
                                                         number_of_args=2,
                                                         type_arg=int,
                                                         required_arg=True,
                                                         destination_arg='Bth_coordinate'),
                                       ArgumentSubParser(name_arg='--Cth_coordinate',
                                                         number_of_args=2,
                                                         type_arg=int,
                                                         required_arg=True,
                                                         destination_arg='Cth_coordinate'),
                                       ArgumentSubParser(name_arg='--Dth_coordinate',
                                                         number_of_args=2,
                                                         type_arg=int,
                                                         required_arg=True,
                                                         destination_arg='Dth_coordinate'),
                                       ]}

assert len(SINGLE_PICTURE_ARGUMENTS) == len(PARSER_SINGLE_PICTURE['arguments'])

MULTIPLE_PICTURES_ARGUMENTS = ('image_dir',
                               'coordinate_file',
                               'save_path',
                               'computation_method'
                               )

PARSER_MULTIPLE_PICTURES = {'name': TILE_MULTIPLE_PICTURES,
                            'description': 'Create tiles from a multiple images.',
                            'arguments': [ArgumentSubParser(name_arg='--image_dir',
                                                            number_of_args=1,
                                                            type_arg=str,
                                                            required_arg=True,
                                                            destination_arg='image_dir'),
                                          ArgumentSubParser(name_arg='--coordinate_file',
                                                            number_of_args=1,
                                                            required_arg=True,
                                                            destination_arg='coordinate_file'),
                                          ArgumentSubParser(name_arg='--save_path',
                                                            number_of_args=1,
                                                            type_arg=str,
                                                            required_arg=True,
                                                            destination_arg='save_path'),
                                          ArgumentSubParser(name_arg='--computation_method',
                                                            number_of_args=1,
                                                            default_arg='sequential',
                                                            type_arg=str,
                                                            choices_arg=['sequential, concurrent'],
                                                            required_arg=True,
                                                            destination_arg='computation_method')
                                          ]}

APPLICATION_COMMANDS = [PARSER_SINGLE_PICTURE, PARSER_MULTIPLE_PICTURES]
