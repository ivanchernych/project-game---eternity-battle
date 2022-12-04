import pygame

pygame.init()
FPS = 60
size = (860, 1080)
clock = pygame.time.Clock()

pygame.display.set_caption("eternity battle")
sc = pygame.display.set_mode(size)
sc.fill((255, 255, 255))

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill((255, 255, 255))
    pygame.display.update()
    clock.tick(FPS)

