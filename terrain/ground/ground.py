import os
import pygame
from terrain.terrain import Terrain
from common.utils.scale_sprite import scale_sprite


class Ground(Terrain):
    def __init__(self, ground_type):
        image_path = pygame.image.load(os.path.join("assets", "terrain", ground_type))
        scaled_image = scale_sprite(image_path)
        super().__init__(scaled_image)
        self.tiles = self._generate_tiles()

    def _generate_tiles(self):
        tiles = []
        screen_width = pygame.display.get_surface().get_width()
        screen_height = pygame.display.get_surface().get_height()
        for i in range(screen_width // self.width + 1):
            rect = self.image.get_rect(
                topleft=(i * self.width, screen_height - self.height)
            )
            tiles.append(rect)

        return tiles
