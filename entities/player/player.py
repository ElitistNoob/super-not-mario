import pygame
from common.utils.scale_sprite import scale_sprite
from entities.player.sprite_loader import load_player_sprites
from settings import GRAVITY
from entities.entity import Entity
from entities.state import State

class Player(Entity):
    def __init__(self,x , y, terrain):
        super().__init__(x,y)
        self.terrain = terrain
        self.sprites = load_player_sprites()
        self.image = scale_sprite(self.sprites[self.state][self.frame_index])

        self.rect = self.image.get_rect(midbottom=(x,y))
        self.pos = pygame.Vector2(self.rect.center)

        self.speed = 200
        self.animation_speed = 5
        self.jump_strength = -400
        self.is_moving = False

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

    def move(self, dt, terrain_rects):
        self.velocity.y += GRAVITY * dt
        self.velocity.x = self.direction.x * self.speed
        self.pos += self.velocity * dt

        self.rect.center = round(self.pos)

        for tile in terrain_rects:
            if not self.rect.colliderect(tile):
                continue

            if self.velocity.y > 0 and self.rect.bottom >= tile.top:
                self.rect.bottom = tile.top
                self.velocity.y = 0
                self.on_ground = True

        self.pos = pygame.math.Vector2(self.rect.center)

    def animate(self, dt):
        if self.is_moving:
            self.frame_index += self.animation_speed * dt

        if self.frame_index >= len(self.sprites[self.state]):
            self.frame_index = 0

        self.image = scale_sprite(self.sprites[self.state][int(self.frame_index)])

    def draw(self, screen):
        image = self.image 
        if self.direction.x == -1:
            image = pygame.transform.flip(self.image, True, False)
        screen.blit(image, self.rect.topleft)

    def update(self, keys, dt, terrain_rects):
        self.input(keys)
        self.state_handler()
        self.animate(dt)
        self.move(dt, terrain_rects)
