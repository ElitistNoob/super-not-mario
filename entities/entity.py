import pygame

from entities.state import State


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.state = State.IDLE
        self.frame_index = 0

        self.pos = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.direction = pygame.math.Vector2()
