import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

BASE_WIDTH = 256
BASE_HEIGHT = 224


def scale_sprite(image):
    scale_x = (SCREEN_WIDTH // 2) / BASE_WIDTH
    scale_y = (SCREEN_HEIGHT // 2) / BASE_HEIGHT
    scale = min(scale_x, scale_y)

    scaled_width = int(image.get_width() * scale)
    scaled_height = int(image.get_height() * scale)

    return pygame.transform.scale(image, (scaled_width, scaled_height))
