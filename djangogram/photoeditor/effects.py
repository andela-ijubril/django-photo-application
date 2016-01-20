import os

from PIL import Image, ImageFilter, ImageEnhance, ImageOps


class Deformer:
    def getmesh(self, im):
        x, y = im.size
        return [((0, 0, x, y), (0, 0, x, 0, x, y, y, 0))]

deformer = Deformer()


class GramEffects(object):

    @classmethod
    def g_open(cls, image):
        '''
        A class method that opens an image and returns a class
        '''
        cls.image = Image.open(image)
        return cls

    @classmethod
    def blur(cls):
        return cls.image.filter(ImageFilter.GaussianBlur(radius=2))

    @classmethod
    def deform(cls):
        return ImageOps.deform(cls.image, deformer=deformer)

    @classmethod
    def solarize(cls):
        return ImageOps.solarize(cls.image)

    @classmethod
    def greyscale(cls):
        return ImageOps.grayscale(cls.image)

    @classmethod
    def mirror(cls):
        return ImageOps.mirror(cls.image)

    @classmethod
    def brighten(cls):
        enhancer = ImageEnhance.Brightness(cls.image)
        return enhancer.enhance(1.5)

    @classmethod
    def flip(cls):
        return ImageOps.flip(cls.image)

    @staticmethod
    def g_apply(effect_name):
        """
        A class method that apply any effect specified in the photo_effects dictionary
        :param effect_name:
        """
        effect = photo_effects.get(effect_name)
        return effect()

photo_effects = {
    "flip": GramEffects.flip,
    "brightness": GramEffects.brighten,
    "solarize": GramEffects.solarize,
    "greyscale": GramEffects.greyscale,
    "mirror": GramEffects.mirror,
    "deform": GramEffects.deform,
    "blur": GramEffects.blur
}
