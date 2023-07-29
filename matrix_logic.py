import itertools
import random
from copy import deepcopy

class GameLogic:
    def __init__(
        self,
        matrix: list[
            list[int, int, int, int],
            list[int, int, int, int],
            list[int, int, int, int],
            list[int, int, int, int]
        ],
        max_undo: int = 4
    ) -> None:
        self.matrix = matrix
        self.state_stack = []  # Stack to store previous states
        self.max_undo = max_undo

    def is_full(self) -> bool:
        """
        Check if the game board is full.
        """
        return all(0 not in row for row in self.matrix)

    def save_state(self) -> None:
        """
        Save the current state of the game board to the state stack.
        """
        self.state_stack.append(deepcopy(self.matrix))
        if 0 < self.max_undo < len(self.state_stack):
            self.state_stack.pop(0)  # Remove the oldest state

    def undo(self) -> None:
        """
        Undo the last move by restoring the previous state from the state stack.
        """
        if self.state_stack:
            self.matrix = self.state_stack.pop()

    def spawn(self) -> None | list[list[int, int, int, int]]:
        """
        Place a random number (2 or 4) at an empty location on the board.
        """
        if self.is_full():
            return self.matrix

        self.save_state()

        while True:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            if self.matrix[row][col] == 0:
                self.matrix[row][col] = random.choice([2, 4])
                break

        return self.matrix

    def spawn_customised(self, chance_of_numbers:dict):
        """
        Place a random number (given by chance_of_numbers) at an empty location on the board.
        :param chance_of_numbers: {2: 90, 4: 10}, {2: 80, 4: 20}, {2: 70, 4: 20, 8: 10} etc.
        """
        if self.is_full():
            return self.matrix

        self.save_state()

        while True:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            if self.matrix[row][col] == 0:
                self.matrix[row][col] = random.choices(list(chance_of_numbers.keys()), weights=list(chance_of_numbers.values()))[0]
                break

        return self.matrix

    def move_left(self) -> None:
        """
        Move the numbers to the left and merge adjacent numbers if they are equal.
        """
        self.save_state()

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

        return self.matrix

    def move_right(self) -> None:
        """
        Move the numbers to the right and merge adjacent numbers if they are equal.
        """
        self.save_state()

        # Reverse each row, move left, and reverse back
        for row in self.matrix:
            row.reverse()
        self.move_left()
        for row in self.matrix:
            row.reverse()

        return self.matrix

    def move_up(self) -> None:
        """
        Move the numbers up and merge adjacent numbers if they are equal.
        """
        self.save_state()

        # Transpose the matrix, move left, and transpose back
        self.transpose()
        self.move_left()
        self.transpose()
        return self.matrix

    def move_down(self) -> None:
        """
        Move the numbers down and merge adjacent numbers if they are equal.
        """
        self.save_state()

        # Transpose the matrix, move right, and transpose back
        self.transpose()
        self.move_right()
        self.transpose()
        return self.matrix

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

    def reset(self) -> list[list[int, int, int, int]]:
        """
        Reset the game board to its initial state.
        """
        for i, j in itertools.product(range(4), range(4)):
            self.matrix[i][j] = 0

        return self.matrix
