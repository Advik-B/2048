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
from textwrap import dedent

DISPLAY_SIZE = (1000, 750)
VSYNC = True
ALLOW_RESIZE = False
FULLSCREEN = False

WINDOW_TITLE = '2048 by Advik'
FPS = 60
STARTUP_TEXT = "2048"
STARTUP_SUBTEXT = dedent(
    """
    A game by Advik, for Pratibha
    To distract you from your work
    
    This took a whopping 18 hours to make
    """
)
# STARTUP_SUBTEXT = dedent(
#     """
#     A stupid ass game
#     that i work on for some reason

#    This took a whopping 18 hours to make
#     """
# )
CONTROLS_TEXT = "Controls"
STARTUP_SUBTEXT_FONT = "Averia.ttf"
STARTUP_TEXT_FONT = "Bungee.ttf"
STARTUP_KEYBOARD_SOUND = "keyboard.mp3"

FONT_DIR = "fonts"
SOUND_DIR = "audio"
IMAGE_DIR = "images"

# Colors
BACKGROUND_COLOR = (250, 248, 239)
GRID_COLOR = (187, 173, 160)
TEXT_COLOR = (119, 110, 101)
STARTUP_TEXT_COLOR = TEXT_COLOR
STARTUP_SUBTEXT_COLOR = (119, 110, 101)
GAME_OVER_COLOR = (238, 228, 218)


# Key bindings
KEY_BINDINGS = {
    "reset": [K_r],
    "mute": [K_m],
    "up": [K_UP, K_w],
    "down": [K_DOWN, K_s],
    "left": [K_LEFT, K_a],
    "right": [K_RIGHT, K_d],
}

IMAGES = {
    "reset": "R.png",
    "mute":"M.png",
    "up": ("UP.png", "W.png"),
    "down":("DOWN.png", "S.png"),
    "left":("LEFT.png", "A.png"),
    "right":("RIGHT.png", "D.png"),
    "esc": "ESC.png"
}




GRID_MOVEMENT_DURATION = 1
GRID_MOVEMENT_INTENSITY = 20
CHANCE_OF_SPAWN = 30 # 30% chance of spawning new number
CHANCE_OF_SPAWN_NUMBERS = {
    2: 89,
    4: 20,
    8: 1,
}

