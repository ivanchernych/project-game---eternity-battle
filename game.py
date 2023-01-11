import sys
import os
import pygame
from menu import Menu
from user import User

class Game:

    def __init__(self, size_screen, caption):
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode(size_screen)
        self.size_screen = size_screen
        self.open_menu('main')

    def load_image(self, name, colorkey=None):
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

    def start_game(self):
            all_sprites = pygame.sprite.Group()
            player_group = pygame.sprite.Group()
            image = self.load_image("1.png", -1)
            User(image, 200, 200, player_group, all_sprites)
            run = True
            while run:
                for event in pygame.event.get():  # error is here
                    if event.type == pygame.QUIT:
                        run = False
                bg_color = (230, 230, 230)
                self.screen.fill(bg_color)
                pygame.display.flip()
            pygame.quit()

    def open_menu(self, type):
        Menu(type).start_menu(self.size_screen, self.screen, self.start_game)

    def exit_game(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
