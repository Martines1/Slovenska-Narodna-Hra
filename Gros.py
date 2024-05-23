import random

import pygame as py

class Gros:

    def __init__(self):
        self.x = 1200
        self.y = 0
        self.pattern = ['triangle','worm','square']
        self.coords = []
        self.width = 0
        self.amount = 0


    def getAmount(self):
        return str(self.amount)

    def addAmount(self):
        self.amount += 1
    def generate(self):
        self.coords = self.drawPattern(random.choice(self.pattern))
    def drawGros(self):
        imp = py.image.load("images/gros.png").convert()
        return imp

    def drawPattern(self,name):
        self.coords = []
        size = random.randrange(1,5 + 1)
        self.width = size
        if name == 'triangle':
            for i in range(1,size + 1):
                for j in range(i,size + 1):
                    self.coords.append([i * 50,(j - i) * -50])
        if name == "square":
            for i in range(1,size + 1):
                for j in range(1,size + 1):
                    self.coords.append([i * 50,j * -50])
        if name == "worm":
            self.width = size * 2
            for i in range(1,2 * size):
                self.coords.append([i * 50,0])
        return self.coords

    def setHeight(self,y):
        self.y = y

    def setWidth(self,x):
        self.x = x