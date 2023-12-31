import itertools
import random

import pygame

import settings
from matrix_logic import GameLogic


class Grid:
    def __init__(
            self,
            size: tuple,
            pos: tuple,
            square_size: int,
            color: tuple = (255, 255, 255),
            line_width: int = 1,
            text_color: tuple = (255, 100, 255),
            surface: pygame.surface = None
    ):
        self.font: pygame.font.SysFont = None
        self.duration: int = None
        self.size = size
        self.pos = pos
        self.square_size = square_size
        self.color = color
        self.line_width = line_width
        self.goto = self.pos
        self.text_color = text_color

        self.matrix = [[0 for _ in range(self.size[0])] for _ in range(self.size[1])]
        self.update_font()
        self.logic = GameLogic(self.matrix)
        self.game_over_text = self.font.render(
            "Game Over",
            True,
            self.text_color
        )
        self.game_over = False
        self.enabled = False
        self.surface = surface
        self.autoplay = False

    def draw(self):
        if not self.enabled:
            return
        if self.game_over:
            self.surface.blit(
                self.game_over_text,
                (
                    self.pos[0] + self.size[0] * self.square_size / 2,
                    self.pos[1] + self.size[1] * self.square_size / 2
                )
            )

        # First, draw the grid lines
        for i in range(self.size[0] + 1):
            pygame.draw.line(
                self.surface,
                self.color,
                (self.pos[0] + i * self.square_size, self.pos[1]),
                (self.pos[0] + i * self.square_size, self.pos[1] + self.square_size * self.size[1]),
                self.line_width
            )

        for i in range(self.size[1] + 1):
            pygame.draw.line(
                self.surface,
                self.color,
                (self.pos[0], self.pos[1] + i * self.square_size),
                (self.pos[0] + self.square_size * self.size[0], self.pos[1] + i * self.square_size),
                self.line_width
            )

        # Then, draw the squares
        # for i in range(self.size[0]):
        #     for j in range(self.size[1]):
        #         pygame.draw.rect(
        #             surface,
        #             self.color,
        #             pygame.Rect(
        #                 self.pos[0] + i * self.square_size + self.line_width,
        #                 self.pos[1] + j * self.square_size + self.line_width,
        #                 self.square_size - self.line_width * 2,
        #                 self.square_size - self.line_width * 2
        #             )
        #         )

        # Then, draw the numbers in the squares

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.matrix[j][i] != 0:
                    text_surface = self.font.render(
                        str(
                            self.matrix[j][i]
                        ),
                        True,
                        self.text_color
                    )
                    text_rect = text_surface.get_rect()
                    text_rect.center = (
                        self.pos[0] + i * self.square_size + self.square_size / 2,
                        self.pos[1] + j * self.square_size + self.square_size / 2
                    )
                    self.surface.blit(text_surface, text_rect)



    def resize(self, *new_size: tuple):
        self.size = new_size

    def move(self, *new_pos: tuple):
        self.pos = new_pos

    def update(self):
        """
        Called every frame, to update the grid if needed
        :return:
        """
        if not self.enabled:
            return

        if self.pos != self.goto:
            time_delta = pygame.time.get_ticks() - self.start_time
            if time_delta > self.duration:
                self.pos = self.goto
            else:
                self.pos = (
                    self.pos[0] + (self.goto[0] - self.pos[0]) * (time_delta / self.duration),
                    self.pos[1] + (self.goto[1] - self.pos[1]) * (time_delta / self.duration)
                )


    def update_font(self):
        # Find out the maximum number in the grid
        max_num = 0
        for i, j in itertools.product(range(self.size[0]), range(self.size[1])):
            if self.matrix[j][i] > max_num:
                max_num = self.matrix[j][i]

        # Find out the number of digits in the maximum number
        num_digits = len(str(max_num))
        # Now, find out the optimal font size for the text based on the number of digits and the square size
        font_size = int(self.square_size / num_digits)
        # Now, create a font object
        self.font = pygame.font.SysFont('Arial', font_size)

    def change_matrix(self, new_matrix: list[list[int]]):
        self.matrix = new_matrix
        if self.logic.is_full():
            self.game_over = True

        # Spawn a new number in a random position (settings.CHANCE_OF_SPAWN)
        if random.randint(0, 100) <= settings.CHANCE_OF_SPAWN:
            self.logic.spawn_customised(settings.CHANCE_OF_SPAWN_NUMBERS)
        self.update_font()


    def move_up(self):
        self.change_matrix(self.logic.move_up())

    def move_down(self):
        self.change_matrix(self.logic.move_down())

    def move_left(self):
        self.change_matrix(self.logic.move_left())

    def move_right(self):
        self.change_matrix(self.logic.move_right())


    def move_animate(self, *new_pos: tuple, duration: int = 1):
        """
        Move the grid from current position to new position over a (specified) period of time
        :param new_pos: tuple of new position
        :param duration: time in seconds
        :return:
        """
        if self.pos == new_pos:
            return
        self.goto = new_pos
        self.start_time = pygame.time.get_ticks()
        self.duration = duration * 1000


    def set_square(self, pos: tuple, value: int):
        """
        Set the value of a square
        :param pos: tuple of position
        :param value: value to set
        :return:
        """
        self.matrix[pos[0]][pos[1]] = value


    def get_square(self, pos: tuple) -> int:
        """
        Get the value of a square
        :param pos: tuple of position
        :return:
        """
        return self.matrix[pos[0]][pos[1]]
