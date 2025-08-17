import os
import pygame
from common.utils.asset_loader import get_image_path, load_image
from terrain.terrain import Terrain
from common.utils.graphic_utils import scale_sprite


class Ground(Terrain):
    def __init__(self, name):
        path = get_image_path("assets", "terrain")
        scaled_image = scale_sprite(load_image(path, name))
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
