import pygame, time
from entities.player.player import Player
from settings import FPS, SKY_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT
from terrain.terrain import Terrain

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
prev_time = time.time()
running = True

terrain = Terrain("ground_tile.png")
player = Player(screen.get_width() / 2, screen.get_height() /2, terrain)

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

updatable.add(player)
drawable.add(player, terrain)

while running:
    dt = time.time() - prev_time
    prev_time = time.time()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY_COLOR)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False

    for obj in updatable:
        obj.update(keys, dt)

    for obj in drawable:
        obj.draw(screen)

    pygame.display.flip()
    dt = clock.tick()

pygame.quit()
