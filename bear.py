from animated_object import *


class Bear(AnimatedObject):
    images = []
    image = 'medved'
    image_source = ""
    num_bear_anim_images = 2
    for i in range(1, num_bear_anim_images + 1):
        images.append(py.image.load(image_source + image + str(i) + '.png'))

    width = images[0].get_width()
    height = images[0].get_height()



    def __init__(self, x_start, y_start):
        super().__init__()
        self.x_pos = x_start
        self.y_pos = y_start
        self.animation_timer = 0
    def draw(self, pozadie):
        rect = py.Rect(self.right(), self.up(), Bear.width, Bear.height)
        pozadie.obrazovka.blit(Bear.images[self.animation_timer], rect)

    def right(self):
        return self.x_pos + Bear.width / 2

    def left(self):
        return self.x_pos - Bear.width / 2

    def up(self):
        return self.y_pos - Bear.width / 2

    def down(self):
        return self.y_pos + Bear.height / 2
