import pygame
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, type, controles, image_left, image_right, xCord, yCord, plfrm, *group):
        super().__init__(*group)
        self.all_sprite_group = group[2]
        self.bullet_group = group[1]
        self.platform = plfrm
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
        self.mask = pygame.mask.from_surface(self.image)
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
            self.mask = pygame.mask.from_surface(self.image)
        if keys[self.controles['right']]:
            self.rect.x += self.speed
            self.image = self.image_right
            self.side = 'right'
            self.mask = pygame.mask.from_surface(self.image)
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

    def shoot(self):
        bullet = Bullet(self.rect.x, self.rect.y, self.side, self.rect, self.platform)
        self.all_sprite_group.add(bullet)
        self.bullet_group.add(bullet)

    def fall(self):
        if pygame.sprite.spritecollideany(self, self.platform) is None:
            self.rect.y += self.speed

    def update(self, *args):
            self.fall()
            self.controle()

