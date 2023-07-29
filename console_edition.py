import settings
from matrix_logic import GameLogic

game = GameLogic(
    matrix=[
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
)
game.spawn()

for i in range(4):
    game.spawn()

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
        result = game.autoplay(priority="space")
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

