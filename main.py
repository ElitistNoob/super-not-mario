import os
import pygame
from settings import FPS, SKY_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0


def load_sprites(type, name):
    path = os.path.join("assets", "sprites", type, name)
    return pygame.image.load(path).convert_alpha()


player_sprites = {"standing": load_sprites("mario", "small_mario_standing.png")}
start_x = screen.get_width() / 2
start_y = screen.get_height() / 2
player = Player(start_x, start_y, player_sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY_COLOR)
    screen.blit(player.sprites["standing"], player.rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    player.move(keys)

    pygame.display.flip()
    dt = clock.tick(FPS) / 1000

pygame.quit()
