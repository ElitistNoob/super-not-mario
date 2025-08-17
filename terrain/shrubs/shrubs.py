import os
import random
import pygame

from common.utils.asset_loader import get_image_path, load_image
from common.utils.graphic_utils import scale_sprite
from terrain.terrain import Terrain


class Shrubs(Terrain):
    def __init__(self, ground_top):
        path = get_image_path("assets", "terrain")
        scaled_image = scale_sprite(load_image(path, "shrub.png"))
        super().__init__(scaled_image)
        self.tiles = self._generate_shrubs(ground_top)
        self.ground = ground_top
        self.layer = 0

    def _generate_shrubs(self, ground_top):
        tiles = []
        screen_width = pygame.display.get_surface().get_width()

        for i in range(screen_width // self.width + 1):
            rect = self.image.get_rect(
                midbottom=(i * self.width * random.randint(1, 10), ground_top)
            )
            tiles.append(rect)

        return tiles
