import pygame


class Terrain(pygame.sprite.Sprite):
    def __init__(self, image, layer=0):
        super().__init__()
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.tiles = []
        self.layer = layer

    def draw(self, screen):
        for tile in self.tiles:
            screen.blit(self.image, tile)
