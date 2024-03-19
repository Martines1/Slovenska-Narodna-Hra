class Pozadie:
    
    def __init__(self,WIDTH,HEIGHT,py):
        self.obrazovka = py.display.set_mode([WIDTH,HEIGHT])
        py.display.set_caption('SNH')
        self.background = py.image.load("pozadie.png").convert()
        self.fps = 60
        
    def change_phase(self,phase,py):
        self.background = py.image.load("pozadie"+phase+".png").convert()