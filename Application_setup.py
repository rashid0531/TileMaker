import AppVerification

# This script should contain information about all the possible parameters for a given task.
TILE_SINGLE_PICTURE = 'single picture'
TILE_MULTIPLE_PICTURES = 'multiple pictures'

# Need to automate finding the appropriate class. Watch the Pluralsight video.
TASKS = {TILE_SINGLE_PICTURE: AppVerification.ParamVerificationSinglePicture,
         TILE_MULTIPLE_PICTURES: AppVerification.ParamVerificationMultiplePictures}

SINGLE_PICTURE_ACTIONS = ('image_path',
                          'tile_size',
                          'save_path',
                          'Ath_coordinate',
                          'Bth_coordinate',
                          'Cth_coordinate',
                          'Dth_coordinate')

# Need to fill in later.
MULTIPLE_PICTURES_ACTIONS = ()


class TaskInfo:
    pass
