import pygame
import settings
class StartupAnimation:
    def __init__(self, surface: pygame.surface, size: tuple, color: tuple, pos: tuple):
        self.surface = surface
        self.size = size # Screen size
        self.color = color # Color of the animation
        self.pos = pos
        # A typing animation
        self.main_text = "Welcome to 2048"