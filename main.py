import pygame as py
import math
from pozadie import Pozadie

#miesto pred samotny beh kodu, nie triedy atd



######konstanty######
WIDTH = 1200
HEIGHT = 700
scroll = 0
pozadie = Pozadie(WIDTH,HEIGHT,py)
bg_width = pozadie.background.get_width()
tiles = math.ceil(WIDTH / bg_width)+1
print(tiles)
#####################



######----mainloop----######
py.init()

timer = py.time.Clock()
running = True
while(running):
    timer.tick(pozadie.fps)

    #vykreslenie pozadia
    for i in range(0,tiles):
        pozadie.obrazovka.blit(pozadie.background,[i*bg_width+scroll,0])
    scroll-=2
    if(abs(scroll)>bg_width):
        scroll = 0

    for event in py.event.get():
        if(event.type==py.QUIT):
            running = False

    #py.display.flip()
    py.display.update()

py.quit()
######----------------######