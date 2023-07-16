import pygame
import settings
class StartupAnimation:
    def __init__(self, surface: pygame.surface, size: tuple, color: tuple, pos: tuple):
        self.surface = surface
        self.size = size # Screen size
        self.color = color # Color of the animation
        self.pos = pos
        # A typing animation
        self.head_text = settings.STARTUP_TEXT
        self.body_text = settings.STARTUP_SUBTEXT
        self.head_font = pygame.font.Font(f"{settings.FONT_DIR}/{settings.STARTUP_TEXT_FONT}", 100)
        # Calculate the appropriate font size for the body text and the head text based on the screen size
        self.body_font_size = int(self.size[1] / 20)
        self.head_font_size = int(self.size[1] / 10)
        self.body_font = pygame.font.Font(f"{settings.FONT_DIR}/{settings.STARTUP_SUBTEXT_FONT}", self.body_font_size)
        self.head_text_surface = self.head_font.render(self.head_text, True, self.color)
        self.body_text_surface = self.body_font.render(self.body_text, True, self.color)

    def draw(self):
        self.surface.blit(
            self.head_text_surface,
            (
                self.pos[0] + self.size[0] / 2 - self.head_text_surface.get_width() / 2,
                self.pos[1] + self.size[1] / 2 - self.head_text_surface.get_height() / 2
            )
        )
        self.surface.blit(
            self.body_text_surface,
            (
                self.pos[0] + self.size[0] / 2 - self.body_text_surface.get_width() / 2,
                self.pos[1] + self.size[1] / 2 - self.body_text_surface.get_height() / 2 + self.head_text_surface.get_height()
            )
        )

    def update(self):
        # Animate the typing
        if len(self.head_text) < len(settings.STARTUP_TEXT):
            self.head_text = settings.STARTUP_TEXT[:len(self.head_text) + 1]
            self.head_text_surface = self.head_font.render(self.head_text, True, self.color)
        elif len(self.body_text) < len(settings.STARTUP_SUBTEXT):
            self.body_text = settings.STARTUP_SUBTEXT[:len(self.body_text) + 1]
            self.body_text_surface = self.body_font.render(self.body_text, True, self.color)
        else:
            return True