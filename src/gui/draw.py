import pygame


def draw_rect(screen, color, rect, width=0, radius=0):
    pygame.draw.rect(screen, color, rect, width=width, border_radius=radius)