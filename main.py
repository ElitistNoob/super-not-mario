import pygame, time
from entities.player.player import Player
from settings import FPS, SKY_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
prev_time = time.time()
running = True

start_x = screen.get_width() / 2
start_y = screen.get_height() / 2
ground_y = screen.get_height() - 200
player = Player(start_x, start_y)

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

updatable.add(player)

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
        obj.update(keys, dt, ground_y)

    player.draw(screen)

    pygame.display.flip()
    dt = clock.tick()

pygame.quit()
