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

        self.head_font = pygame.font.Font(f"{settings.FONT_DIR}/{settings.STARTUP_TEXT_FONT}", 40)
        self.head_text_surface = self.head_font.render(settings.CONTROLS_TEXT, True, settings.STARTUP_TEXT_COLOR)
        self.enabled = False

        self.up_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['up'][0]}"
        self.down_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['down'][0]}"
        self.left_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['left'][0]}"
        self.right_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['right'][0]}"

        self.w_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['w'][0]}"
        self.a_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['a'][0]}"
        self.s_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['s'][0]}"
        self.d_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['d'][0]}"

        self.escape_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['escape']}"
        self.reset_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['reset']}"
        self.mute_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['mute']}"

        self.up = pygame.image.load(self.up_i)
        self.down = pygame.image.load(self.down_i)
        self.left = pygame.image.load(self.left_i)
        self.right = pygame.image.load(self.right_i)

        self.w = pygame.image.load(self.w_i)
        self.a = pygame.image.load(self.a_i)
        self.s = pygame.image.load(self.s_i)
        self.d = pygame.image.load(self.d_i)

        self.escape = pygame.image.load(self.escape_i)
        self.reset = pygame.image.load(self.reset_i)
        self.mute = pygame.image.load(self.mute_i)


    def draw(self):
        if not self.enabled:
            return
        # Draw the text on the bottom half of the screen
        self.surface.blit(
            self.head_text_surface,
            (
                self.pos[0] + self.size[0] / 2 - self.head_text_surface.get_width() / 2,
                self.pos[1] + self.size[1] / 2 - self.head_text_surface.get_height() / 2 + 135
            )
        )


    def update(self):
        pass

    def process_event(self, event):
        FLATTENED_KEY_BINDINGS = [item for sublist in list(settings.KEY_BINDINGS.values()) for item in sublist]
        if event.key in FLATTENED_KEY_BINDINGS:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    tmp = self.mute_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.mute_i.split("/")[:-1]) + tmp
                    self.mute = pygame.image.load(tmp)

                elif event.key == pygame.K_r:
                    tmp = self.reset_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.reset_i.split("/")[:-1]) + tmp
                    self.reset = pygame.image.load(tmp)

                elif event.key == pygame.K_ESCAPE:
                    tmp = self.escape_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.escape_i.split("/")[:-1]) + tmp
                    self.escape = pygame.image.load(tmp)

                elif event.key == pygame.K_UP:
                    tmp = self.up_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.up_i.split("/")[:-1]) + tmp
                    self.up = pygame.image.load(tmp)

                elif event.key == pygame.K_DOWN:
                    tmp = self.down_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.down_i.split("/")[:-1]) + tmp
                    self.down = pygame.image.load(tmp)

                elif event.key == pygame.K_LEFT:
                    tmp = self.left_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.left_i.split("/")[:-1]) + tmp
                    self.left = pygame.image.load(tmp)

                elif event.key == pygame.K_RIGHT:
                    tmp = self.right_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.right_i.split("/")[:-1]) + tmp
                    self.right = pygame.image.load(tmp)

                elif event.key == pygame.K_w:
                    tmp = self.w_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.w_i.split("/")[:-1]) + tmp
                    self.w = pygame.image.load(tmp)

                elif event.key == pygame.K_a:
                    tmp = self.a_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.a_i.split("/")[:-1]) + tmp
                    self.a = pygame.image.load(tmp)

                elif event.key == pygame.K_s:
                    tmp = self.s_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.s_i.split("/")[:-1]) + tmp
                    self.s = pygame.image.load(tmp)

                elif event.key == pygame.K_d:
                    tmp = self.d_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.d_i.split("/")[:-1]) + tmp
                    self.d = pygame.image.load(tmp)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    self.mute = pygame.image.load(self.mute_i)

                elif event.key == pygame.K_r:
                    self.reset = pygame.image.load(self.reset_i)

                elif event.key == pygame.K_ESCAPE:
                    self.escape = pygame.image.load(self.escape_i)

                elif event.key == pygame.K_UP:
                    self.up = pygame.image.load(self.up_i)

                elif event.key == pygame.K_DOWN:
                    self.down = pygame.image.load(self.down_i)

                elif event.key == pygame.K_LEFT:
                    self.left = pygame.image.load(self.left_i)

                elif event.key == pygame.K_RIGHT:
                    self.right = pygame.image.load(self.right_i)

                elif event.key == pygame.K_w:
                    self.w = pygame.image.load(self.w_i)

                elif event.key == pygame.K_a:
                    self.a = pygame.image.load(self.a_i)

                elif event.key == pygame.K_s:
                    self.s = pygame.image.load(self.s_i)

                elif event.key == pygame.K_d:
                    self.d = pygame.image.load(self.d_i)
            



