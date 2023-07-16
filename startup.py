import pygame
import settings
import time

class StartupAnimation:
    def __init__(self, surface: pygame.surface, size: tuple, color: tuple, pos: tuple,
                 clock: pygame.time.Clock):
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
        self.clock = clock
        self.start_time = self.clock.get_time()
        self.until_index = 0

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
        if self.until_index < len(self.body_text):
            self.until_index += 1
            self.body_text_surface = self.body_font.render(self.body_text[:self.until_index], True, self.color)
            time.sleep(0.1)
            return False
        return True









if __name__ == "__main__":
    print("This file is not meant to be run directly. Please run main.py instead.")
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(settings.DISPLAY_SIZE, pygame.RESIZABLE)
    startup_animation = StartupAnimation(screen, settings.DISPLAY_SIZE, (255, 255, 255), (0, 0), clock)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        screen.fill((0, 0, 0))
        startup_animation.update()
        startup_animation.draw()
        pygame.display.update()



    pygame.quit()
