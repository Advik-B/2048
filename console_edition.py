import settings
from matrix_logic import GameLogic
from copy import deepcopy

game = GameLogic(
    matrix=[
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
)


def help_msg():
    print("Welcome to 2048!")
    print("A game made by @Advik-B for Pratibha to distract her from her studies :)")
    print("Use the following keys to play:")
    print("u - move up")
    print("d - move down")
    print("l - move left")
    print("r - move right")
    print("h - help")
    print("Press Ctrl+C to exit the game")

def main():
    game.spawn_customised(settings.CHANCE_OF_SPAWN_NUMBERS)
    help_msg()
    game.display()


    while True:
        try:
            move = input("Enter move: ")
        except KeyboardInterrupt:
            break

        if move == "u":
            game.move_up()
        elif move == "l":
            game.move_left()
        elif move == "d":
            game.move_down()
        elif move == "r":
            game.move_right()
        elif move == "a":
            result = game.autoplay(priority=settings.AUTOPLAY_PRIORITY)
            print(f"Autoplay: {result[-1]}")
        elif move == "h":
            help_msg()
            continue
        else:
            print("Invalid move!")
            continue

        game.spawn_customised(settings.CHANCE_OF_SPAWN_NUMBERS)
        game.display()
        if game.is_full():
            print("Game over!")
            break

def play_against_myself():
    auto_play_choices = []
    max_same_choices = 100 # The higher this number, the more the game will try to make the same move over and over again.
    max_attempts = 100
    scores: dict[int, list[list[int, int, int, int]]] = {}
    for i in range(max_attempts):
        while len(auto_play_choices) < max_same_choices or any(
            auto_play_choices[-1] != x
            for x in auto_play_choices[-max_same_choices:]
        ):
            game.spawn_customised(settings.CHANCE_OF_SPAWN_NUMBERS)
            # game.display()


            result = game.autoplay(priority=settings.AUTOPLAY_PRIORITY)
            auto_play_choices.append(result[-1])

        print(f"Attempt {i+1} over!")
        # print(f"Score: {game.score()}")
        scores[game.score()] = deepcopy(game.matrix)
        # game.display()
        game.reset()
        game.spawn_customised(settings.CHANCE_OF_SPAWN_NUMBERS)
        auto_play_choices = []

    # print("Scores:")
    # for score, matrix in scores.items():
    #     print(f"{score}:")
    #     display_matrix(matrix)
    #     print()

    print("="*80)
    best_score = max(scores.keys())
    print(f"Best Score: {best_score}")
    display_matrix(scores[best_score])


def display_matrix(matrix):
    for row in matrix:
        for num in row:
            print(num, end="\t")
        print()


if __name__ == "__main__":
    # main()
    play_against_myself()