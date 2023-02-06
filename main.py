import pygame
from game import Game

if __name__ == '__main__':
    pygame.init()
    size = width, height, = 1700, 850
    Game(size, caption='Eternity battle')