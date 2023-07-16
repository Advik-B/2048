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
        self.small_font = pygame.font.Font(f"{settings.FONT_DIR}/{settings.STARTUP_TEXT_FONT}", 20)
        self.head_text_surface = self.head_font.render(settings.CONTROLS_TEXT, True, settings.STARTUP_TEXT_COLOR)
        self.enabled = False

        self.up_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['up'][0]}"
        self.down_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['down'][0]}"
        self.left_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['left'][0]}"
        self.right_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['right'][0]}"

        self.w_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['up'][1]}"
        self.a_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['left'][1]}"
        self.s_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['down'][1]}"
        self.d_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['right'][1]}"

        self.escape_i = f"{settings.IMAGE_DIR}/{settings.IMAGES['esc']}"
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

        self.controls_menu = pygame.Surface((self.size[0] - 100, self.size[1] - 100))
        self.controls_menu.fill(settings.BACKGROUND_COLOR)

    def draw(self):
        if not self.enabled:
            return
        # Draw the text on the bottom half of the screen

        self.surface.blit(
            self.head_text_surface,
            (
                self.pos[0] + self.size[0] / 2 - self.head_text_surface.get_width() / 2 + 200,
                self.pos[1] + self.size[1] / 2 - self.head_text_surface.get_height() - 300
            )
        )
        # Make a rectangle for the controls
        # Make the menu
        """
        W or UP: Move up
        S or DOWN: Move down
        A or LEFT: Move left
        D or RIGHT: Move right
        ESCAPE: Exit the game
        R: Reset the game
        M: Mute the game
        
        Just replace the "W" with the image of the key and so on
        """
        self.controls_menu.blit(
            self.a,
            (
                10,
                10
            )
        )
        self.controls_menu.blit(
            self.small_font.render("or", True, settings.STARTUP_TEXT_COLOR),
            (
                10 + self.a.get_width() + 10,
                10 + self.a.get_height() / 2 - self.small_font.get_height() / 2
            )
        )
        self.controls_menu.blit(
            self.left,
            (
                10 + self.a.get_width() + 10 + self.small_font.size("or")[0] + 10,
                10
            )
        )
        self.controls_menu.blit(
            self.small_font.render("Move left", True, settings.STARTUP_TEXT_COLOR),
            (
                10 + self.a.get_width() + 10 + self.small_font.size("or")[0] + 10 + self.left.get_width() + 10,
                10 + self.left.get_height() / 2 - self.small_font.get_height() / 2
            )
        )

        self.controls_menu.blit(
            self.d,
            (
                10,
                10 + self.a.get_height() + 10
            )
        )
        self.controls_menu.blit(
            self.small_font.render("or", True, settings.STARTUP_TEXT_COLOR),
            (
                10 + self.d.get_width() + 10,
                10 + self.a.get_height() + 10 + self.d.get_height() / 2 - self.small_font.get_height() / 2
            )
        )
        self.controls_menu.blit(
            self.right,
            (
                10 + self.d.get_width() + 10 + self.small_font.size("or")[0] + 10,
                10 + self.a.get_height() + 10
            )
        )
        self.controls_menu.blit(
            self.small_font.render("Move right", True, settings.STARTUP_TEXT_COLOR),
            (
                10 + self.d.get_width() + 10 + self.small_font.size("or")[0] + 10 + self.right.get_width() + 10,
                10 + self.a.get_height() + 10 + self.right.get_height() / 2 - self.small_font.get_height() / 2
            )
        )

        self.controls_menu.blit(
            self.w,
            (
                10,
                10 + self.a.get_height() + 10 + self.d.get_height() + 10
            )
        )
        self.controls_menu.blit(
            self.small_font.render("or", True, settings.STARTUP_TEXT_COLOR),
            (
                10 + self.w.get_width() + 10,
                10 + self.a.get_height() + 10 + self.d.get_height() + 10 + self.w.get_height() / 2 - self.small_font.get_height() / 2
            )
        )
        self.controls_menu.blit(
            self.up,
            (
                10 + self.w.get_width() + 10 + self.small_font.size("or")[0] + 10,
                10 + self.a.get_height() + 10 + self.d.get_height() + 10
            )
        )
        self.controls_menu.blit(
            self.small_font.render("Move up", True, settings.STARTUP_TEXT_COLOR),
            (
                10 + self.w.get_width() + 10 + self.small_font.size("or")[0] + 10 + self.up.get_width() + 10,
                10 + self.a.get_height() + 10 + self.d.get_height() + 10 + self.up.get_height() / 2 - self.small_font.get_height() / 2
            )
        )

        self.controls_menu.blit(
            self.s,
            (
                10,
                10 + self.a.get_height() + 10 + self.d.get_height() + 10 + self.w.get_height() + 10
            )
        )
        self.controls_menu.blit(
            self.small_font.render("or", True, settings.STARTUP_TEXT_COLOR),
            (
                10 + self.s.get_width() + 10,
                10 + self.a.get_height() + 10 + self.d.get_height() + 10 + self.w.get_height() + 10 + self.s.get_height() / 2 - self.small_font.get_height() / 2
            )
        )
        self.controls_menu.blit(
            self.down,
            (
                10 + self.s.get_width() + 10 + self.small_font.size("or")[0] + 10,
                10 + self.a.get_height() + 10 + self.d.get_height() + 10 + self.w.get_height() + 10
            )
        )
        self.controls_menu.blit(
            self.small_font.render("Move down", True, settings.STARTUP_TEXT_COLOR),
            (
                10 + self.s.get_width() + 10 + self.small_font.size("or")[0] + 10 + self.down.get_width() + 10,
                10 + self.a.get_height() + 10 + self.d.get_height() + 10 + self.w.get_height() + 10 + self.down.get_height() / 2 - self.small_font.get_height() / 2
            )
        )

        self.controls_menu.blit(
            self.mute,
            (
                10,
                10 + self.a.get_height() + 10 + self.d.get_height() + 10 + self.w.get_height() + 10 + self.s.get_height() + 10
            )
        )
        self.controls_menu.blit(
            self.small_font.render("Mute", True, settings.STARTUP_TEXT_COLOR),
            (
                10 + self.mute.get_width() + 10,
                10 + self.a.get_height() + 10 + self.d.get_height() + 10 + self.w.get_height() + 10 + self.s.get_height() + 10 + self.mute.get_height() / 2 - self.small_font.get_height() / 2
            )
        )

        # THe reset button is inlined with the mute button
        self.controls_menu.blit(
            self.reset,
            (
                10 + self.mute.get_width() + 10 + self.small_font.size("Mute")[0] + 10,
                10 + self.a.get_height() + 10 + self.d.get_height() + 10 + self.w.get_height() + 10 + self.s.get_height() + 10
            )
        )
        self.controls_menu.blit(
            self.small_font.render("Reset", True, settings.STARTUP_TEXT_COLOR),
            (
                10 + self.mute.get_width() + 10 + self.small_font.size("Mute")[0] + 10 + self.reset.get_width() + 10,
                10 + self.a.get_height() + 10 + self.d.get_height() + 10 + self.w.get_height() + 10 + self.s.get_height() + 10 + self.reset.get_height() / 2 - self.small_font.get_height() / 2
            )
        )


        # Make the controls menu appear right below the controls text
        self.surface.blit(
            self.controls_menu,
            (
                self.pos[0] + self.size[0] / 2 - self.head_text_surface.get_width() / 2 + 150,
                self.pos[1] + self.size[1] / 2 - self.head_text_surface.get_height() - 260
            )
        )


    def update(self):
        pass

    def event_processor(self, event):
        FLATTENED_KEY_BINDINGS = [item for sublist in list(settings.KEY_BINDINGS.values()) for item in sublist]
        if event.type == pygame.KEYDOWN:
            if event.key in FLATTENED_KEY_BINDINGS:
                if event.key == pygame.K_m:
                    tmp = self.mute_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.mute_i.split("/")[:-1])+"/" + tmp
                    self.mute = pygame.image.load(tmp)

                elif event.key == pygame.K_r:
                    tmp = self.reset_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.reset_i.split("/")[:-1])+"/" + tmp
                    self.reset = pygame.image.load(tmp)

                elif event.key == pygame.K_ESCAPE:
                    tmp = self.escape_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.escape_i.split("/")[:-1])+"/" + tmp
                    self.escape = pygame.image.load(tmp)

                elif event.key == pygame.K_UP:
                    tmp = self.up_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.up_i.split("/")[:-1])+"/" + tmp
                    self.up = pygame.image.load(tmp)

                elif event.key == pygame.K_DOWN:
                    tmp = self.down_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.down_i.split("/")[:-1])+"/" + tmp
                    self.down = pygame.image.load(tmp)

                elif event.key == pygame.K_LEFT:
                    tmp = self.left_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.left_i.split("/")[:-1])+"/" + tmp
                    self.left = pygame.image.load(tmp)

                elif event.key == pygame.K_RIGHT:
                    tmp = self.right_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.right_i.split("/")[:-1])+"/" + tmp
                    self.right = pygame.image.load(tmp)

                elif event.key == pygame.K_w:
                    tmp = self.w_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.w_i.split("/")[:-1])+"/" + tmp
                    self.w = pygame.image.load(tmp)

                elif event.key == pygame.K_a:
                    tmp = self.a_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.a_i.split("/")[:-1])+"/" + tmp
                    self.a = pygame.image.load(tmp)

                elif event.key == pygame.K_s:
                    tmp = self.s_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.s_i.split("/")[:-1])+"/" + tmp
                    self.s = pygame.image.load(tmp)

                elif event.key == pygame.K_d:
                    tmp = self.d_i.split("/")[-1]
                    tmp = f"_{tmp}"
                    tmp = "/".join(self.d_i.split("/")[:-1])+"/" + tmp
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
            



if __name__ == "__main__":
    print("This is a module, run main.py")
    pygame.init()
    screen = pygame.display.set_mode(settings.DISPLAY_SIZE)
    pygame.display.set_caption("Controls")

    controls = ControlsHint(screen, settings.DISPLAY_SIZE, (0, 0))
    controls.enabled = True
    while True:
        screen.fill(settings.BACKGROUND_COLOR)
        controls.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            controls.event_processor(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                break
        # controls.update()
        pygame.display.update()
