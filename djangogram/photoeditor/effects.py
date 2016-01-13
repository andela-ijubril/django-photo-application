import os

from PIL import Image, ImageFilter, ImageEnhance, ImageOps


class GramEffects(object):

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

    def greyscale(self):
        pass

    def mirror(self):
        pass

    def brighten(self):
        return 4

    def flip(self):
        pass

    def invert(self):
        pass


gram_effects = GramEffects()
photo_effects = {
    "flip": gram_effects.flip(),
    "brightness": gram_effects.brighten(),
    "invert": gram_effects.invert(),
}


