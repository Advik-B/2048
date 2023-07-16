import pygame


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


    def draw_on(self, surface: pygame.surface):
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


class GameLogic:

    def __init__(self, grid: Grid):
        self.g_matrix = grid.matrix
        self.g_size = grid.size

    def move_left(self):
        # Move all the tiles to the left
        # Example:
        """
        [2, 2, 2, 2] -> [4, 4, 0, 0]
        [2, 0, 2, 2] -> [4, 2, 0, 0]
        [2, 0, 0, 2] -> [4, 0, 0, 0]
        [0, 0, 0, 2] -> [2, 0, 0, 0]

        Merging is done if and ONLY if the tiles are the same
        """
        # First, move all the tiles to the left
        for i in range(self.g_size[0]):
            for j in range(self.g_size[1]):
                if self.g_matrix[i][j] == 0:
                    for k in range(j + 1, self.g_size[1]):
                        if self.g_matrix[i][k] != 0:
                            self.g_matrix[i][j] = self.g_matrix[i][k]
                            self.g_matrix[i][k] = 0
                            break

        # Now, merge the tiles
        for i in range(self.g_size[0]):
            for j in range(self.g_size[1] - 1):
                if self.g_matrix[i][j] == self.g_matrix[i][j + 1]:
                    self.g_matrix[i][j] *= 2
                    self.g_matrix[i][j + 1] = 0


    def move_right(self):
        # Move all the tiles to the right
        # Example:
        """
        [2, 2, 2, 2] -> [0, 0, 4, 4]
        [2, 0, 2, 2] -> [0, 0, 2, 4]
        [2, 0, 0, 2] -> [0, 0, 0, 4]
        [0, 0, 0, 2] -> [0, 0, 0, 2]

        Merging is done if and ONLY if the tiles are the same
        """
        # First, move all the tiles to the right
        for i in range(self.g_size[0]):
            for j in range(self.g_size[1] - 1, -1, -1):
                if self.g_matrix[i][j] == 0:
                    for k in range(j - 1, -1, -1):
                        if self.g_matrix[i][k] != 0:
                            self.g_matrix[i][j] = self.g_matrix[i][k]
                            self.g_matrix[i][k] = 0
                            break

        # Now, merge the tiles
        for i in range(self.g_size[0]):
            for j in range(self.g_size[1] - 1, 0, -1):
                if self.g_matrix[i][j] == self.g_matrix[i][j - 1]:
                    self.g_matrix[i][j] *= 2
                    self.g_matrix[i][j - 1] = 0

    def move_up(self):
        # Move all the tiles to the up
        # Example:
        """
        [2, 2, 2, 2] -> [4, 4, 0, 0]
        [2, 0, 2, 2] -> [4, 2, 2, 0]
        [2, 0, 0, 2] -> [4, 0, 0, 2]
        [0, 0, 0, 2] -> [2, 0, 0, 0]

        Merging is done if and ONLY if the tiles are the same
        """
        # First, move all the tiles to the up
        for i in range(self.g_size[0]):
            for j in range(self.g_size[1]):
                if self.g_matrix[j][i] == 0:
                    for k in range(j + 1, self.g_size[1]):
                        if self.g_matrix[k][i] != 0:
                            self.g_matrix[j][i] = self.g_matrix[k][i]
                            self.g_matrix[k][i] = 0
                            break

        # Now, merge the tiles
        for i in range(self.g_size[0]):
            for j in range(self.g_size[1] - 1):
                if self.g_matrix[j][i] == self.g_matrix[j + 1][i]:
                    self.g_matrix[j][i] *= 2
                    self.g_matrix[j + 1][i] = 0

    def move_down(self):
        # Move all the tiles to the down
        # Example:
        """
        [2, 2, 2, 2] -> [0, 0, 0, 2]
        [2, 0, 2, 2] -> [0, 0, 2, 4]
        [2, 0, 0, 2] -> [0, 0, 2, 0]
        [0, 0, 0, 2] -> [0, 0, 0, 2]

        Merging is done if and ONLY if the tiles are the same
        """
        # First, move all the tiles to the down
        for i in range(self.g_size[0]):
            for j in range(self.g_size[1] - 1, -1, -1):
                if self.g_matrix[j][i] == 0:
                    for k in range(j - 1, -1, -1):
                        if self.g_matrix[k][i] != 0:
                            self.g_matrix[j][i] = self.g_matrix[k][i]
                            self.g_matrix[k][i] = 0
                            break

        # Now, merge the tiles
        for i in range(self.g_size[0]):
            for j in range(self.g_size[1] - 1, 0, -1):
                if self.g_matrix[j][i] == self.g_matrix[j - 1][i]:
                    self.g_matrix[j][i] *= 2
                    self.g_matrix[j - 1][i] = 0