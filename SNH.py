import pygame as py
import math
from pozadie import Pozadie
from structure_creator import StructureCreator
from player import Player
from scorebanner import Scorebanner
from Gros import Gros
from bear import Bear
from fireplace import Fireplace
from pygame import mixer
import menu
from save import Save

class SNH:
    def __init__(self):
        self.WIDTH = 1200
        self.HEIGHT = 700
        self.fps = 60
        self.gros_bg = 1200
        self.scroll_background = 0
        self.scroll_obstacles = 0
        self.world_phase = 0  # 0-pozadie.png
        self.zandar_phase = 0

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

        # music init
        mixer.init()
        mixer.music.load("music/bg.mp3")
        mixer.music.set_volume(0.5)
        self.coin_effect = mixer.Sound("music/minca.mp3")
        self.bear_effect = mixer.Sound("music/maco.mp3")
        self.fire_effect = mixer.Sound("music/ohen.mp3")
        self.bear_is_playing = False
        self.fire_is_playing = False

        self.timer = py.time.Clock()
        self.running = True
        self.peniaz = Gros()
        self.peniaz.generate()
        self.gros_y = 250

        # Load player
        self.player = Player()
        self.all_sprites = py.sprite.Group()
        self.all_sprites.add(self.player)
        self.game_speed = 4

        # Create menu
        self.menu = menu.Menu(self.pozadie.obrazovka, self.WIDTH, self.HEIGHT)

    def wait_for_start(self):
        waiting = True
        font = py.font.Font(None, 76)
        text = font.render("Please press the right arrow to begin!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.WIDTH / 2, self.HEIGHT - 250))

        while waiting:
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False
                    waiting = False
                if event.type == py.KEYDOWN:
                    if event.key == py.K_RIGHT:
                        waiting = False
            self.pozadie.obrazovka.blit(self.pozadie.fixed_background, [0, 0])
            for i in range(0, self.tiles):
                self.pozadie.obrazovka.blit(self.pozadie.background, [i * self.bg_width + self.scroll_background, 2])
            for entity in self.all_sprites:
                self.pozadie.obrazovka.blit(entity.curr_image, entity.rect)

            
            self.pozadie.obrazovka.blit(text, text_rect)

            py.display.update()
            self.timer.tick(self.fps)

    def run(self):
        self.menu.display_menu()
        self.menu.wait_for_input()
        self.wait_for_start()
        mixer.music.play(loops=-1)
        start_time = py.time.get_ticks()
        fireplace_anim_time_treshold = 300  # ms
        fireplace_anim_time = 0  # ms
        while self.running:
            self.timer.tick(self.fps)
            pressed_key = py.key.get_pressed()

            # draw backgroung
            self.pozadie.obrazovka.blit(self.pozadie.fixed_background, [0, 0])
            for i in range(0, self.tiles):
                self.pozadie.obrazovka.blit(self.pozadie.background, [i * self.bg_width + self.scroll_background, 2])
            self.scroll_background -= 4
            if abs(self.scroll_background) > self.bg_width:
                self.scroll_background = 0
            for entity in self.all_sprites:
                self.pozadie.obrazovka.blit(entity.curr_image, entity.rect)

            # gros stuff
            self.gros_bg -= 4
            
            zandar = py.image.load(f"images/zandar{self.zandar_phase % 5}.png").convert_alpha()
            self.pozadie.obrazovka.blit(zandar, (0, 560))
            self.zandar_phase += 1

            if self.gros_bg == -50 * (self.peniaz.width + 1):
                print("lk")
                self.gros_bg = 1200
                self.peniaz.x = 1200
                self.peniaz.generate()
                self.gros_y = objects[-1].y - 100
            self.scorebanner.set_grose(self.peniaz.amount)

            for gros in self.peniaz.coords:
                if abs(self.gros_bg + gros[0] - self.player.rect.x) < 50 and abs(self.gros_y - gros[1] - self.player.rect.y) < 50:
                    self.peniaz.coords.remove(gros)
                    self.peniaz.amount += 1
                    mixer.Channel(0).play(self.coin_effect, maxtime=1000)
                    continue
                self.pozadie.obrazovka.blit(self.peniaz.drawGros(), [self.gros_bg + gros[0], self.gros_y - gros[1]])
            self.scorebanner.update(start_time)
            self.scorebanner.draw()


            # player is dragged along with the scene
            self.player.rect.move_ip(-self.game_speed, 0)

            if self.player.rect.x < 10:
                self.running = False
            if self.player.rect.x + 75 > 1180:
                self.player.rect.x = 1180 - 75

            #create and draw objects
            base_x = 1200
            base_y = 661
            objects = []
            lethal_objects = []
            objects.append(py.draw.rect(self.pozadie.obrazovka, (53, 55, 33), [0, 661, 1200, 1]))  # ground
            if py.time.get_ticks() - fireplace_anim_time > fireplace_anim_time_treshold:
                Fireplace.animation_timer = (Fireplace.animation_timer + 1) % Fireplace.num_fireplace_anim_images
                fireplace_anim_time = py.time.get_ticks()
                print("Fireplace animation switch")
            bear_on_screen = False
            fire_on_screen = False
            if self.world_phase == 0:  # forest
                for obstacle in self.obstacles_forest:
                    if obstacle == "nic":
                        base_x += 80
                    elif obstacle == "medved":
                        bear = Bear(base_x, base_y)
                        bear.x_pos = base_x + self.scroll_obstacles
                        bear.y_pos = base_y - Bear.height / 2

                        if(bear.x_pos>-200 and bear.x_pos<1400):
                            bear_on_screen = True

                        bear.draw(self.pozadie)
                        lethal_objects.append(bear)
                        base_x += Bear.width * 2

                    elif obstacle == "vatra":
                        fireplace = Fireplace(base_x + self.scroll_obstacles, base_y)
                        if(base_x + self.scroll_obstacles>-200 and base_x + self.scroll_obstacles<1400):
                            fire_on_screen = True
                        fireplace.draw(self.pozadie)
                        lethal_objects.append(fireplace)
                        base_x += Fireplace.width * 2
                    else:
                        object_ = self.structure_creator.draw(self.pozadie, obstacle, base_x + self.scroll_obstacles, base_y)
                        move_by = object_[-1]
                        base_x += move_by
                        object_.pop(-1)
                        for o in object_:
                            objects.append(o)

            if(bear_on_screen):
                if(not self.bear_is_playing):
                    self.bear_is_playing = True
                    self.bear_effect.play(loops=-1)
            else:
                self.bear_effect.stop()
                self.bear_is_playing = False

            if(fire_on_screen):
                if(not self.fire_is_playing):
                    self.fire_is_playing = True
                    self.fire_effect.play(loops=-1)
            else:
                self.fire_effect.stop()
                self.fire_is_playing = False

            self.scroll_obstacles -= 4
            self.player.update(pressed_key, objects)

            # handle object collision
            for _object in objects:
                if self.player.rect.x + 75 >= _object.left and self.player.rect.x + 75 < _object.right and self.player.rect.bottom - 1 > _object.y + 1:
                    self.player.rect.x = _object.left - 75
                elif self.player.rect.x <= _object.right and self.player.rect.x > _object.left and self.player.rect.bottom - 1 > _object.y + 1:
                    self.player.rect.x = _object.right

            for lethal in lethal_objects:
                if isinstance(lethal, Bear):
                    if lethal.left() < self.player.rect.x - 75 < lethal.right() + Bear.width / 4 and self.player.rect.y > lethal.up() and self.player.rect.y - 100 < lethal.down():
                        print("Player", self.player.rect.x, self.player.rect.y)
                        print("Bear", lethal.x_pos, lethal.y_pos)
                        lethal.animation_timer += 1
                        self.running = False
                elif isinstance(lethal, Fireplace):
                    if self.player.rect.x - 75 > lethal.left() + Fireplace.width / 4 and self.player.rect.x - 75 < lethal.right() + Fireplace.width / 4  and self.player.rect.y > lethal.up() - Fireplace.height / 2 and self.player.rect.y < lethal.down() - Fireplace.height / 2:
                        print("Player", self.player.rect.x, self.player.rect.y)
                        print("Fireplace", lethal.x_pos, lethal.y_pos)
                        self.running = False

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False

            py.display.update()

        self.end_game(start_time)


    def end_game(self, start_time):
        mixer.music.stop()
        self.running = False
        
        game_data = Save.load_game_data()
        game_data['coins'] += self.peniaz.amount
        game_data['best_time'] = max(game_data['best_time'], py.time.get_ticks() - start_time)
        Save.save_game_data(game_data)
        font = py.font.Font(None, 76)
        message = font.render("You have been caught!", True, (255, 0, 0))
        message_rect = message.get_rect(center=(self.WIDTH / 2, self.HEIGHT / 2 - 100))

        elapsed_time = py.time.get_ticks() - start_time
        seconds = elapsed_time // 1000
        minutes = seconds // 60
        seconds %= 60   
        milliseconds = (elapsed_time % 1000) // 10
        time_message = font.render(f"Time: {minutes:02}:{seconds:02}:{milliseconds:02}", True, (255, 255, 255))
        time_rect = time_message.get_rect(center=(self.WIDTH / 2, self.HEIGHT / 2))
        score_message = font.render(f"Score: {self.peniaz.amount}", True, (255, 255, 255))
        score_rect = score_message.get_rect(center=(self.WIDTH / 2, self.HEIGHT / 2 + 100))
        button_font = py.font.Font(None, 40)
        button_text = button_font.render("Back to Menu", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=(self.WIDTH / 2, self.HEIGHT / 2 + 200))
        end_screen_running = True
        self.peniaz.amount = 0
        while end_screen_running:
            for event in py.event.get():
                if event.type == py.QUIT:
                    end_screen_running = False
                elif event.type == py.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        end_screen_running = False
                        self.reset_game()
            self.pozadie.obrazovka.blit(self.pozadie.fixed_background, [0, 0])
            for i in range(0, self.tiles):
                self.pozadie.obrazovka.blit(self.pozadie.background, [i * self.bg_width + self.scroll_background, 2])
            for entity in self.all_sprites:
                self.pozadie.obrazovka.blit(entity.curr_image, entity.rect)
            self.pozadie.obrazovka.blit(message, message_rect)
            self.pozadie.obrazovka.blit(time_message, time_rect)
            self.pozadie.obrazovka.blit(score_message, score_rect)
            self.pozadie.obrazovka.blit(button_text, button_rect)
            
            py.display.update()
            self.timer.tick(self.fps)

    def reset_game(self):
        self.scorebanner.set_grose(0)
        self.peniaz.generate()
        self.running = True
        self.player = Player()
        self.all_sprites = py.sprite.Group()
        self.all_sprites.add(self.player)
        self.game_speed = 4
        self.scroll_background = 0
        self.scroll_obstacles = 0
        self.run()



if __name__ == "__main__":
    snh = SNH()
    snh.run()
