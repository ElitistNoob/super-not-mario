import os
import pygame

from settings import SCREEN_HEIGHT, SCREEN_WIDTH


class Terrain(pygame.sprite.Sprite):
    def __init__(self, ground_type):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "terrain", ground_type))
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

    def get_ground(self):
        tiles = []
        for i in range(SCREEN_WIDTH // self.width +1):
            pos = (i * self.width, SCREEN_HEIGHT - self.height)
            tiles.append(pos)

        return tiles


    def draw(self, screen):
        tiles = self.get_ground()

        for tile in tiles:
            screen.blit(self.image, tile)
