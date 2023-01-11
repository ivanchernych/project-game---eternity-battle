import sys
import pygame
from menu import Menu


class Game:

    def __init__(self, size_screen, caption):
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode(size_screen)
        self.size_screen = size_screen
        self.open_menu('main')

    def start_game(self):
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
