import os
import pygame

from settings import SCREEN_HEIGHT, SCREEN_WIDTH


class Terrain(pygame.sprite.Sprite):
    def __init__(self, ground_type):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "terrain", ground_type))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.tiles = self._generate_tiles()

    def _generate_tiles(self):
        tiles = []
        for i in range(SCREEN_WIDTH // self.width +1):
            rect = self.image.get_rect(topleft=(i * self.width, SCREEN_HEIGHT - self.height))
            tiles.append(rect)

        return tiles
    
    def draw(self, screen):
        for tile in self.tiles:
            screen.blit(self.image, tile)
