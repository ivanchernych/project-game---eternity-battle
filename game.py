import sys
import os
import pygame
from menu import Menu
from player import Player


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
        player1_image_left = load_image('player1_image_left.png', -1)
        player1_image_right = load_image('player1_image_right.png', -1)
        player_1_controle = {
            'left': pygame.K_a,
            'right': pygame.K_d,
            'jump': pygame.K_w,
            'attack': pygame.K_LSHIFT

        }
        Player('player1', player_1_controle, player1_image_left, player1_image_right, 500, 500, self.player1_group, self.bullet, self.all_sprites)

        player2_image_left = load_image('player2_image_left.png', -1)
        player2_image_right = load_image('player2_image_right.png', -1)
        player_2_controle = {
            'left': pygame.K_LEFT,
            'right': pygame.K_RIGHT,
            'jump': pygame.K_UP,
            'attack': pygame.K_RSHIFT

        }
        Player('player2', player_2_controle, player2_image_left, player2_image_right, 1000, 500, self.player2_group, self.bullet,self.all_sprites)

    def start_game(self):
            FPS = 60
            tick = 0
            clock = pygame.time.Clock()
            self.bullet = pygame.sprite.Group()
            self.all_sprites = pygame.sprite.Group()
            self.player1_group = pygame.sprite.Group()
            self.player2_group = pygame.sprite.Group()
            self.create_charackter()
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.exit_game(event)
                        run = False
                self.all_sprites.update()
                self.screen.fill((128, 166, 255))
                self.all_sprites.draw(self.screen)
                tick += 1
                clock.tick(FPS)
                pygame.display.flip()
            pygame.quit()

    def open_menu(self, type_menu):
        Menu(type_menu).start_menu(self.size_screen, self.screen, self.start_game)

    def exit_game(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
