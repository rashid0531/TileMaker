import abc
from abc import ABC


class Tasks(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def initialize_task(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass


class TileSinglePicture(Tasks):
    pass


class TileMultiplePictures(Tasks):
    pass
