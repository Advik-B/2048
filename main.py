import pygame
import settings
import threading
import time
import math
import random

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

class Grid:
    def __init__(
            self,
            size: tuple,
            pos: tuple,
            square_size: int,
            color: tuple = (255, 255, 255),
            line_width: int = 1
    ):
        self.size = size
        self.pos = pos
        self.square_size = square_size
        self.color = color
        self.line_width = line_width
        self.goto = self.pos

        self.grid = [[0 for _ in range(self.size[0])] for _ in range(self.size[1])]


    def draw_on(self, surface: pygame.surface):
        pygame.draw.rect(
            surface, self.color,
            (
                self.pos[0],
                self.pos[1],
                self.size[0] * self.square_size,
                self.size[1] * self.square_size
            ),
            self.line_width - 1
        )

        for i in range(self.size[0]):
            pygame.draw.line(
                surface, self.color,
                (
                    self.pos[0] + i * self.square_size,
                    self.pos[1]
                ),
                (
                    self.pos[0] + i * self.square_size,
                    self.pos[1] + self.size[1] * self.square_size
                ),
                self.line_width
            )

        for i in range(self.size[1]):
            pygame.draw.line(
                surface, self.color,
                (
                    self.pos[0],
                    self.pos[1] + i * self.square_size
                ),
                (
                    self.pos[0] + self.size[0] * self.square_size,
                    self.pos[1] + i * self.square_size
                ),
                self.line_width
            )

    def resize(self, *new_size: tuple):
        self.size = new_size

    def move(self, *new_pos: tuple):
        self.pos = new_pos

    def update(self):
        """
        Called every frame, to update the grid if needed
        :return:
        """

        if self.pos != self.goto:
            time_delta = pygame.time.get_ticks() - self.start_time
            if time_delta > self.duration:
                self.pos = self.goto
            else:
                self.pos = (
                    self.pos[0] + (self.goto[0] - self.pos[0]) * (time_delta / self.duration),
                    self.pos[1] + (self.goto[1] - self.pos[1]) * (time_delta / self.duration)
                )


    def move_animate(self, *new_pos: tuple, duration: int = 1):
        """
        Move the grid from current position to new position over a (specified) period of time
        :param new_pos: tuple of new position
        :param duration: time in seconds
        :return:
        """
        self.goto = new_pos
        self.start_time = pygame.time.get_ticks()
        self.duration = duration * 1000

    def __repr__(self):
        return f"Grid(size={self.size}, pos={self.pos}, square_size={self.square_size}, color={self.color}, line_width={self.line_width})"


    def set_square(self, pos: tuple, value: int):
        """
        Set the value of a square
        :param pos: tuple of position
        :param value: value to set
        :return:
        """
        self.grid[pos[0]][pos[1]] = value

    def get_square(self, pos: tuple) -> int:
        """
        Get the value of a square
        :param pos: tuple of position
        :return:
        """
        return self.grid[pos[0]][pos[1]]

    




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

start_time = pygame.time.get_ticks()
# grid.move_animate(10, 10, duration=1)

BOUNDING_BOX = pygame.Rect(0, 0, *settings.DISPLAY_SIZE)

global TIME_DELTA
while is_running:
    TIME_DELTA = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    window_surface.fill((0, 0, 0))
    grid.draw_on(window_surface)
    grid.update()
    pygame.display.update()

