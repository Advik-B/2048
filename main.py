import pygame
import settings

pygame.init()

args = [settings.DISPLAY_SIZE]
if settings.VSYNC:
    args.append(pygame.DOUBLEBUF)

if settings.ALLOW_RESIZE:
    args.append(pygame.RESIZABLE)
if settings.FULLSCREEN:
    args.append(pygame.FULLSCREEN)
if settings.FULLSCREEN and settings.ALLOW_RESIZE:
    args.append(pygame.RESIZABLE)
SCREEN_RATIO = settings.DISPLAY_SIZE[0] / settings.DISPLAY_SIZE[1]


window_surface = pygame.display.set_mode(*args)
pygame.display.set_caption(settings.WINDOW_TITLE)


clock = pygame.time.Clock()
is_running = True

# First, draw a 4x4 grid of squares
# The squares should be consistent in size, but the grid should be able to be resized
# The squares should be centered in the grid
# The squares should be spaced evenly

def draw_grid(
        surface: pygame.surface,
        grid_size: tuple,
        square_size: int,
        line_width: int = 1,
        color: tuple = (255, 255, 255),
        pos: tuple = (0, 0),
):
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            pygame.draw.rect(
                surface,
                color,
                (
                    pos[0] + x * square_size,
                    pos[1] + y * square_size,
                    square_size,
                    square_size,
                ),
                line_width,
            )


while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    window_surface.fill((0, 0, 0))
    draw_grid(window_surface, (4, 4), 100, 6)
    pygame.display.update()

