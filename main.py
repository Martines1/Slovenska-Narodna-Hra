import pygame as py
import math
from pozadie import Pozadie
from structure_creator import StructureCreator
import player as pl
#miesto pred samotny beh kodu, nie triedy atd



######konstanty######
WIDTH = 1200
HEIGHT = 700
scroll_bg = 0
scroll_p = 0
structure_creator = StructureCreator()
pozadie = Pozadie(WIDTH,HEIGHT,py)
bg_width = pozadie.background.get_width()
tiles = math.ceil(WIDTH / bg_width)+1
obstacles_0 = [] # les
f = open("ob0.txt", "r")
obstacles_0 = f.readline().strip().split(' ')
f.close()
phase = 0 # 0-pozadie.png
#####################



######----mainloop----######
py.init()

timer = py.time.Clock()
running = True

#nacitaj hraca
player = pl.Player()
all_sprites = py.sprite.Group()
all_sprites.add(player)

game_speed = 2
while(running):
    timer.tick(pozadie.fps)
    pressed_key = py.key.get_pressed()
    #vykreslenie pozadia
    for i in range(0,tiles):

        pozadie.obrazovka.blit(pozadie.background,[i*bg_width+scroll_bg,0])
    scroll_bg-=2
    if(abs(scroll_bg)>bg_width):
        scroll_bg = 0
    for entity in all_sprites:
        pozadie.obrazovka.blit(entity.curr_image, entity.rect)
    #vykreslenie prekazok
    base_x = 1200
    base_y = 661
    player.rect.move_ip(-game_speed, 0)
    if player.rect.x < 10:
        py.quit()
    if phase==0:#les
        for ob in obstacles_0:
            if(ob=="nic"):
                base_x+=100
            else:
                move_by = structure_creator.draw(pozadie,ob,base_x+scroll_p,base_y)
                base_x+=move_by

    scroll_p-=1
    player.update(pressed_key)

    for event in py.event.get():
        if(event.type==py.QUIT):
            running = False

    #py.display.flip()
    py.display.update()

py.quit()
######----------------######