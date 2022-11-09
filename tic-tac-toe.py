#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 
from turtle import position


board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    board[int(position)] = mark

# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard():
    print(' {} | {} | {} \n'.format(board[1], board[2], board[3]) +
    ' --------- \n' +
    ' {} | {} | {} \n'.format(board[4], board[5], board[6]) +
    ' --------- \n' +
    ' {} | {} | {} \n'.format(board[7], board[8], board[9]))

# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    #To ensure position is not >9 and <1
    if int(position) >= 1 and int(position) <= 9:
        #To ensure no duplicates
        if board[int(position)] == " ":
            return True
    return False

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 5, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 5, 7],
    [3, 6, 9]
]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    for x in winCombinations:
        if board[x[0]]==player and board[x[1]]==player and board[x[2]]==player:
            return True
    return False


# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    for x in board:
        if board[x] == " ":
            return False
    return True

#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'
x = 1

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
while not gameEnded:
    move = input(currentTurnPlayer + "'s turn, input: ")
    print(validateMove(move))
    if validateMove(move) == True:
        markBoard(move, currentTurnPlayer)
        printBoard()
        if checkWin(currentTurnPlayer)==True:
            print("Congratulations to "+currentTurnPlayer+" for winning this game!")
            print("Would you like to restart the game? Y/N")
            restart = input()
            if restart == "Y":
                board = board.fromkeys(board," ")
                gameEnded = False
            elif restart == "N":
                gameEnded = True
        else:
            if checkFull() == False:
                if currentTurnPlayer == "X":
                    currentTurnPlayer = "O"
                else:
                    currentTurnPlayer = "X"
            else:
                print("It's a tie! \nWould you like to restart the game? Y/N")
                restart = input()
                if restart == "Y":
                    board = board.fromkeys(board," ")
                    gameEnded = False
                elif restart == "N":
                    gameEnded = True
    else:
        move = input(currentTurnPlayer + "'s turn, input: ")
    

# Bonus Point: Implement the feature for the user to restart the game after a tie or game over
