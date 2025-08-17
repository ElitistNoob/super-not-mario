import os
import random
import pygame

from common.utils.scale_sprite import scale_sprite
from terrain.terrain import Terrain


class Shrubs(Terrain):
    def __init__(self, ground_top):
        image_path = os.path.join("assets", "terrain", "shrub.png")
        scaled_image = scale_sprite(pygame.image.load(image_path).convert_alpha())
        super().__init__(scaled_image)
        self.tiles = self._generate_shrubs(ground_top)

    def _generate_shrubs(self, ground_top):
        tiles = []
        screen_width = pygame.display.get_surface().get_width()
        screen_height = pygame.display.get_surface().get_height()

        for i in range(screen_width // self.width + 1):
            rect = self.image.get_rect(
                midbottom=(i * self.width * random.randint(1, 10), ground_top)
            )
            tiles.append(rect)

        return tiles
