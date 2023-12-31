import pygame
import settings
import time

class StartupAnimation:
    def __init__(self, surface: pygame.surface, size: tuple, pos: tuple, on_done: callable = None):
        self.surface = surface
        self.size = size # Screen size
        self.pos = pos
        # A typing animation
        self.head_text = settings.STARTUP_TEXT
        self.body_text = settings.STARTUP_SUBTEXT
        self.head_font = pygame.font.Font(f"{settings.FONT_DIR}/{settings.STARTUP_TEXT_FONT}", 100)
        # Calculate the appropriate font size for the body text and the head text based on the screen size
        self.body_font_size = int(self.size[1] / 20)
        self.head_font_size = int(self.size[1] / 10)
        self.body_font = pygame.font.Font(f"{settings.FONT_DIR}/{settings.STARTUP_SUBTEXT_FONT}", self.body_font_size)
        self.head_text_surface = self.head_font.render(settings.STARTUP_TEXT, True, settings.STARTUP_TEXT_COLOR)
        self.body_text_surface = self.body_font.render("", True, settings.STARTUP_SUBTEXT_COLOR)
        self.until_index = 0
        pygame.mixer.music.load(f"{settings.SOUND_DIR}/{settings.STARTUP_KEYBOARD_SOUND}")
        pygame.mixer.music.play()
        self.done = False
        self.on_done: callable = on_done
        self.texts = []
        for line in settings.STARTUP_SUBTEXT.split("\n"):
            self.texts.append(line.strip())

    def draw(self):
        if self.done:
            return
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
        if self.done:
            return False
        # Animate the typing
        if self.until_index < len(self.texts):
            self.body_text_surface = self.body_font.render(self.texts[self.until_index], True, settings.STARTUP_SUBTEXT_COLOR)
            self.until_index += 1
            pygame.mixer.music.play()
            time.sleep(1)
            return True

        self.done = True
        if self.on_done is not None:
            self.on_done()
        time.sleep(1)
        return False



if __name__ == "__main__":
    print("This file is not meant to be run directly. Please run main.py instead.")
    pygame.init()
    screen = pygame.display.set_mode(settings.DISPLAY_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption("Startup Animation")
    startup_animation = StartupAnimation(screen, settings.DISPLAY_SIZE, (0, 0))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        screen.fill(settings.BACKGROUND_COLOR)
        running = startup_animation.update()
        startup_animation.draw()
        pygame.display.update()



    pygame.quit()
