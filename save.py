import pygame as py
import os
import json


class Save():

    def load_game_data():
        game_data = {
            'coins': 0,
            'best_time': 0,
            'Item 1': 0,
            'Item 2': 0,
            'Item 3': 0
        }
        if os.path.exists('game_data.json'):
            with open('game_data.json', 'r') as file:
                game_data = json.load(file)
        return game_data


    def save_game_data(game_data):
        with open('game_data.json', 'w') as file:
            json.dump(game_data, file)