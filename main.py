import pygame
import pygame_menu
from menu import Menu

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()

if __name__ == '__main__':
    pygame.init()
    size = width, height, = 800, 400
    screen = pygame.display.set_mode(size)
    Menu(screen)