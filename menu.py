import pygame as py
from shop import ShopMenu
from save import Save

class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = py.font.Font(None, 74)
        self.text_color = (255, 255, 255)
        self.background = py.image.load('images/menu_sample.jpg')
        self.background = py.transform.scale(self.background, (width, height))
        self.screen.blit(self.background, (0, 0))

    def display_menu(self):
        self.screen.blit(self.background, (0, 0))
        self.display_name()
        self.display_best_time()
        self.display_play()
        self.display_shop()
        self.display_quit()
        py.display.flip()

    def display_name(self):
        title = self.font.render('Slovenská Národná Hra', True, self.text_color)
        self.screen.blit(title, (self.width // 2 - title.get_width() // 2, (self.height // 4) - 100))

    def display_best_time(self):
        game_data = Save.load_game_data()
        curr_time = game_data['best_time']
        elapsed_time = curr_time
        seconds = elapsed_time // 1000
        minutes = seconds // 60
        seconds %= 60   
        milliseconds = (elapsed_time % 1000) // 10
        title = self.font.render(f"Best time: {minutes:02}:{seconds:02}:{milliseconds:02}", True, (255, 255, 255))
        title = py.transform.scale(title, (int(title.get_width() * 0.7), int(title.get_height() * 0.7)))
        self.screen.blit(title, (self.width // 2 - title.get_width() // 2, (self.height // 4) + 50))

    def display_play(self):
        self.play_butt = py.Rect((self.width // 2 - 100, self.height // 2 - 50, 200, 100))
        transparent_rect = py.Surface((self.play_butt.width, self.play_butt.height), py.SRCALPHA)
        transparent_rect.fill((100, 100, 100, 128))
        self.screen.blit(transparent_rect, self.play_butt.topleft)
        start_text = self.font.render('Start', True, self.text_color)
        text_rect = start_text.get_rect(center=self.play_butt.center)
        self.screen.blit(start_text, text_rect.topleft)

    def display_shop(self):
        self.shop_butt = py.Rect((self.width // 2 - 100, self.height // 2 + 50, 200, 100))
        transparent_rect = py.Surface((self.shop_butt.width, self.shop_butt.height), py.SRCALPHA)
        transparent_rect.fill((100, 100, 100, 128))
        self.screen.blit(transparent_rect, self.shop_butt.topleft)
        start_text = self.font.render('Shop', True, self.text_color)
        text_rect = start_text.get_rect(center=self.shop_butt.center)
        self.screen.blit(start_text, text_rect.topleft)

    def display_quit(self):
        self.quit_button = py.Rect((self.width // 2 - 100, self.height // 2 + 150, 200, 100))
        transparent_rect = py.Surface((self.quit_button.width, self.quit_button.height), py.SRCALPHA)
        transparent_rect.fill((100, 100, 100, 128))
        self.screen.blit(transparent_rect, self.quit_button.topleft)
        start_text = self.font.render('Quit', True, self.text_color)
        text_rect = start_text.get_rect(center=self.quit_button.center)
        self.screen.blit(start_text, text_rect.topleft)

    def wait_for_input(self):
        waiting = True
        while waiting:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.play_butt.collidepoint(event.pos):
                        waiting = False
                    elif self.quit_button.collidepoint(event.pos):
                        py.quit()
                    elif self.shop_butt.collidepoint(event.pos):
                        self.screen.blit(self.background, (0, 0))
                        shop_menu = ShopMenu(self.screen, self.width, self.height, self.background, self.font)
                        shop_menu.display_menu()
                        shop_menu.wait_for_input()
                        self.display_menu()
                if event.type == py.KEYDOWN:
                    if event.key == py.K_RETURN:
                        waiting = False

