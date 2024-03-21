import pygame as py


class Scorebanner:

    def __init__(self, snh, x, y, font='Arial', size=30, color_rgb=(0, 0, 0)):
        self.snh = snh
        self.x = x
        self.y = y
        self.color_rgb = color_rgb
        self.grose = 0

        py.font.init()
        self.text_font = py.font.SysFont(font, size)  # font pre text
        self.time_text = self.text_font.render('00:00:00', False, color_rgb)
        self.time_text_rect = self.time_text.get_rect(center=(self.x, self.y))
        self.grose_counter = self.text_font.render('0', False, color_rgb)
        grose_counter_x_offset = self.time_text_rect.width + 20
        self.grose_counter_rect= self.grose_counter.get_rect(center=(self.x + grose_counter_x_offset, self.y))

    def set_grose(self, grose):
        self.grose = grose
        self.grose_counter = self.text_font.render(str(grose), False, self.color_rgb)
    def set_time(self, time):
        millis = time
        seconds = (millis / 1000) % 60.
        seconds = round(int(seconds), 2)
        minutes = (millis / (1000 * 60)) % 60.
        minutes = round(int(minutes), 2)
        millis = round(millis, 2) % 1000
        self.time_text = self.text_font.render(
            str("{0:02}:{1:02}:{2:02}".format(minutes, seconds, millis)), False, self.color_rgb
        )

    def draw(self):
        self.snh.pozadie.obrazovka.blit(self.time_text, self.time_text_rect)
        self.snh.pozadie.obrazovka.blit(self.grose_counter, self.grose_counter_rect)

    def update(self):
        self.set_time(py.time.get_ticks())
        self.draw()
