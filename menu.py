import pygame
import pygame_menu


class Menu:
    def __init__(self, sc):
        self.sc = sc

    def crete_theme_menu(self):
        mytheme = pygame_menu.Theme(background_color=(0, 0, 0, 0),  # прозрачный фон
                       title_background_color=(4, 47, 126),
                       title_font_shadow=True,
                       widget_padding=25)
        return mytheme

    def start_menu(self):
        menu = pygame_menu.Menu(
            height=300,
            width=400,
            theme=pygame_menu.themes.THEME_BLUE,
            title='Welcome!'
        )
        menu.mainloop(self.sc)

