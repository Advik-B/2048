import pygame
import settings

from grid_helper import Grid

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


grid = Grid(
    size=(4, 4),
    pos=(100, 100),
    square_size=100,
    color=(255, 255, 255),
    line_width=6
)

print(grid.matrix)
grid.matrix = [
    [0, 2, 4, 0],
    [4, 0, 0, 2],
    [0, 4, 2, 0],
    [2, 0, 0, 4]
]
print(grid.matrix)

start_time = pygame.time.get_ticks()
# grid.move_animate(10, 10, duration=1)

BOUNDING_BOX = pygame.Rect(0, 0, *settings.DISPLAY_SIZE)
OLD_POS = (0, 0)

def game_event_processor(event: pygame.event.Event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            grid.move_animate(0, -1)
        if event.key == pygame.K_DOWN:
            grid.move_animate(0, 1)
        if event.key == pygame.K_LEFT:
            grid.move_animate(-1, 0)
        if event.key == pygame.K_RIGHT:
            grid.move_animate(1, 0)

    if event.type == pygame.KEYUP:

        if event.key == pygame.K_UP:
            grid.move_animate(0, -1)
        if event.key == pygame.K_DOWN:
            grid.move_animate(0, 1)
        if event.key == pygame.K_LEFT:
            grid.move_animate(-1, 0)
        if event.key == pygame.K_RIGHT:
            grid.move_animate(1, 0)

        if event.key == pygame.K_ESCAPE:
            is_running = False

while is_running:
    clock.tick(settings.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.VIDEORESIZE:
            # Check if the new size is valid
            if event.w / event.h != SCREEN_RATIO:
                continue
            settings.DISPLAY_SIZE = (event.w, event.h)
            BOUNDING_BOX = pygame.Rect(0, 0, *settings.DISPLAY_SIZE)
            window_surface = pygame.display.set_mode(settings.DISPLAY_SIZE, *args)
            grid.resize(
                int((settings.DISPLAY_SIZE[0] - 200) / 4),
                int((settings.DISPLAY_SIZE[1] - 200) / 4)
            )
            grid.move(
                int((settings.DISPLAY_SIZE[0] - grid.size[0] * grid.square_size) / 2),
                int((settings.DISPLAY_SIZE[1] - grid.size[1] * grid.square_size) / 2)
            )
            print(grid.size)

        game_event_processor(event)

    window_surface.fill((0, 0, 0))
    grid.draw_on(window_surface)
    grid.update()
    pygame.display.update()

