import pygame as py
from sys import platform


from pygame.locals import (
    RLEACCEL,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_UP
)

class Player(py.sprite.Sprite):
    def __init__(self):
        if platform == 'win32':
            delimiter = '\\'
        else:
            delimiter = '/'
        # pociatocna pozicia hraca
        self.y_position = 575
        self.x_position = 100
        self.image_source = "images" + delimiter 
        super(Player, self).__init__()
        self.jumping = False
        self.curr_image = self.load_image('janosik0.png')
        self.rect = py.Rect(50, 350, 75, 80)
        self.number_of_animations = 5
        self.rect.x = self.x_position
        self.rect.y = self.y_position
        self.y_vel = 0  # Vertical velocity
        self.jumping = False
        self.jump_height = 20  # Adjust jump height
        self.y_gravity = 1  # Adjust gravity for desired fall speed
        self.image_rotation = 'right'
        self.animation_timer = 0
        self.current_idle = 0
        self.current_run = 0
        self.current_jump = 0
        self.standing = True

    def load_image(self, image: str, flip : bool = False):
        width = 75
        height = 100
        new_image = py.image.load(self.image_source + image)
        #new_image = py.transform.scale(new_image, (width, height))
        new_image = py.transform.flip(new_image, flip, False)
        return new_image
    
    def flip_image(self):
        return py.transform.flip(self.curr_image, True, False)

    def update(self, key, objects = None):
        if key[K_RIGHT]:
            self.turn_right()
        elif key[K_LEFT]:
            self.turn_left()
        else:
            self.stay()
        if (key[py.K_SPACE] or key[py.K_UP]) and not self.jumping:
            self.jumping = True
            self.y_vel = self.jump_height
        if self.jumping:
            self.jump()
        standing = self.is_standing(objects)
        if not standing and self.jumping == False:
            self.fall()
        if not standing and self.rect.y >= 575:
            self.stay_on_ground()
                


    def turn_right(self):
        self.animation_timer += 1
        if self.animation_timer % 2 == 0:
            self.current_run = (self.current_run + 1) % self.number_of_animations
            flip = False
            if self.image_rotation == 'left':
                flip = True
                self.image_rotation = 'right' 
            if not self.jumping:
                self.curr_image = self.load_image('janosik{}.png'.format(self.current_run), flip)
        x_velocity = 8
        self.move(x_velocity)

    def turn_left(self):
        self.animation_timer += 1
        if self.animation_timer % 2 == 0:
            self.current_run = (self.current_run + 1) % self.number_of_animations
            if self.image_rotation == 'right':
                self.image_rotation = 'left' 
            if not self.jumping:
                flip = True
                self.curr_image = self.load_image('janosik{}.png'.format(self.current_run), flip)
        x_velocity = -4
        self.move(x_velocity)

    def stay(self):
        self.animation_timer += 1
        if self.animation_timer % 2 == 0:
            self.animation_timer = 0
            self.current_idle = (self.current_idle + 1) % self.number_of_animations
            flip = False
            if self.image_rotation == 'left':
                flip = True
            self.curr_image = self.load_image('janosik{}.png'.format(self.current_run), flip)

    def move(self, x_velocity):
        self.rect.x += x_velocity
        
        

    def jump(self):
        self.current_jump = (self.current_jump+1) % self.number_of_animations
        if self.image_rotation == 'left':
            self.curr_image = self.load_image('janosik{}.png'.format(self.current_jump), True)
        else:
            self.curr_image = self.load_image('janosik{}.png'.format(self.current_jump), False)
        self.y_vel -= self.y_gravity
        if self.y_vel < -self.jump_height:
            self.y_vel = -self.jump_height
        self.rect.y -= self.y_vel

    def fall(self):
        self.rect.y += 5
        self.current_jump = (self.current_jump+1) % self.number_of_animations
        if self.image_rotation == 'left':
            self.curr_image = self.load_image('janosik{}.png'.format(self.current_jump), True)
        else:
            self.curr_image = self.load_image('janosik{}.png'.format(self.current_jump), False)

    def stay_on_ground(self):
        self.jumping = False
        self.standing = True
        self.rect.y = 575


    def is_standing(self, objects):
        for _object in objects:
            if _object.y + 10 >= self.rect.y + 80 >= _object.y -10  and ((self.rect.x + 75 >= _object.left and self.rect.x + 75 <= _object.right) or (self.rect.x >= _object.left and self.rect.x <= _object.right)):
                self.rect.y = _object.y - 80
                self.y_vel = 0
                self.jumping = False
                return True
        return False
