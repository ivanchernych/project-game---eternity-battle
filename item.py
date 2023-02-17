import pygame
import sys
import os


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


class Item(pygame.sprite.Sprite):
    def __init__(self,  x, y, type):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        if type == 'p1':
            self.image = load_image('pltf.png', 1)
            self.rect = self.image.get_rect()
            self.rect = pygame.Rect(self.x, self.y, 50, 50)
            self.mask = pygame.mask.from_surface(self.image)
        elif type == 'st':
            self.image = load_image('st.png', 1)
            self.rect = self.image.get_rect()
            self.rect = pygame.Rect(self.x, self.y, 1700, 150)
            self.mask = pygame.mask.from_surface(self.image)
        elif type == 'h':
            self.image = load_image('h.png', -1)
            self.rect = self.image.get_rect()
            self.rect = pygame.Rect(self.x, self.y, 1700, 150)
            self.mask = pygame.mask.from_surface(self.image)








