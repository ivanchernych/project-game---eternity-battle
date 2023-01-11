import pygame


class User(pygame.sprite.Sprite):
    def __init__(self, image, xCord, yCord, *group):
        super().__init__(*group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = xCord
        self.rect.y = yCord
        self.speed = 3
        self.jumpCount = 10  # высота прыжка
        self.isJump = False
        self.hp = 100

    def controle(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if not(self.isJump):
            if keys[pygame.K_SPACE]:
                self.isJump = True
        else:
            if self.jumpCount >= -10:
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.isJump = False

    def update(self, *args):
        if args:
            self.controle(args[0])
