from grid_helper import Grid


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
