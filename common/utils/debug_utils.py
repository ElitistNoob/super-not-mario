import pygame
from typing import Callable


def draw_rect(
    color: tuple[int, int, int],
) -> Callable[[pygame.Surface, pygame.Rect], pygame.Rect]:
    def fn(screen: pygame.Surface, rect: pygame.Rect) -> pygame.Rect:
        return pygame.draw.rect(screen, color, rect, 2)

    return fn


draw_green_rect = draw_rect((0, 255, 0))
draw_red_rect = draw_rect((255, 0, 0))
draw_blue_rect = draw_rect((0, 0, 255))
