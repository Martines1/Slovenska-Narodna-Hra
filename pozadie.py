import pygame as py
class Pozadie:
    
    def __init__(self, WIDTH, HEIGHT):
        self.obrazovka = py.display.set_mode([WIDTH,HEIGHT])
        py.display.set_caption('SNH')
        self.background = py.image.load("pozadie.png").convert()
        
    def change_phase(self, phase, py):
        self.background = py.image.load("pozadie" + phase + ".png").convert()