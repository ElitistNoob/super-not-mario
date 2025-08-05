import os


def load_images(entity, variant):
    return os.path.join("assets", "sprites", entity, variant)
