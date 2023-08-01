import random

import pygame

import settings
from grid_helper import Grid
from startup import StartupAnimation
from controls_hint import ControlsHint

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


def play_music():
    global MUSIC_PLAYING
    print("Starting music...")
    music = pygame.mixer.Sound("audio/lofi.mp3")
    # Get the legnth of the audio
    music_length = music.get_length()
    # Load the audio
    pygame.mixer.music.load("audio/lofi.mp3")
    # Play the audio at a random position
    # Set the volume to 0.5

    pygame.mixer.music.set_volume(0.1)

    pygame.mixer.music.play(start=random.randint(0, int(music_length)))
    MUSIC_PLAYING = True
    grid.enabled = True
    controls_hint.enabled = True

def mute_music():
    global MUSIC_PLAYING
    if MUSIC_PLAYING:
        pygame.mixer.music.pause()
        MUSIC_PLAYING = False
    else:
        pygame.mixer.music.unpause()
        MUSIC_PLAYING = True
def game_event_processor(event: pygame.event.Event):
    """

    :type event: pygame.event.Event
    """
    global is_running
    global grid
    global MUSIC_PLAYING
    if not grid.enabled:
        return
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            is_running = False

        elif event.key == pygame.K_r:
            grid.matrix = grid.logic.reset()
            grid.matrix = grid.logic.spawn()
            grid.game_over = False
            grid.update_font()

        elif event.key == pygame.K_m:
            # Mute/unmute the audio
            mute_music()

        elif event.key in settings.KEY_BINDINGS["up"]:
            grid.move_up()
            # Animate the movement of the grid using the move_animate method with GRID_POS as the old position
            # 5 pixel up
            grid.move_animate(
                GRID_POS[0],
                GRID_POS[1] - settings.GRID_MOVEMENT_INTENSITY,
                duration=settings.GRID_MOVEMENT_DURATION
            )



        elif event.key in settings.KEY_BINDINGS["down"]:
            grid.move_down()
            # Animate the movement of the grid using the move_animate method with GRID_POS as the old position
            # 5 pixel down
            grid.move_animate(
                GRID_POS[0],
                GRID_POS[1] + settings.GRID_MOVEMENT_INTENSITY,
                duration=settings.GRID_MOVEMENT_DURATION
            )

        elif event.key in settings.KEY_BINDINGS["left"]:
            grid.move_left()
            # Animate the movement of the grid using the move_animate method with GRID_POS as the old position
            # 5 pixel left
            grid.move_animate(
                GRID_POS[0] - settings.GRID_MOVEMENT_INTENSITY,
                GRID_POS[1], duration=settings.GRID_MOVEMENT_DURATION
            )


        elif event.key in settings.KEY_BINDINGS["right"]:
            grid.move_right()
            grid.move_animate(
                GRID_POS[0] + settings.GRID_MOVEMENT_INTENSITY,
                GRID_POS[1], duration=settings.GRID_MOVEMENT_DURATION
            )



    if event.type == pygame.KEYUP:

        FLATTENED_KEY_BINDINGS = [item for sublist in list(settings.KEY_BINDINGS.values()) for item in sublist]


        if event.key in FLATTENED_KEY_BINDINGS:
            # Animate the grid back to its original position
            grid.move_animate(GRID_POS[0], GRID_POS[1], duration=settings.GRID_MOVEMENT_DURATION)

        if event.key == pygame.K_ESCAPE:
            is_running = False


grid = Grid(
    size=(4, 4),
    pos=(100, 100),
    square_size=100,
    color=settings.GRID_COLOR,
    line_width=6,
    text_color=settings.TEXT_COLOR,
    surface=window_surface,
)

# startup_animation = StartupAnimation(
#     window_surface,
#     settings.DISPLAY_SIZE,
#     pos=(0, 0),
#     on_done=play_music,
# )

controls_hint = ControlsHint(
    window_surface,
    settings.DISPLAY_SIZE,
    pos=(0, 0)
)

start_time = pygame.time.get_ticks()
# grid.move_animate(10, 10, duration=1)

BOUNDING_BOX = pygame.Rect(0, 0, *settings.DISPLAY_SIZE)
OLD_POS = (0, 0)
MUSIC_PLAYING = True


GRID_POS = grid.pos

grid.matrix = grid.logic.spawn_customised(settings.CHANCE_OF_SPAWN_NUMBERS)
grid.matrix = grid.logic.spawn_customised(settings.CHANCE_OF_SPAWN_NUMBERS)

# TODO: Remove this in the release (and re-enable the startup animation)
play_music()

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
        controls_hint.event_processor(event)

    window_surface.fill(settings.BACKGROUND_COLOR)

    grid.update()
    # startup_animation.update()
    controls_hint.update()

    grid.draw()
    controls_hint.draw()
    # startup_animation.draw()

    pygame.display.update()
