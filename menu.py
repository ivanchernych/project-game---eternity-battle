import pygame_menu


class Menu:
    def __init__(self, type_menu):
        self.type_menu = type_menu

    def create_theme_menu(self):
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

    def open_main_menu(self, screen_size, screen, start_game):
        menu = pygame_menu.Menu(
            height=screen_size[1],
            width=screen_size[0],
            theme=self.create_theme_menu(),
            title=''
        )
        menu.add.button('Играть', start_game)
        menu.add.button('Управление', self.controle(screen_size, screen, lambda: start_game(self.map, self.round)))
        self.map = menu.add.selector('карта: ', [('1', 1), ('2', 2)], style=pygame_menu.widgets.SELECTOR_STYLE_FANCY)
        self.round = menu.add.selector('кол-во раундов: ', [('1', 1), ('10', 2), ('20', 3)],
                          style=pygame_menu.widgets.SELECTOR_STYLE_FANCY)
        menu.add.button('Выход', pygame_menu.events.EXIT)
        menu.mainloop(screen)

    def create_theme_menu_winer_player1(self):
        myimage = pygame_menu.baseimage.BaseImage(
            image_path='winer_player_1.jpg',
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
            drawing_offset=(0, 0)
        )
        mytheme = pygame_menu.Theme(background_color=myimage,  # прозрачный фон
                                    title_background_color=(4, 47, 126),
                                    title_font_shadow=True,
                                    widget_padding=25,
                                    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE)
        return mytheme

    def winer_player1(self, screen_size, screen, start_game):
        menu = pygame_menu.Menu(
            height=screen_size[1],
            width=screen_size[0],
            theme=self.create_theme_menu_winer_player1(),
            title=''
        )
        menu.add.button('Меню', self.open_main_menu(screen_size, screen, start_game))
        menu.add.button('Выход', pygame_menu.events.EXIT)
        menu.mainloop(screen)

    def create_theme_menu_winer_player2(self):
        myimage = pygame_menu.baseimage.BaseImage(
            image_path='winer_player_2.jpg',
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
            drawing_offset=(0, 0)
        )
        mytheme = pygame_menu.Theme(background_color=myimage,  # прозрачный фон
                                    title_background_color=(4, 47, 126),
                                    title_font_shadow=True,
                                    widget_padding=25,
                                    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE)
        return mytheme

    def winer_player2(self, screen_size, screen, start_game):
        menu = pygame_menu.Menu(
            height=screen_size[1],
            width=screen_size[0],
            theme=self.create_theme_menu_winer_player2(),
            title=''
        )
        menu.add.button('Меню', self.open_main_menu(screen_size, screen, start_game))
        menu.add.button('Выход', pygame_menu.events.EXIT)
        menu.mainloop(screen)

    def create_theme_menu_controle(self):
        myimage = pygame_menu.baseimage.BaseImage(
            image_path='controle.jpg',
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
            drawing_offset=(0, 0)
        )
        mytheme = pygame_menu.Theme(background_color=myimage,  # прозрачный фон
                                    title_background_color=(4, 47, 126),
                                    title_font_shadow=True,
                                    widget_padding=25,
                                    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE)
        return mytheme

    def controle(self, screen_size, screen, start_game):
        menu = pygame_menu.Menu(
            height=screen_size[1],
            width=screen_size[0],
            theme=self.create_theme_menu_controle(),
            title=''
        )
        menu.add.button('Назад', self.open_main_menu(screen_size, screen, lambda: start_game(self.map, self.round)) )

        menu.mainloop(screen)

    def start_menu(self, screen_size, screen, start_game):
        if self.type_menu == "main":
            self.open_main_menu(screen_size, screen, lambda: start_game(self.map, self.round))
        elif self.type_menu == "win player 1":
            self.winer_player1(screen_size, screen, lambda: start_game(self.map, self.round))
        elif self.type_menu == "win player 2":
            self.winer_player2(screen_size, screen, lambda: start_game(self.map, self.round))





