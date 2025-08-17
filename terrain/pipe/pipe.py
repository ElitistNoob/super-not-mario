import pygame
from terrain.terrain import Terrain
from common.utils.graphic_utils import scale_sprite
from common.utils.asset_loader import get_image_path, load_image


class Pipe(Terrain):
    def __init__(self, ground_top, x_pos=None, layer=0):
        path = get_image_path("assets", "terrain")
        scaled_image = scale_sprite(load_image(path, "pipe.png"))
        screen_width = pygame.display.get_surface().get_width()

        super().__init__(scaled_image)
        self.ground = ground_top
        self.x_pos = x_pos if x_pos is not None else screen_width // 2
        self.layer = layer

        self.rect = self.image.get_rect(midbottom=(self.x_pos, self.ground))
        self.tiles = [self.rect]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
