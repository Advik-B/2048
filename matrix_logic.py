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
        if self.max_undo > 0 and len(self.state_stack) > self.max_undo:
            self.state_stack.pop(0)  # Remove the oldest state

    def undo(self) -> None:
        """
        Undo the last move by restoring the previous state from the state stack.
        """
        if self.state_stack:
            self.matrix = self.state_stack.pop()

    def apply_move(self, move_func) -> None:
        """
        Apply a move function to the matrix.
        """
        self.save_state()
        for row in self.matrix:
            move_func(row)

    def move_left(self) -> None:
        """
        Move the numbers to the left and merge adjacent numbers if they are equal.
        """
        def move_row_left(row):
            # Merge numbers if they are equal
            for i in range(3):
                if row[i] == row[i + 1] and row[i] != 0:
                    row[i] *= 2
                    row[i + 1] = 0

            # Shift numbers to the left
            temp_row = [num for num in row if num != 0]  # Remove zeros
            temp_row += [0] * (4 - len(temp_row))  # Pad with zeros
            row[:] = temp_row

        self.apply_move(move_row_left)

    def move_right(self) -> None:
        """
        Move the numbers to the right and merge adjacent numbers if they are equal.
        """
        def move_row_right(row):
            # Reverse the row, move left, and reverse back
            row.reverse()
            self.move_left()
            row.reverse()

        self.apply_move(move_row_right)

    def move_up(self) -> None:
        """
        Move the numbers up and merge adjacent numbers if they are equal.
        """
        self.transpose()
        self.move_left()
        self.transpose()

    def move_down(self) -> None:
        """
        Move the numbers down and merge adjacent numbers if they are equal.
        """
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

    def reset(self) -> list[list[int, int, int, int]]:
        """
        Reset the game board to its initial state.
        """
        for i, j in itertools.product(range(4), range(4)):
            self.matrix[i][j] = 0

        return self.matrix

    def calculate_smoothness(self) -> float:
        """
        Calculate the smoothness score for the current board state.
        """
        smoothness_score = 0

        for row in self.matrix:
            for col in range(3):
                if row[col] != 0 and row[col + 1] != 0:
                    smoothness_score -= abs(row[col] - row[col + 1])

        for col in range(4):
            for row in range(3):
                if self.matrix[row][col] != 0 and self.matrix[row + 1][col] != 0:
                    smoothness_score -= abs(self.matrix[row][col] - self.matrix[row + 1][col])

        return smoothness_score

    def calculate_monotonicity(self) -> float:
        """
        Calculate the monotonicity score for the current board state.
        """
        monotonicity_score = 0

        for row in self.matrix:
            if all(row[i] >= row[i + 1] for i in range(3)):
                monotonicity_score += sum(row[i] - row[i + 1] for i in range(3))
            elif all(row[i] <= row[i + 1] for i in range(3)):
                monotonicity_score += sum(row[i + 1] - row[i] for i in range(3))

        for col in range(4):
            column_values = [self.matrix[row][col] for row in range(4)]
            if all(column_values[i] >= column_values[i + 1] for i in range(3)):
                monotonicity_score += sum(column_values[i] - column_values[i + 1] for i in range(3))
            elif all(column_values[i] <= column_values[i + 1] for i in range(3)):
                monotonicity_score += sum(column_values[i + 1] - column_values[i] for i in range(3))

        return monotonicity_score

    def score(self) -> int:
        """
        Calculate the score for the current board state.
        """
        # First, flatten the matrix into a list
        flattened_matrix = [num for row in self.matrix for num in row]
        # Then, make a dictionary of the number of occurrences of each number
        num_occurrences = {num: flattened_matrix.count(num) for num in flattened_matrix}
        return sum(num * (value / 2) for num, value in num_occurrences.items())

    def calculate_heuristic_score(self, priority: str) -> float:
        """
        Calculate the heuristic score for the current board state.
        :param priority: The aspect to prioritize - "score" or "space".
        """
        # Factor weights for each heuristic component
        smoothness_weight = 0.1
        monotonicity_weight = 1.0
        empty_cells_weight = 2.7
        max_tile_weight = 1.0

        # Additional weights based on the chosen priority
        if priority == "score":
            score_weight = 1.0
            space_weight = 0.0
        elif priority == "space":
            score_weight = 0.0
            space_weight = 1.0

        # Smoothness score
        smoothness_score = self.calculate_smoothness()

        # Monotonicity score
        monotonicity_score = self.calculate_monotonicity()

        # Empty cells score
        empty_cells_score = len([(row, col) for row in range(4) for col in range(4) if self.matrix[row][col] == 0])

        # Max tile score
        max_tile_score = max(max(row) for row in self.matrix)

        return (
            smoothness_weight * smoothness_score
            + monotonicity_weight * monotonicity_score
            + empty_cells_weight * empty_cells_score
            + max_tile_weight * max_tile_score
            + score_weight * max_tile_score
            + space_weight  # Add score_weight component based on priority
            * empty_cells_score  # Add space_weight component based on priority
        )

    def autoplay(self, priority: str = "score"):
        """
        AI Autoplay function to make the best move based on the current matrix information.
        :param priority: The aspect to prioritize - "score" or "space".
        """
        if priority not in ["score", "space"]:
            raise ValueError("Invalid priority. Use 'score' or 'space'.")

        possible_moves = ['left', 'right', 'up', 'down']
        max_score = float('-inf')
        best_move = None

        # Save the current state before making any moves
        # self.save_state() # Not needed because it will take up undo stack space

        for move in possible_moves:
            # Make the move and get the resulting matrix
            self.apply_move(move)

            # Calculate the score for this move using the advanced heuristic function
            score = self.calculate_heuristic_score(priority)

            # Undo the move to revert the matrix back to the original state
            self.undo()

            # Update the best move if the score is higher
            if score > max_score:
                max_score = score
                best_move = move

        # Make the best move
        self.apply_move(best_move)
        # Return the best move direction and the score
        return best_move


    def spawn_customised(self, chance_of_numbers: dict) -> None | list[list[int, int, int, int]]:
        """
        Place a random number (given by chance_of_numbers) at an empty location on the board.
        :param chance_of_numbers: {2: 90, 4: 10}, {2: 80, 4: 20}, {2: 70, 4: 20, 8: 10} etc.
        """
        if self.is_full():
            return self.matrix

        while True:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            if self.matrix[row][col] == 0:
                self.matrix[row][col] = random.choices(list(chance_of_numbers.keys()), weights=list(chance_of_numbers.values()))[0]
                break

        return self.matrix

    def spawn(self) -> None | list[list[int, int, int, int]]:
        """
        Place a random number (2 or 4) at an empty location on the board.
        """
        if self.is_full():
            return self.matrix

        while True:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            if self.matrix[row][col] == 0:
                self.matrix[row][col] = random.choices([2, 4], weights=[90, 10])[0]
                break

        return self.matrix