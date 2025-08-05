import pygame
from entities.player.sprite_loader import load_player_sprites
from settings import GRAVITY
from entities.entity import Entity
from entities.state import State


class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.sprites = load_player_sprites()
        self.image = self.sprites[self.state][self.frame_index]
        self.rect = self.image.get_rect(center=self.pos)

        self.speed = 200
        self.jump_strength = -400
        self.is_moving = False
        self.on_ground = True

    def state_handler(self):
        previous_state = self.state

        if not self.on_ground:
            self.state = State.JUMPING
        elif self.is_moving:
            self.state = State.WALKING
        else:
            self.state = State.IDLE

        if self.state != previous_state:
            self.frame_index = 0

    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_strength
            self.on_ground = False

    def input(self, keys):
        if keys[pygame.K_d]:
            self.direction.x = 1
            self.is_moving = True
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.is_moving = True
        else:
            self.direction.x = 0
            self.is_moving = False

        if keys[pygame.K_SPACE]:
            self.jump()

    def draw(self, screen):
        image = self.image
        if self.direction.x == -1:
            image = pygame.transform.flip(self.image, True, False)
        screen.blit(image, self.pos)

    def update(self, keys, dt, ground_y):
        self.input(keys)

        if self.is_moving:
            self.frame_index += 1

        if self.frame_index >= len(self.sprites[self.state]):
            self.frame_index = 0

        self.velocity.y += GRAVITY * dt
        self.velocity.x = self.direction.x * self.speed
        self.pos += self.velocity * dt
        self.rect.center = self.pos

        if self.pos.y >= ground_y:
            self.pos.y = ground_y
            self.velocity.y = 0
            self.on_ground = True

        self.state_handler()
        self.image = self.sprites[self.state][self.frame_index]
