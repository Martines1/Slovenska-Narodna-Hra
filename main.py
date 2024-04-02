import pygame as py
import math
from pozadie import Pozadie
from structure_creator import StructureCreator
import player as pl
from Gros import Gros
import random
#miesto pred samotny beh kodu, nie triedy atd



######konstanty######
WIDTH = 1200
HEIGHT = 700
scroll_bg = 0
gros_bg = 1200
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
peniaz = Gros()
peniaz.generate()
gros_y = 250
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

    gros_bg -= 2

    if gros_bg == -50 * (peniaz.width + 1):
        print("lk")
        gros_bg = 1200
        peniaz.x = 1200
        peniaz.generate()
        gros_y = objects[-1].y - 100

    for gros in peniaz.coords:
        if abs(gros_bg + gros[0] - player.rect.x) < 50 and abs(gros_y - gros[1] - player.rect.y) < 50:
            peniaz.coords.remove(gros)
            peniaz.amount += 1
            continue
        pozadie.obrazovka.blit(peniaz.drawGros(), [gros_bg + gros[0],gros_y - gros[1]])

    scroll_bg-=2

    pozadie.obrazovka.blit(peniaz.drawGros(), [0,50])
    myfont = py.font.SysFont("monospace", 50).render(peniaz.getAmount(), 1, (255,255,0))
    pozadie.obrazovka.blit(myfont, [40, 40])
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
    if player.rect.x+75 >1180:
        player.rect.x = 1180-75


    objects = []
    if phase==0:#les
        for ob in obstacles_0:
            if(base_x+scroll_p>1250):
                break
            if(ob=="nic"):
                base_x+=80
            else:
                object_ = structure_creator.draw(pozadie,ob,base_x+scroll_p,base_y)
                move_by = object_[-1]
                base_x+=move_by
                object_.pop(-1)
                for o in object_:
                    objects.append(o)


    scroll_p-=2
    player.update(pressed_key, objects)
    for _object in objects:
        if player.rect.x+75 >= _object.left and player.rect.x+75< _object.right and player.rect.bottom-1 > _object.y+1 :
            player.rect.x = _object.left - 75
        elif player.rect.x <= _object.right and player.rect.x > _object.left and player.rect.bottom-1 > _object.y+1 :
            player.rect.x = _object.right
    
    for event in py.event.get():
        if(event.type==py.QUIT):
            running = False
    #py.draw.rect(pozadie.obrazovka,(0,0,0),[player.rect.x,player.rect.y,75,100]) #75 100pozadie.obrazovka,(204,102,0),[b_x,b_y-300,300,300])
    #py.display.flip()
    py.display.update()

py.quit()
######----------------######
