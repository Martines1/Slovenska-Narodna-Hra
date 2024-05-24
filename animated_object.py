import pygame as py
from sys import platform


class AnimatedObject(py.sprite.Sprite):

    if platform == 'win32':
        delimiter = '\\'
    else:
        delimiter = '/'
    image_source = "images" + delimiter

    def __init__(self):
        super().__init__()
