import pygame
import pygame_menu
from menu import Menu
import os
import sys


def start(sc):
    pass
    #run = True
    #while run:
    #    for event in pygame.event.get():  # error is here
    #        if event.type == pygame.QUIT:
    #            run = False
    #    pygame.display.flip()
    #pygame.quit()


if __name__ == '__main__':
    pygame.init()
    size = width, height, = 1920, 1080
    pygame.display.set_caption("eternity battle")
    screen = pygame.display.set_mode(size)
    ss = Menu(screen, size)
    Menu.start_menu(ss)