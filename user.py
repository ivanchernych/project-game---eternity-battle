import pygame


class User:
    def __init__(self, xCord, yCord, sc):
        self.xCord = xCord
        self.yCord = yCord
        self.sc = sc
        self.jumpCount = 10  # высота прыжка
        self.isJump = False
        self.hp = 100

    def character_creation(self):
        pygame.draw.rect(self.sc, (255, 0, 0), (self.xCord, self.yCord, 40, 80))

    def user1(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.xCord -= 3
        if keys[pygame.K_d]:
            self.xCord += 3
        if not(self.isJump):
            if keys[pygame.K_SPACE]:
                self.isJump = True
        else:
            if self.jumpCount >= -10:
                self.yCord -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.isJump = False
