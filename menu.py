import pygame_menu


class Menu:
    def __init__(self, type_menu, screen_size, screen, start_game):
        self.screen_size = screen_size
        self.screen = screen
        self.start_game = start_game
        self.type_menu = type_menu

    def create_theme_menu(self, image):
        myimage = pygame_menu.baseimage.BaseImage(
            image_path=image,
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
            drawing_offset=(0, 0)
        )
        mytheme = pygame_menu.Theme(background_color=myimage,  # прозрачный фон
                                    title_background_color=(4, 47, 126),
                                    title_font_shadow=True,
                                    widget_padding=25,
                                    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE)
        return mytheme

    def open_main_menu(self):
        menu = pygame_menu.Menu(
            height=self.screen_size[1],
            width=self.screen_size[0],
            theme=self.create_theme_menu('date/menu_image.png'),
            title=''
        )
        menu.add.button('Играть', lambda: self.start_game(map, round))
        menu.add.button('Управление', lambda: self.controle())
        map = menu.add.selector('карта: ', [('1', 1), ('2', 2)], style=pygame_menu.widgets.SELECTOR_STYLE_FANCY)
        round = menu.add.selector('кол-во раундов: ', [('5', 1), ('10', 2), ('20', 3)],
                                  style=pygame_menu.widgets.SELECTOR_STYLE_FANCY)
        menu.add.button('Выход', pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

    def winner_player1(self):
        menu = pygame_menu.Menu(
            height=self.screen_size[1],
            width=self.screen_size[0],
            theme=self.create_theme_menu('date/winer_player_1.jpg'),
            title=''
        )
        menu.add.button('Меню', lambda: self.open_main_menu())
        menu.add.button('Выход', pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

    def winner_player2(self):
        menu = pygame_menu.Menu(
            height=self.screen_size[1],
            width=self.screen_size[0],
            theme=self.create_theme_menu('date/winer_player_2.jpg'),
            title=''
        )
        menu.add.button('Меню', lambda: self.open_main_menu())
        menu.add.button('Выход', pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

    def controle(self):
        menu = pygame_menu.Menu(
            height=self.screen_size[1],
            width=self.screen_size[0],
            theme=self.create_theme_menu('date/controle.jpg'),
            title=''
        )
        menu.add.button('Назад', lambda: self.open_main_menu())
        menu.mainloop(self.screen)

    def start_menu(self):
        if self.type_menu == "main":
            self.open_main_menu()
        elif self.type_menu == "win player 1":
            self.winner_player1()
        elif self.type_menu == "win player 2":
            self.winner_player2()
