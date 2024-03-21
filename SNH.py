import pygame as py
import math
from pozadie import Pozadie
from structure_creator import StructureCreator
from player import Player
from scorebanner import Scorebanner


class SNH:

    def __init__(self):

        self.WIDTH = 1200
        self.HEIGHT = 700
        self.fps = 60
        self.scroll_background = 0
        self.scroll_obstacles = 0
        self.world_phase = 0  # 0-pozadie.png

        self.structure_creator = StructureCreator()
        self.pozadie = Pozadie(WIDTH=self.WIDTH, HEIGHT=self.HEIGHT)
        self.bg_width = self.pozadie.background.get_width()
        self.tiles = math.ceil(self.WIDTH / self.bg_width) + 1
        self.obstacles_forest = []  # les
        self.scorebanner = Scorebanner(snh=self, x=self.WIDTH / 2, y=20)

        f = open("ob0.txt", "r")
        self.obstacles_forest = f.readline().strip().split(' ')
        f.close()

        py.init()

        self.timer = py.time.Clock()
        self.running = True

        # nacitaj hraca
        self.player = Player()
        self.all_sprites = py.sprite.Group()
        self.all_sprites.add(self.player)
        self.game_speed = 2


    def run(self):
        while (self.running):

            self.timer.tick(self.fps)
            pressed_key = py.key.get_pressed()
            # vykreslenie pozadia
            for i in range(0, self.tiles):
                self.pozadie.obrazovka.blit(self.pozadie.background, [i * self.bg_width + self.scroll_background, 0])
            self.scroll_background -= 2
            if (abs(self.scroll_background) > self.bg_width):
                self.scroll_background = 0
            for entity in self.all_sprites:
                self.pozadie.obrazovka.blit(entity.curr_image, entity.rect)

            # Update a kreslenie scorebannera
            self.scorebanner.update()
            self.scorebanner.draw()

            # vykreslenie prekazok
            base_x = 1200
            base_y = 661
            self.player.rect.move_ip(-self.game_speed, 0)

            if self.player.rect.x < 10:
                py.quit()
            if self.player.rect.x + 75 > 1180:
                self.player.rect.x = 1180 - 75

            objects = []
            if self.world_phase == 0:  # les
                for obstacle in self.obstacles_forest:
                    if (obstacle == "nic"):
                        base_x += 80
                    else:
                        object_ = self.structure_creator.draw(
                            self.pozadie, obstacle, base_x + self.scroll_obstacles, base_y
                        )
                        move_by = object_[-1]
                        base_x += move_by
                        object_.pop(-1)
                        for o in object_:
                            objects.append(o)

            self.scroll_obstacles -= 2
            self.player.update(pressed_key, objects)
            for _object in objects:
                if (self.player.rect.x + 75 >= _object.left
                        and self.player.rect.x + 75 < _object.right
                        and self.player.rect.bottom - 1 > _object.y + 1):
                    self.player.rect.x = _object.left - 75
                elif (self.player.rect.x <= _object.right
                      and self.player.rect.x > _object.left
                      and self.player.rect.bottom - 1 > _object.y + 1):
                    self.player.rect.x = _object.right

            for event in py.event.get():
                if (event.type == py.QUIT):
                    self.running = False
            # py.draw.rect(pozadie.obrazovka,(0,0,0),[player.rect.x,player.rect.y,75,100]) #75 100pozadie.obrazovka,(204,102,0),[b_x,b_y-300,300,300])
            # py.display.flip()
            py.display.update()

        py.quit()

if __name__=="__main__":
    snh = SNH()
    snh.run()