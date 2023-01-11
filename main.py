import pygame
from game import Game

if __name__ == '__main__':
    pygame.init()
    size = width, height, = 1920, 1080
    Game(size, caption='Eternity battle')

