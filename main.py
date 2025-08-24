import pygame, time
from common.utils.debug_utils import draw_green_rect, draw_red_rect
from terrain.ground.ground import Ground
from terrain.pipe.pipe import Pipe
from terrain.shrubs.shrubs import Shrubs
from entities.player.player import Player
from settings import FPS, SKY_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT, DEBUG_MODE

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
prev_time = time.time()
running = True

terrain_group = pygame.sprite.Group()
ground = Ground("ground_tile.png")
ground_rects = ground.tiles
starting_pos_x, starting_pos_y = ground_rects[0].centerx, ground_rects[0].top

shrubs = Shrubs(starting_pos_y)
pipe = Pipe(ground_rects[0].bottom)

terrain_group.add(ground, pipe)
player = Player(starting_pos_x, starting_pos_y, terrain_group)

updatable = pygame.sprite.Group()
updatable.add(player)

drawable = pygame.sprite.Group()
drawable.add(player, ground, shrubs, pipe)

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

    for obj in sorted(drawable, key=lambda x: x.layer):
        obj.draw(screen)

        if DEBUG_MODE is False:
            continue
        if isinstance(obj, Player):
            draw_green_rect(screen, obj.rect)
        if isinstance(obj, Pipe):
            draw_red_rect(screen, obj.rect)

    pygame.display.flip()
    dt = clock.tick(FPS) / 1000

pygame.quit()
