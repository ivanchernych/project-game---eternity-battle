import pygame
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, type, controles, image_left, image_right, xCord, yCord, *group):
        super().__init__(*group)
        self.all_sprite_group = group[2]
        self.bullet_group = group[1]
        self.type = type
        self.side = ''
        self.controles = controles
        self.image_left = image_left
        self.image_right = image_right
        if self.type == 'player1':
            self.image = self.image_right
            self.rect = self.image.get_rect()
            self.side = 'right'
        elif self.type == 'player2':
            self.image = self.image_left
            self.rect = self.image.get_rect()
            self.side = 'left'
        self.rect.x = xCord
        self.rect.y = yCord
        self.speed = 4
        self.jumpCount = 10  # высота прыжка
        self.isJump = False
        self.hp = 100

    def controle(self):
        keys = pygame.key.get_pressed()
        if keys[self.controles['left']]:
            self.rect.x -= self.speed
            self.image = self.image_left
            self.side = 'left'
        if keys[self.controles['right']]:
            self.rect.x += self.speed
            self.image = self.image_right
            self.side = 'right'
        if not(self.isJump):
            if keys[self.controles['jump']]:
                self.isJump = True
        else:
            if self.jumpCount >= -10:
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.isJump = False
        if keys[self.controles['attack']]:
            bullet = Bullet(self.rect.x, self.rect.y, self.side, self.rect)
            self.all_sprite_group.add(bullet)
            self.bullet_group.add(bullet)

    def update(self, *args):
            self.controle()

