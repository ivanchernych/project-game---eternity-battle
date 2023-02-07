import sys
import os
import pygame
from menu import Menu
from player import Player
from map import Map


def load_image(name, colorkey=None):
    fullname = os.path.join('date', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Game:
    def __init__(self, size_screen, caption):
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode(size_screen)
        self.size_screen = size_screen
        self.open_menu('main')

    def create_charackter(self):
        player1_image_left = load_image('1.1_photo-resizer.ru.png', -1)
        player1_image_right = load_image('1.2_photo-resizer.ru.png', -1)
        player_1_controle = {
            'left': pygame.K_a,
            'right': pygame.K_d,
            'jump': pygame.K_w,
            'attack': pygame.K_LSHIFT

        }
        self.player1 = Player('player1', player_1_controle, player1_image_left, player1_image_right, 50, 650, self.heart_player1, self.heart_player2, self.player1_point, self.player2_point,
                              self.item_group, self.player1_group, self.bullet, self.all_sprites, self.player2_group)

        player2_image_left = load_image('2.2_photo-resizer.ru.png', -1)
        player2_image_right = load_image('2.1_photo-resizer.ru.png', -1)
        player_2_controle = {
            'left': pygame.K_LEFT,
            'right': pygame.K_RIGHT,
            'jump': pygame.K_UP,
            'attack': pygame.K_RSHIFT

        }
        self.player2 = Player('player2', player_2_controle, player2_image_left, player2_image_right, 1575, 650, self.heart_player1, self.heart_player2, self.player1_point, self.player2_point,
                              self.item_group, self.player2_group, self.bullet, self.all_sprites, self.player1_group)

    def start_game(self, map, round):
        self.name_map = int(map.get_value()[0][0])
        self.round = int(round.get_value()[0][0])
        print(self.round, self.name_map)
        # ФПС
        FPS = 60
        tick = 0
        clock = pygame.time.Clock()

        # Группы
        self.item_group = pygame.sprite.Group()
        self.bullet = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.player1_group = pygame.sprite.Group()
        self.player2_group = pygame.sprite.Group()
        self.player1_point = []
        self.player2_point = []
        self.heart_player1 = []
        self.heart_player2 = []

        # Генерация карты
        Map(self.name_map, self.item_group, self.all_sprites).draw()

        # Создание персонажей
        self.create_charackter()
        self.player1.draw_heart()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game(event)
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LSHIFT:
                        self.player1.shoot()
                    if event.key == pygame.K_RSHIFT:
                        self.player2.shoot()
            # Обновление
            self.all_sprites.update()
            tick += 1
            clock.tick(FPS)
            if self.round == len(self.player1_point):
                print('WIN')
                Menu('win player 1').start_menu(self.size_screen, self.screen, self.start_game)
            if self.round == len(self.player2_point):
                Menu('win player 2').start_menu(self.size_screen, self.screen, self.start_game)

            f1 = pygame.font.Font('Molot.otf', 100)
            vs = f1.render('VS', True,
                              (255, 255, 255))
            pl1 = f1.render(str(len(self.player1_point)), True,
                              (255, 255, 255))
            pl2 = f1.render(str(len(self.player2_point)), True,
                              (255, 255, 255))

            # Отрисовка
            self.screen.fill((38, 219, 255))
            self.all_sprites.draw(self.screen)
            self.screen.blit(vs, (790, 740))
            self.screen.blit(pl1, (550, 740))
            self.screen.blit(pl2, (1050, 740))

            # После отрисовки всего, переворачиваем экран
            pygame.display.flip()

        pygame.quit()

    def open_menu(self, type_menu):
        m = Menu(type_menu)
        m.start_menu(self.size_screen, self.screen,  self.start_game)

    def exit_game(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
