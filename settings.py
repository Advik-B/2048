from pygame.locals import (
    K_ESCAPE,
    K_r,
    K_m,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_s,
    K_a,
    K_d,
)

DISPLAY_SIZE = (600, 800)
VSYNC = True
ALLOW_RESIZE = False
FULLSCREEN = False

WINDOW_TITLE = '2048 - by Advik, for Pratibha'
FPS = 60

# Colors
BACKGROUND_COLOR = (250, 248, 239)
GRID_COLOR = (187, 173, 160)
TEXT_COLOR = (119, 110, 101)

# Key bindings
KEY_BINDINGS = {
    "reset": [K_r],
    "mute": [K_m],
    "up": [K_UP, K_w],
    "down": [K_DOWN, K_s],
    "left": [K_LEFT, K_a],
    "right": [K_RIGHT, K_d],
}

GRID_MOVEMENT_DURATION = 1
GRID_MOVEMENT_INTENSITY = 20
CHANCE_OF_SPAWN = 30
CHANCE_OF_SPAWN_NUMBERS = {
    2: 89,
    4: 20,
    8: 1,
}
