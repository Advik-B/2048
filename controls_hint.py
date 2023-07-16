import pygame
import settings

class ControlsHint:
    def __init__(
            self,
            surface: pygame.surface,
            size: tuple,
            pos: tuple,

    ):
        self.surface = surface
        self.size = size # Screen size
        self.pos = pos

        self.head_font = pygame.font.Font(f"{settings.FONT_DIR}/{settings.STARTUP_TEXT_FONT}", 50)
        self.head_text_surface = self.head_font.render(settings.CONTROLS_TEXT, True, settings.STARTUP_TEXT_COLOR)

    def draw(self):
        # Draw the text on the bottom half of the screen
        self.surface.blit(
            self.head_text_surface,
            (
                self.pos[0] + self.size[0] / 2 - self.head_text_surface.get_width() / 2,
                self.pos[1] + self.size[1] / 2 - self.head_text_surface.get_height() / 2
            )
        )

    def update(self):
        pass



