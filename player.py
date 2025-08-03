import os
import pygame
from settings import GRAVITY


def load_sprites(char, variant, animation):
    path = os.path.join("assets", "sprites", char, variant, animation)
    return pygame.image.load(path).convert_alpha()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.state = "run"
        self.image_index = 0
        self.sprites = {
            "run": [
                load_sprites("mario", "small", "stand.png"),
                load_sprites("mario", "small", "run.png"),
            ],
            "jump": [load_sprites("mario", "small", "jump.png")],
        }
        self.rect = self.sprites[self.state][self.image_index].get_rect()

        self.pos = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

        self.rect.topleft = self.pos
        self.speed = 200
        self.jump_strength = -400
        self.on_ground = True
        self.is_moving = False

    def get_current_sprite(self, keys):
        image = pygame.transform.scale(
            self.sprites[self.state][self.image_index], (27, 27)
        )
        if keys[pygame.K_a]:
            image = pygame.transform.flip(image, True, False)

        return image

    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_strength
            self.on_ground = False

    def update(self, keys, dt, ground):
        self.velocity.x = 0

        if keys[pygame.K_d]:
            self.velocity.x += self.speed
            self.is_moving = True
        if keys[pygame.K_a]:
            self.velocity.x -= self.speed
            self.is_moving = True
        if keys[pygame.K_SPACE]:
            self.jump()

        if not self.on_ground:
            self.state = "jump"

        if self.is_moving:
            self.image_index += 1

        if self.image_index >= len(self.sprites[self.state]):
            self.image_index = 0

        self.velocity.y += GRAVITY * dt
        self.pos += self.velocity * dt

        if self.pos.y >= ground + 200:
            self.pos.y = ground + 200
            self.velocity.y = 0
            self.on_ground = True
            self.state = "run"

        self.is_moving = False
        self.rect.topleft = self.pos
