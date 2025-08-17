import pygame, time
from terrain.ground.ground import Ground
from terrain.shrubs.shrubs import Shrubs
from entities.player.player import Player
from settings import FPS, SKY_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
prev_time = time.time()
running = True

ground = Ground("ground_tile.png")
ground_rects = ground.tiles
starting_pos_x, starting_pos_y = ground_rects[0].centerx, ground_rects[0].top

shrubs = Shrubs(starting_pos_y)
player = Player(starting_pos_x, starting_pos_y, ground)

updatable = pygame.sprite.Group()
updatable.add(player)

drawable = pygame.sprite.Group()
drawable.add(player, ground, shrubs)

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
        obj.update(keys, dt, ground_rects)

    for obj in sorted(drawable, key=lambda x: x.layer):
        obj.draw(screen)

    pygame.display.flip()
    dt = clock.tick(FPS) / 1000

pygame.quit()
