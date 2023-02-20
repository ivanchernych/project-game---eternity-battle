import pygame
from bullet import Bullet
from item import Item

SPEED = 4
JUMP_COUNT = 10
GRAVITY = 0.25


class Player(pygame.sprite.Sprite):
    def __init__(self, type, controles, image_left, image_right, xCord, yCord, heart_player1, heart_player2,
                 player1_point, player2_point, item_group, *group):
        super().__init__(group[0], group[2])
        self.enemy = group[-1]
        self.me_group = group[0]
        self.all_sprite_group = group[2]
        self.bullet_group = group[1]
        self.item_group = item_group

        self.heart_player1 = heart_player1
        self.heart_player2 = heart_player2
        self.player1_point = player1_point
        self.player2_point = player2_point

        self.type = type
        self.side = ''
        self.controles = controles

        self.image_left = image_left
        self.image_right = image_right

        self.sides()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(xCord, yCord, 73, 100)

        self.onGround = False
        self.x_speed = 0
        self.y_speed = 0

    def sides(self):
        if self.type == 'player1':
            self.image = self.image_right
            self.rect = self.image.get_rect()
            self.side = 'right'
        elif self.type == 'player2':
            self.image = self.image_left
            self.rect = self.image.get_rect()
            self.side = 'left'

    def draw_heart(self):
        x = 260
        for _ in range(5):
            pl = Item(x, 795, 'heart')
            self.all_sprite_group.add(pl)
            self.heart_player1.append(pl)
            x += 30
        x = 1285
        for _ in range(5):
            pl = Item(x, 795, 'heart')
            self.all_sprite_group.add(pl)
            self.heart_player2.append(pl)
            x += 30

    def respawn(self):
        if self.type == 'player1':
            self.rect.x = 50
            self.rect.y = 600

        elif self.type == 'player2':
            self.rect.x = 1575
            self.rect.y = 600

    def controle(self):
        keys = pygame.key.get_pressed()
        if keys[self.controles['left']]:
            self.x_speed = -SPEED
            self.image = self.image_left
            self.side = 'left'
            self.mask = pygame.mask.from_surface(self.image)

        if keys[self.controles['right']]:
            self.x_speed = SPEED
            self.image = self.image_right
            self.side = 'right'
            self.mask = pygame.mask.from_surface(self.image)

        if keys[self.controles['jump']]:
            if self.onGround:
                self.y_speed = -JUMP_COUNT

        if not self.onGround:
            self.y_speed += GRAVITY

        self.onGround = False
        self.rect.y += self.y_speed
        self.collide(0, self.y_speed)

        self.rect.x += self.x_speed
        self.collide(self.x_speed, 0)

        if not (keys[self.controles['left']] or keys[self.controles['right']]):
            self.x_speed = 0

    def shoot(self):
        bullet = Bullet(self.rect.x, self.rect.y, self.side, self.type, self.enemy, self.item_group,
                        self.all_sprite_group,
                        self.heart_player1, self.heart_player2)
        self.all_sprite_group.add(bullet)
        self.bullet_group.add(bullet)

    def collide(self, x, y):
        for platform in self.item_group:
            if pygame.sprite.collide_rect(self, platform):
                if x > 0:
                    self.rect.right = platform.rect.left

                if x < 0:
                    self.rect.left = platform.rect.right

                if y > 0:
                    self.rect.bottom = platform.rect.top
                    self.onGround = True
                    self.y_speed = 0

                if y < 0:
                    self.rect.top = platform.rect.bottom
                    self.y_speed = 0

    def update(self):
        self.controle()
