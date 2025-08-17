import pygame

from entities.state import State


class Entity(pygame.sprite.Sprite):
    def __init__(self, x,y, width=32, height=32):
        super().__init__()

        self.state = State.IDLE
        self.frame_index = 0

        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.pos= pygame.math.Vector2(self.rect.center) 
        self.velocity = pygame.Vector2(0, 0)
        self.direction = pygame.math.Vector2()
        self.on_ground = False
