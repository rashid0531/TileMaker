import os
from PIL import Image, ImageFile


class ImageObject(object):

    def __init__(self, path):
        self.path = path
        self.length = None
        self.width = None
        self.img_obj = None

    def load_image(self):
        try:
            self.img_obj = Image.open(self.path)
            self.length, self.width = self.img_obj.size
        except Exception as e:
            print(e)

        return self.img_obj
