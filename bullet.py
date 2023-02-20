import pygame
import random

screen_rect = (0, 0, 1700, 850)


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    image = pygame.Surface((5, 5))
    image.fill((255, 0, 0))
    fire = [image]

    def __init__(self, pos, dx, dy, all_sprite_group):
        super().__init__(all_sprite_group)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = 0.10

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position, all_sprite_group):
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers), all_sprite_group)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, side, name_shooting, name_in_whom, item_group, all_sprite_group,
                 hp_heart_player1, hp_heart_player2):
        pygame.sprite.Sprite.__init__(self)
        self.item_group = item_group
        self.image = pygame.Surface((15, 8))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.y = y + 50
        self.rect.x = x + 36.5
        self.side = side
        self.speedy = 10
        self.mask = pygame.mask.from_surface(self.image)
        self.name_shooting = name_shooting
        self.enemy = name_in_whom
        self.all_sprite_group = all_sprite_group
        self.hp_heart_player1 = hp_heart_player1
        self.hp_heart_player2 = hp_heart_player2

    def shot(self):
        if self.side == 'left':
            self.rect.x -= self.speedy
        if self.side == 'right':
            self.rect.x += self.speedy

    def hit(self):
        for i in self.enemy:
            if pygame.sprite.collide_mask(self, i):
                pos = self.rect.x, self.rect.y
                create_particles(pos, self.all_sprite_group)
                if self.name_shooting == 'player1':
                    self.hp_heart_player2[-1].kill()
                    self.hp_heart_player2.remove(self.hp_heart_player2[-1])
                if self.name_shooting == 'player2':
                    self.hp_heart_player1[-1].kill()
                    self.hp_heart_player1.remove(self.hp_heart_player1[-1])
                self.kill()

    def update(self):
        self.shot()
        self.hit()
        if len(self.hp_heart_player1) == 0 or len(self.hp_heart_player2) == 0:
            self.kill()
        for i in self.item_group:
            if pygame.sprite.collide_rect(self, i):
                self.kill()
