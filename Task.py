import abc
from abc import ABC
import os
import Application_setup as appsetup
from ImageObject import ImageObject
import CoreTaskFunc as task_func


class Tasks(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def initialize_task(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass


class TileSinglePicture(Tasks):
    def __init__(self, task_setup):
        self.settings = task_setup
        self.image_obj = None
        self.tile_width = None
        self.tile_height = None
        self.output_directory = None
        self.coordinates_used_for_cropping = None

    def initialize_task(self):
        try:
            img_path = self.settings['image_path']
            self.image_obj = ImageObject(img_path)
            output_directory = self.settings['save_path']
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)
            self.output_directory = output_directory
            self.tile_width, self.tile_height = self.settings['tile_size']
            self.coordinates_used_for_cropping = (self.settings['Ath_coordinate'],
                                                  self.settings['Bth_coordinate'],
                                                  self.settings['Cth_coordinate'],
                                                  self.settings['Dth_coordinate'])

        except Exception as e:
            pass

    def run(self):
        task_func.make_tiles(self.image_obj,
                             self.coordinates_used_for_cropping,
                             (self.tile_width, self.tile_height),
                             self.output_directory)


class TileMultiplePictures(Tasks):
    def __init__(self, task_setup):
        self.settings = task_setup

    def initialize_task(self):
        pass

    def run(self):
        pass


class TaskRunner:
    @classmethod
    def run_task(cls, task_setup: dict):
        try:
            task = appsetup.TASKS_RUNNER[task_setup['task']]
            task_instance = task(task_setup)
            task_instance.initialize_task()
            task_instance.run()
        except KeyError as e:
            print(f'Invalid task: {e} Not found.')
