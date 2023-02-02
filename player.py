import pygame
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, type, controles, image_left, image_right, xCord, yCord, item_group, *group):
        super().__init__(group[0], group[2])
        self.enemy = group[-1]
        self.me_group = group[0]
        self.all_sprite_group = group[2]
        self.bullet_group = group[1]
        self.item_group = item_group

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
        self.rect = pygame.Rect(xCord, yCord, 145, 210)
        self.speed = 4
        self.jumpCount = 10
        self.gravity = 0.25
        self.onGround = False
        self.x_speed = 0
        self.y_speed = 0
        self.hp = 10

    def controle(self):
        keys = pygame.key.get_pressed()
        if keys[self.controles['left']]:
            self.x_speed = -self.speed
            self.image = self.image_left
            self.side = 'left'
            self.mask = pygame.mask.from_surface(self.image)

        if keys[self.controles['right']]:
            self.x_speed = self.speed
            self.image = self.image_right
            self.side = 'right'
            self.mask = pygame.mask.from_surface(self.image)

        if keys[self.controles['jump']]:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.y_speed = -self.jumpCount

        if not self.onGround:
            self.y_speed += self.gravity

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.y_speed
        self.collide(0, self.y_speed)

        self.rect.x += self.x_speed  # переносим свои положение на xvel
        self.collide(self.x_speed, 0)

        if not(keys[self.controles['left']] or keys[self.controles['right']]): # стоим, когда нет указаний идти
            self.x_speed = 0

    def shoot(self):
        bullet = Bullet(self.rect.x, self.rect.y, self.side, 'bujhm', self.enemy, self.item_group)
        self.all_sprite_group.add(bullet)
        self.bullet_group.add(bullet)

    def collide(self, x, y):
        for p in self.item_group:
            if pygame.sprite.collide_rect(self, p):
                if x > 0:  # если движется вправо
                    self.rect.right = p.rect.left # то не движется вправо

                if x < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if y > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.y_speed = 0  # и энергия падения пропадает

                if y < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.y_speed = 0  # и энергия прыжка пропадает

    def update(self, *args):
        self.controle()

