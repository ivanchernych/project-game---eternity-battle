import pygame
import pygame_menu
from game import Game


class Menu:
    def __init__(self, sc, size):
        self.sc = sc
        self.size = size

    def crete_theme_menu(self):
        mytheme = pygame_menu.Theme(background_color=(0, 0, 0, 0),  # прозрачный фон
                       title_background_color=(4, 47, 126),
                       title_font_shadow=True,
                       widget_padding=25)
        return mytheme

    def start_menu(self):
        menu = pygame_menu.Menu(
            height=self.size[1],
            width=self.size[0],
            theme=pygame_menu.themes.THEME_BLUE,
            title='Welcome!'
        )
        menu.add.button('Играть', Game)
        menu.add.button('Выход', Game)
        menu.mainloop(self.sc)

