import settings
from matrix_logic import GameLogic
from copy import deepcopy
from alive_progress import alive_bar
from time import sleep
from threading import Thread

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
    global auto_play_choices, scores_size_limit, game_running, scores
    auto_play_choices = []
    max_same_choices = 50 # The higher this number, the more the game will try to make the same move over and over again.
    max_attempts = 10000
    game_running = True
    scores_size_limit = 100
    # scores: dict[int, list[list[int, int, int, int]]] = {}
    scores = {}
    def max_attempts_background_cleanup():
        global scores_size_limit
        global game_running
        global scores
        while game_running:
            if len(scores) > scores_size_limit:
                # Trim the scores dict to only the top MAX_ATTEMPTS scores
                scores = dict(sorted(scores.items(), key=lambda x: x[0], reverse=True)[:scores_size_limit])
                # print(f"Chopped scores to {len(scores)}")
                sleep(1)
                continue

            else:
                # print(f"Current scores: {len(scores)}")
                sleep(1)
                continue



    background_thread = Thread(target=max_attempts_background_cleanup)
    background_thread.daemon = True
    background_thread.start()

    with alive_bar(max_attempts) as bar:
        for _ in range(max_attempts):
            while len(auto_play_choices) < max_same_choices or any(
                auto_play_choices[-1] != x
                for x in auto_play_choices[-max_same_choices:]
            ):
                game.spawn_customised(settings.CHANCE_OF_SPAWN_NUMBERS)
                # game.display()


                result = game.autoplay(priority=settings.AUTOPLAY_PRIORITY)
                auto_play_choices.append(result[-1])

            # print(f"Attempt {_+1} over!")
            # print(f"Score: {game.score()}")
            scores[game.score()] = deepcopy(game.matrix)
            # game.display()
            game.reset()
            bar()
            game.spawn_customised(settings.CHANCE_OF_SPAWN_NUMBERS)
            auto_play_choices = []

    # print("Scores:")
    # for score, matrix in scores.items():
    #     print(f"{score}:")
    #     display_matrix(matrix)
    #     print()

    # print("="*80)
    best_score = max(scores.keys())
    print()
    print(f"Best Score: {best_score}")
    display_matrix(scores[best_score])
    print(len(scores.keys()))
    game_running = False
    background_thread.join()
    # Trim the scores dict to only contain the best scores
    # This is done to reduce the size of the scores dict, which will save memory


def display_matrix(matrix):
    final_width = 4 * len(matrix[0]) + 1
    print(f"{'='*final_width:4}")
    for row in matrix:
        for element in row:
            print(f"{element:4}", end="")
        print()
    print(f"{'='*final_width:4}")



if __name__ == "__main__":
    global game_running
    # main()
    try:
        play_against_myself()
    except KeyboardInterrupt:
        game_running = False
        exit(0)