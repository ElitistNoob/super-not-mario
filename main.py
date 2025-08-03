import os
import pygame
from settings import FPS, SKY_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

start_x = screen.get_width() / screen.get_width()
start_y = screen.get_height() / 2
player = Player(start_x, start_y)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY_COLOR)

    keys = pygame.key.get_pressed()
    screen.blit(player.get_current_sprite(keys), player.pos)

    if keys[pygame.K_ESCAPE]:
        running = False

    player.update(keys, dt, start_y)

    pygame.display.flip()
    dt = clock.tick(FPS) / 1000

pygame.quit()
