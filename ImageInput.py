import os


class ImageInput(object):

    def __init__(self, path, representing_module):
        self.path = path
        self.representing_module = representing_module
        self.length = None
        self.width = None
        self.image_read = None
        self.load_image()

    def load_image(self):
        if self.path:
            if os.path.isfile(self.path):
                self.image_read = self.representing_module.open(self.path)
                self.length, self.width = self.image_read.size