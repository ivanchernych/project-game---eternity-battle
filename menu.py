import pygame
import pygame_menu
from game import Game


class Menu:
    def __init__(self, sc, size):
        self.sc = sc
        self.size = size


    def crete_theme_menu(self):
        myimage = pygame_menu.baseimage.BaseImage(
            image_path='menu_image.png',
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
            drawing_offset=(0, 0)
        )
        mytheme = pygame_menu.Theme(background_color=myimage,  # прозрачный фон
                       title_background_color=(4, 47, 126),
                       title_font_shadow=True,
                       widget_padding=25,
                       title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE)
        return mytheme

    def start_menu(self):
        menu = pygame_menu.Menu(
            height=self.size[1],
            width=self.size[0],
            theme=self.crete_theme_menu(),
            title=''
        )
        menu.add.button('Играть', Game)
        menu.add.selector('карта: ', [('map1', 1), ('map2', 2)], style=pygame_menu.widgets.SELECTOR_STYLE_FANCY)
        menu.add.selector('кол-во раундов: ', [('5', 1), ('10', 2), ('20', 3)], style=pygame_menu.widgets.SELECTOR_STYLE_FANCY)
        menu.add.button('Выход', pygame_menu.events.EXIT)
        menu.mainloop(self.sc)