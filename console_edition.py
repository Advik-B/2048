from matrix_logic import GameLogic

game = GameLogic(
    matrix=[
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
)
game.place_random_number()

for i in range(4):
    game.place_random_number()

game.display()

while True:
    move = input("Enter move: ")
    if move == "u":
        game.move_up()
    elif move == "l":
        game.move_left()
    elif move == "d":
        game.move_down()
    elif move == "r":
        game.move_right()
    else:
        print("Invalid move!")
        continue

    game.place_random_number()
    game.display()
    if game.is_full():
        print("Game over!")
        break

