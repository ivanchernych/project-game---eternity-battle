import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, side, name_shooting, name_in_whom, item_group):
        pygame.sprite.Sprite.__init__(self)
        self.item_group = item_group
        self.image = pygame.Surface((30, 15))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.y = y + 155
        self.rect.x = x + 180
        self.side = side
        self.speedy = 10
        self.mask = pygame.mask.from_surface(self.image)
        self.name_shooting = name_shooting
        self.enemy = name_in_whom

    def shot(self):
        if self.side == 'left':
            self.rect.x -= self.speedy
        if self.side == 'right':
            self.rect.x += self.speedy

    def hit(self):
        for i in self.enemy:
            if pygame.sprite.collide_mask(self, i):
                self.kill()

    def update(self):
        self.hit()
        for i in self.item_group:
            if pygame.sprite.collide_rect(self, i):
                self.kill()
        self.shot()
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.x < 0 or self.rect.x > 1920:
            self.kill()