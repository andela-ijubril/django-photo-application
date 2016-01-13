import os

from PIL import Image, ImageFilter, ImageEnhance, ImageOps


class GramEffects(object):
    def __init__(self, image):
        self.original_image = Image.open(image)

    def blur(self):
        pass

    def contour(self):
        pass

    def detail(self):
        pass

    def edge_enhance(self):
        pass

    def emboss(self):
        pass

    def smooth(self):
        pass

    def sharpen(self):
        pass

    def deform(self):
        pass

    def solarize(self):
        pass

    @staticmethod
    def greyscale(image):
        original_image = Image.open(image)
        return ImageOps.grayscale(original_image)

    def mirror(self):
        pass

    @staticmethod
    def brighten(image):
        original_image = Image.open(image)
        enhancer = ImageEnhance.Brightness(original_image)
        return enhancer.enhance(1.5)

    @staticmethod
    def flip(image):
        original_image = Image.open(image)
        return ImageOps.flip(original_image)

    def invert(self, image):
        original_image = Image.open(image)
        return ImageOps.invert(self.original_image)


photo_effects = {
    "flip": GramEffects.flip,
    "brightness": GramEffects.brighten,
    "invert": GramEffects.invert,
    "greyscale": GramEffects.greyscale
}


