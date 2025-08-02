import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, sprites):
        super().__init__()
        self.sprites = sprites
        self.rect = self.sprites["standing"].get_rect()
        self.pos = pygame.Vector2(x, y)
        self.rect.topleft = self.pos
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_w]:
            self.pos.y -= self.speed
        if keys[pygame.K_s]:
            self.pos.y += self.speed
        if keys[pygame.K_d]:
            self.pos.x += self.speed
        if keys[pygame.K_a]:
            self.pos.x -= self.speed

        self.rect.topleft = self.pos
