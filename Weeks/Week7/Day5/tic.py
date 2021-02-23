# Exercise TicTacToe
print("Welcome to TIC TAC TOE!")
print("")

positions = {
    "pos1": "",
    "pos2": "",
    "pos3": "",
    "pos4": "",
    "pos5": "",
    "pos6": "",
    "pos7": "",
    "pos8": "",
    "pos9": "",
}
empty_positions = []


def empty(positions):
    for pos in positions.values():
        if pos == "":
            empty_positions.append(pos)


def gameboard(pos_player1, pos_player2, turn, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9):
    print(f"TIC TAC TOE")
    print(f"*********************")
    print(f"*   {pos1}  |  {pos2}  |  {pos3}   *")
    print(f"*  --- | --- | ---  *")
    print(f"*   {pos4}  |  {pos5}  |  {pos6}   *")
    print(f"*  --- | --- | ---  *")
    print(f"*   {pos7}  |  {pos8}  |  {pos9}   *")
    print(f"*********************")
    print("")
    print(f"Player {turn}'s turn...")
    print("")
    print("")

# def enter_position(row,column):
#     row = input("Enter row: ")
#     column = input("Enter column: ")
#     if row


print(empty(1))
print(gameboard(1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1))
