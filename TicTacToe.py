from colorama import Fore

def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices



# declare colors
# color of the cells
cellsColor = Fore.LIGHTCYAN_EX
Xcolor = Fore.LIGHTRED_EX
Ocolor = Fore.LIGHTBLUE_EX

def printBoard(boardList):
    # update the tick tac toe board
    line = "║ "
    print(cellsColor + f"╔═══╦═══╦═══╗")
    for i in range(0, 9):
        if (boardList[i][1] != 1):
            boardList[i] = (str(i),None)
            # boardList[i] = (" ",None)

        # rebuild the line based on color of the cell and X or O
        if boardList[i][1] == 1 and boardList[i][0] == 'X':
            line += Xcolor + boardList[i][0] + cellsColor + " ║ "
        elif boardList[i][1] == 1 and boardList[i][0] == 'O':
            line += Ocolor + boardList[i][0] + cellsColor + " ║ "
        else:
            line += boardList[i][0] + " ║ "


        if ((i+1) % 3 == 0):
            print(line)
            if (i+1) != 9:
                print(cellsColor + f"╠═══╬═══╬═══╣")
            else:
                print(cellsColor + f"╚═══╩═══╩═══╝")
            line = "║ "



def checkWin(boardList):

    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    playerX_indices = find_indices(boardList, ('X', 1))
    playerO_indices = find_indices(boardList, ('O', 1))

    # check if any of wins item is a subset of playerX_indices or playerO_indices
    if any(set(win).issubset(playerX_indices) for win in wins):
        printBoard(boardList)
        print(Fore.LIGHTYELLOW_EX, "X Won the match")
        return True
    elif any(set(win).issubset(playerO_indices) for win in wins):
        printBoard(boardList)
        print(Fore.LIGHTYELLOW_EX, "O Won the match")
        return True
    else:
        # check if all cells are filled and no one has won
        if all(boardList[i][1] == 1 for i in range(9)):
            printBoard(boardList)
            print(Fore.LIGHTYELLOW_EX, "Match Draw")
            return True

    return False



if __name__ == "__main__":

    boardList = []

    boardList = [("player",str(x)) for x in range(9)]

    players = ["O","X"]
    colors = [Ocolor, Xcolor]
    turn = True # 1 for X and 0 for O

    print(Fore.LIGHTYELLOW_EX + "Welcome to Tic Tac Toe")
    while (True):
        printBoard(boardList)

        print(colors[turn] + f"{players[turn]}'s Chance")

        value = int(input(colors[turn] + "Please enter a value: "))
        # check if the value is already taken
        if (boardList[value][1] == None):
            boardList[value] = (players[turn],1)
        else:
            print(Fore.GREEN,"Value already taken")
            continue

        if (checkWin(boardList)):
            print("Match over")
            break

        turn = not turn