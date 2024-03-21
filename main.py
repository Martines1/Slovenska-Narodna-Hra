import pygame as py
from SNH import SNH
import math
from pozadie import Pozadie
from structure_creator import StructureCreator
import player as pl
import scorebanner as sb
#miesto pred samotny beh kodu, nie triedy atd



######konstanty######
# WIDTH = 1200
# HEIGHT = 700
# scroll_bg = 0
# scroll_p = 0
# structure_creator = StructureCreator()
# pozadie = Pozadie(WIDTH,HEIGHT,py)
# bg_width = pozadie.background.get_width()
# tiles = math.ceil(WIDTH / bg_width)+1
# obstacles_0 = [] # les
# scorebanner = sb.Scorebanner(py=py, pozadie=pozadie, x=WIDTH/2, y=20)
# f = open("ob0.txt", "r")
# obstacles_0 = f.readline().strip().split(' ')
# f.close()
# phase = 0 # 0-pozadie.png
#
# #####################
#
#
# ######----mainloop----######
# py.init()
#
# timer = py.time.Clock()
# running = True
#
# #nacitaj hraca
# player = pl.Player()
# all_sprites = py.sprite.Group()
# all_sprites.add(player)
#
# game_speed = 4
# while(running):
#
#     timer.tick(pozadie.fps)
#     pressed_key = py.key.get_pressed()
#     #vykreslenie pozadia
#     for i in range(0,tiles):
#
#         pozadie.obrazovka.blit(pozadie.background,[i*bg_width+scroll_bg,0])
#     scroll_bg-=2
#     if(abs(scroll_bg)>bg_width):
#         scroll_bg = 0
#     for entity in all_sprites:
#         pozadie.obrazovka.blit(entity.curr_image, entity.rect)
#
#     #Update a kreslenie scorebannera
#     scorebanner.update()
#     scorebanner.draw()
#
#     #vykreslenie prekazok
#     base_x = 1200
#     base_y = 661
#     player.rect.move_ip(-game_speed, 0)
#
#     if player.rect.x < 10:
#         py.quit()
#     if player.rect.x+75 >1180:
#         player.rect.x = 1180-75
#
#
#     objects = []
#     if phase==0:#les
#         for ob in obstacles_0:
#             if(ob=="nic"):
#                 base_x+=80
#             else:
#                 object_ = structure_creator.draw(pozadie,ob,base_x+scroll_p,base_y)
#                 move_by = object_[-1]
#                 base_x+=move_by
#                 object_.pop(-1)
#                 for o in object_:
#                     objects.append(o)
#
#
#
#
#     scroll_p-=2
#     player.update(pressed_key, objects)
#     for _object in objects:
#         if player.rect.x+75 >= _object.left and player.rect.x+75< _object.right and player.rect.bottom-1 > _object.y+1 :
#             player.rect.x = _object.left - 75
#         elif player.rect.x <= _object.right and player.rect.x > _object.left and player.rect.bottom-1 > _object.y+1 :
#             player.rect.x = _object.right
#
#     for event in py.event.get():
#         if(event.type==py.QUIT):
#             running = False
#     #py.draw.rect(pozadie.obrazovka,(0,0,0),[player.rect.x,player.rect.y,75,100]) #75 100pozadie.obrazovka,(204,102,0),[b_x,b_y-300,300,300])
#     #py.display.flip()
#     py.display.update()

######----------------######