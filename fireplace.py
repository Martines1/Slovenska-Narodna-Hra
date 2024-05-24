from animated_object import *


class Fireplace(AnimatedObject):
    images = []
    image = 'vatra'
    num_fireplace_anim_images = 3
    scale = 1.5
    for i in range(1, num_fireplace_anim_images + 1):
        images.append(py.image.load(AnimatedObject.image_source + image + str(i) + '.png'))
        images[i-1] = py.transform.scale(images[i-1], (int(images[i-1].get_width() * scale), int(images[i-1].get_height() * scale)))
    width = images[0].get_width()
    height = images[0].get_height()

    animation_timer = 0

    def __init__(self, x_start, y_start):
        super().__init__()
        self.x_pos = x_start
        self.y_pos = y_start

    def draw(self, pozadie):
        rect = py.Rect(self.right(), self.up(), Fireplace.width, Fireplace.height)
        pozadie.obrazovka.blit(Fireplace.images[Fireplace.animation_timer], rect)

    def right(self):
        return self.x_pos + Fireplace.width / 2

    def left(self):
        return self.x_pos - Fireplace.width / 2

    def up(self):
        return self.y_pos - Fireplace.width / 2

    def down(self):
        return self.y_pos + Fireplace.height / 2
