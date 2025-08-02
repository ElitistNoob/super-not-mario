import pygame
from settings import GRAVITY


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, sprites):
        super().__init__()
        self.sprites = sprites
        self.rect = self.sprites["standing"].get_rect()

        self.pos = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

        self.rect.topleft = self.pos
        self.speed = 200
        self.jump_strength = -400
        self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_strength
            self.on_ground = False

    def update(self, keys, dt, ground):
        self.velocity.x = 0

        if keys[pygame.K_d]:
            self.velocity.x += self.speed
        if keys[pygame.K_a]:
            self.velocity.x -= self.speed

        self.velocity.y += GRAVITY * dt
        self.pos += self.velocity * dt

        if self.pos.y >= ground + 200:
            self.pos.y = ground + 200
            self.velocity.y = 0
            self.on_ground = True

        self.rect.topleft = self.pos
