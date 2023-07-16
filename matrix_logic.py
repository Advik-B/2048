import random

class GameLogic:
    def __init__(
        self,
        matrix: list[
            list[int, int, int, int],
            list[int, int, int, int],
            list[int, int, int, int],
            list[int, int, int, int]
        ]
    ) -> None:
        self.matrix = matrix

    def is_full(self) -> bool:
        """
        Check if the game board is full.
        """
        for row in self.matrix:
            if 0 in row:
                return False
        return True

    def place_random_number(self) -> None:
        """
        Place a random number (2 or 4) at an empty location on the board.
        """
        if self.is_full():
            return

        while True:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            if self.matrix[row][col] == 0:
                self.matrix[row][col] = random.choice([2, 4])
                break

    def move_left(self) -> None:
        """
        Move the numbers to the left and merge adjacent numbers if they are equal.
        """
        for row in self.matrix:
            # Merge numbers if they are equal
            for i in range(3):
                if row[i] == row[i + 1] and row[i] != 0:
                    row[i] *= 2
                    row[i + 1] = 0

            # Shift numbers to the left
            temp_row = [num for num in row if num != 0]  # Remove zeros
            temp_row += [0] * (4 - len(temp_row))  # Pad with zeros
            row[:] = temp_row

    def move_right(self) -> None:
        """
        Move the numbers to the right and merge adjacent numbers if they are equal.
        """
        # Reverse each row, move left, and reverse back
        for row in self.matrix:
            row.reverse()
        self.move_left()
        for row in self.matrix:
            row.reverse()

    def move_up(self) -> None:
        """
        Move the numbers up and merge adjacent numbers if they are equal.
        """
        # Transpose the matrix, move left, and transpose back
        self.transpose()
        self.move_left()
        self.transpose()

    def move_down(self) -> None:
        """
        Move the numbers down and merge adjacent numbers if they are equal.
        """
        # Transpose the matrix, move right, and transpose back
        self.transpose()
        self.move_right()
        self.transpose()

    def transpose(self) -> None:
        """
        Transpose the matrix (rows become columns and vice versa).
        """
        self.matrix = [[self.matrix[j][i] for j in range(4)] for i in range(4)]

    def display(self) -> None:
        """
        Display the current state of the game board.
        """
        for row in self.matrix:
            for num in row:
                print(num, end="\t")
            print()

    def reset(self) -> None:
        """
        Reset the game board to its initial state.
        """
        for i in range(4):
            for j in range(4):
                self.matrix[i][j] = 0