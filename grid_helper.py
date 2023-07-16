import pygame

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
    ):
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


    def draw_on(self, surface: pygame.surface):
        if self.game_over:
            surface.blit(
                self.game_over_text,
                (
                    self.pos[0] + self.size[0] * self.square_size / 2,
                    self.pos[1] + self.size[1] * self.square_size / 2
                )
            )

        # First, draw the grid lines
        for i in range(self.size[0] + 1):
            pygame.draw.line(
                surface,
                self.color,
                (self.pos[0] + i * self.square_size, self.pos[1]),
                (self.pos[0] + i * self.square_size, self.pos[1] + self.square_size * self.size[1]),
                self.line_width
            )

        for i in range(self.size[1] + 1):
            pygame.draw.line(
                surface,
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
                    surface.blit(text_surface, text_rect)



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

        self.update_font()
        if self.logic.is_full():
            self.game_over = True

    def update_font(self):
        # Find out the maximum number in the grid
        max_num = 0
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.matrix[j][i] > max_num:
                    max_num = self.matrix[j][i]

        # Find out the number of digits in the maximum number
        num_digits = len(str(max_num))
        # Now, find out the optimal font size for the text based on the number of digits and the square size
        font_size = int(self.square_size / num_digits)
        # Now, create a font object
        self.font = pygame.font.SysFont('Arial', font_size)




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


