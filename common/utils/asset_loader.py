import os
import pygame


def get_image_path(*path_parts):
    return os.path.join(*path_parts)


def load_image(path, name):
    path = os.path.join(path, name)
    return pygame.image.load(path).convert_alpha()
