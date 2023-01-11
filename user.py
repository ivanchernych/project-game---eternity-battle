import pygame


class User(pygame.sprite.Sprite):
    def __init__(self, image, xCord, yCord, *group):
        super().__init__(*group)
        self.image = image
        self.xCord = xCord
        self.yCord = yCord
        self.rect = self.image.get_rect()
        self.speed = 3
        self.jumpCount = 10  # высота прыжка
        self.isJump = False
        self.hp = 100

    def controle(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            self.xCord -= self.speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            self.xCord += self.speed
        if not(self.isJump):
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.isJump = True
        else:
            if self.jumpCount >= -10:
                self.yCord -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.isJump = False

    def update(self, *args):
        if args:
            self.controle(args[0])
