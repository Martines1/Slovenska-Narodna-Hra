import pygame as py
from save import Save

class ShopMenu:
    def __init__(self, screen, width, height, background, font):
        self.screen = screen
        self.width = width
        self.game_data = Save.load_game_data()
        self.height = height
        self.background = background
        self.font = font
        self.text_color = (255, 255, 255)
        self.items = ["Item 1", "Item 2", "Item 3"] 
        self.back_button = py.Rect((width // 2 - 100, height - 150, 200, 100))
        self.prices = dict()
        for value in self.items:
            price = 5 * (self.game_data[value] + 1)
            self.prices[value] = price
        

    def display_currency(self):
        game_data = Save.load_game_data()
        curr_currency = game_data['coins']
        curr_currency_label = self.font.render(f'Current number of coins: {curr_currency}', True, self.text_color)
        curr_currency_label = py.transform.scale(curr_currency_label, (int(curr_currency_label.get_width() * 0.5), int(curr_currency_label.get_height() * 0.5)))
        self.screen.blit(curr_currency_label, ((self.width // 2) - 150, 150))

        py.display.flip()

    def display_menu(self):
        
        self.screen.blit(self.background, (0, 0))
        self.display_currency()
        title = self.font.render('Shop Menu', True, self.text_color)
        self.screen.blit(title, (self.width // 2 - title.get_width() // 2, (self.height // 4) - 100))

        for i, item in enumerate(self.items):
            item_text = self.font.render(item, True, self.text_color)
            self.screen.blit(item_text, (self.width // 2 - 150 - item_text.get_width() // 2, (self.height // 2 - 150) + i * 100))
            for j in range(4):
                color = (255, 255, 255) if j < self.game_data[item] else (100, 100, 100)
                py.draw.circle(self.screen, color, (self.width // 2 - 200 + j * 100, (self.height // 2 - 50) + i * 100 - 30), 10)
            buy_text = self.font.render(f'Buy for {self.prices[item]}', True, self.text_color)
            buy_text = py.transform.scale(buy_text, (int(buy_text.get_width() * 0.5), int(buy_text.get_height() * 0.5)))
            buy_button = py.Rect((self.width // 2 + 150, (self.height // 2 - 175) + i * 100 + 30, 150, 50))
            py.draw.rect(self.screen, (100, 100, 100), buy_button)
            self.screen.blit(buy_text, (self.width // 2 + 150 + (buy_button.width - buy_text.get_width()) // 2, (self.height // 2 - 175) + i * 100 + 30 + (buy_button.height - buy_text.get_height()) // 2))

        transparent_rect = py.Surface((self.back_button.width, self.back_button.height), py.SRCALPHA)
        transparent_rect.fill((100, 100, 100, 128))
        self.screen.blit(transparent_rect, self.back_button.topleft)
        back_text = self.font.render('Back', True, self.text_color)
        text_rect = back_text.get_rect(center=self.back_button.center)
        self.screen.blit(back_text, text_rect.topleft)
        py.display.flip()

    def wait_for_input(self):
        waiting = True
        while waiting:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.back_button.collidepoint(event.pos):
                        waiting = False
                    for i, item in enumerate(self.items):
                        buy_button = py.Rect((self.width // 2 + 150, (self.height // 2 - 175) + i * 100 + 30, 150, 50))
                        if buy_button.collidepoint(event.pos):
                            if self.game_data['coins'] >= self.prices[item]:
                                self.game_data['coins'] -= self.prices[item]
                                self.game_data[item] += 1
                                self.prices[item] = 5 * (self.game_data[item] + 1)
                                Save.save_game_data(self.game_data)
                                self.display_menu()
                if event.type == py.KEYDOWN:
                    if event.key == py.K_ESCAPE:
                        waiting = False
        self.screen.blit(self.background, (0, 0))

