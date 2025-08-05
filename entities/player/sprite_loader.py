import os
import pygame
from common.utils.load_images import load_images
from entities.state import State


def load_image(path, image_url):
    full_path = os.path.join(path, image_url)
    return pygame.image.load(full_path).convert_alpha()


def load_player_sprites():
    base_path = load_images("mario", "small")
    return {
        State.IDLE: [load_image(base_path, "idle.png")],
        State.WALKING: [
            load_image(base_path, "walking0.png"),
            load_image(base_path, "walking1.png"),
        ],
        State.RUNNING: [
            load_image(base_path, "running0.png"),
            load_image(base_path, "running1.png"),
        ],
        State.JUMPING: [load_image(base_path, "jumping.png")],
    }
