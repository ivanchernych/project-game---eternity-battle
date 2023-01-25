import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, side):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((9, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.y = y + 200
        self.rect.x = x + 222
        self.side = side
        self.speedy = 10

    def shot(self):
        if self.side == 'left':
            self.rect.x -= self.speedy
        if self.side == 'right':
            self.rect.x += self.speedy

    def update(self):
        self.shot()
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()