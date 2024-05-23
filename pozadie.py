import pygame as py
class Pozadie:
    
    def __init__(self, WIDTH, HEIGHT):
        self.obrazovka = py.display.set_mode([WIDTH,HEIGHT])
        py.display.set_caption('SNH')
        self.fixed_background = py.image.load("images/pozadie_tatry.png").convert()
        self.background = py.image.load("images/popredie_les.png").convert()
        self.background.set_colorkey((0, 0, 0))
        py.Surface.convert_alpha(self.background)
        
    def change_phase(self, postfix, py):
        self.background = py.image.load("images/popredie_" + postfix + ".png").convert()