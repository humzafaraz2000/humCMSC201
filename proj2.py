# File: proj2.py
# Author: Humza Faraz
# Date: 11/6/18
# Section: 19
# E-mail: hfaraz1@umbc.edu
# Description: Connect 4 game

from random import randint
#constants for players' names
PLAYER1 = "X"
PLAYER2 = "O"

#Constant for empty space
EMPTY = "_"

#minimum height and width for board
MIN_SIZE = 5

#Decreases size of list to scan through when determining winner
#to keep index in bounds
LESS_LIST = 3

#Creates the blank board if width and length >= 5
def createBoard():
    height = int(input("Enter a height: "))
    while(height < MIN_SIZE):
        print ("Invalid! Height must be greater than or equal to 5")
        height = int(input("Enter a height: "))
    width = int (input("Enter a width: "))
    while (width < MIN_SIZE):
        print ("Invalid! Width must be greater than or equal to 5")
        width = int(input("Enter a width: "))
        
    #Creates board filled with empty spaces
    board = []
    while len(board) < height:
        boardCol = []
        while len(boardCol) < width:
            boardCol.append(EMPTY)
        board.append(boardCol)
        
    #Prints empty board
    row = 0
    while row < len(board):
        col = 0
        while col < len(board[row]):
            print(board[row][col], end = " ")
            col += 1
        print()
        row += 1

    return board

#Determines whether user wants to play a computer or another player
#Input: None
#Output: Opponent choice
def versus():
    computer = False
    opponent = input("Would you like to play against a computer?(y/n) ")
    while (opponent != "y" and opponent != "n"):
        print ("Invalid! Enter 'y' or 'n' ")
        opponent = input("Would you like to play against a computer?(y/n) ")
    if (opponent == "y"):
        computer = True
    else:
        computer = False
    return computer

#User inputs column choice and checks if it is valid
#Input: the board
#Ouput: the user's move location
def move(board):
    print ("Player 1 turn!")
    column = len(board[0])
    print ("Column choices: 1 -",column)
    choice = int(input("Enter column choice "))
    
    #Checks if board is full
    full = False
    count = 0
    fullCount = 0
    while count < len(board):
        if board[count][choice - 1] == PLAYER1 or \
           board[count][choice - 1] == PLAYER2:
            fullCount += 1
            count += 1
        else:
            count += 1
    if (fullCount == len(board[0])):
        full = True
        
    while choice not in range(1, (column + 1)) or full == True:
        if choice not in range(1, (column + 1)):
            print ("Invalid! Out of range!")
            choice = int(input("Enter column choice "))
        else:
            print ("Invalid! Column is full!")
            choice = int(input("Enter column choice "))
            full = False
            
    return choice
    
#changes board after player1's turn and prints board
#Input: choice location
#Output: board
def change(choice, board):
    #Adds player2's move
    count = 1
    while (board[len(board) - count][choice - 1] == PLAYER1 or \
           board[len(board) - count][choice - 1] == PLAYER2):
        count += 1
    board[len(board) - count][choice - 1] = PLAYER1
    
    #prints board after piece is added
    row = 0
    while row < len(board):
        col = 0
        while col < len(board[row]):
            print (board[row][col], end = " ")
            col += 1
        print ()
        row += 1
        
    return board

#Player2 or computer makes move
#Input: Opponent choice
#Output: Opponent's move
def move2(board, opponent):
    if opponent == False:
        print ("Player 2 turn!")
        column = len(board[0])
        print ("Column choices: 1 -",column)
        choice2 = int(input("Enter column choice "))
        
        #Checks if column is full
        full = False
        count = 0
        fullCount = 0
        while count < len(board):
            if board[count][choice2 - 1] == PLAYER1 or \
               board[count][choice2 - 1] == PLAYER2:
                fullCount += 1
                count += 1
            else:
                count += 1
        if (fullCount == len(board)):
            full = True
            
        while choice2 not in range(1,(column + 1)) or full == True:
            if choice2 not in range(1,(len(board)+1)):
                print ("Invalid choice! Column choices: 1 -",column)
            else:
                print ("Invalid! Column is full")
            choice2 = int(input("Enter column choice "))
            full = False
    else:
        print ("Computer's turn")
        choice2 = randint(0, len(board[0])-1)
        column = len(board[0])
        full = False
        count = 0
        fullCount = 0
        while count < len(board):
            if board[count][choice2] == PLAYER1 or \
               board[count][choice2] == PLAYER2:
                fullCount += 1
                count += 1
            else:
                count += 1
        if fullCount == len(board):
            full = True
        while full == True:
            choice2 = randint(0, len(board[0])-1)
            full = False
    print ("Computer chose column",choice2)
    return choice2

#prints the board after move has been made
#Input: the player's move
#Output: board after player's move has been made
def printBoard(loc2, board):
    #Adds player 2's piece
    count2 = 1
    while (board[len(board) - count2][loc2 - 1] == PLAYER1 or \
           board[len(board) - count2][loc2 - 1] == PLAYER2):
        count2 += 1
    board[len(board) - count2][loc2 - 1] = PLAYER2

    #Prints board after piece has been added
    row = 0
    while row < len(board):
        col = 0
        while col < len(board[row]):
            print (board[row][col], end = " ")
            col += 1
        print ()
        row += 1

    return board

#checks for a draw
#Input: board
#Output: if there's a draw
def draw(board):
    isDraw = False
    #checks for a draw
    count = 0
    while count < len(board):
        if EMPTY in board[count]:
            return isDraw
        else:
            count += 1
    isDraw = True
    return isDraw
#checks for winner
#Input: the board
#Output: whether there's a winner, draw, or neither
def winner(isDraw, board):
    if (isDraw == False):
        #Checks horizontally for winner
        for row in range(len(board)):
            for col in range(len(board[row]) - LESS_LIST):
                if (board[row][col] == board[row][col+1] \
                    == board[row][col+2] == board[row][col+3]) \
                    and (board[row][col] != EMPTY):
                    return board[row][col]

        #Checks vertically for winner
        for row in range(len(board) - LESS_LIST):
            for col in range (len(board[row])):
                if (board[row][col] == board[row+1][col] \
                    == board[row+2][col] == board[row+3][col]) \
                    and (board[row][col] != EMPTY):
                    return board[row][col]
            
        #Checks diagnonally left down to right
        for row in range(len(board) - LESS_LIST):
            for col in range (len(board[row]) - LESS_LIST):
                if (board[row][col] == board[row+1][col+1] \
                    == board[row+2][col+2] == board[row+3][col+3])\
                    and (board[row][col] != EMPTY):
                    return board[row][col]
            
        #Checks diagnoally left up to right
        for row in range (len(board) - LESS_LIST):
            for col in range (LESS_LIST, len(board[row])):
                if (board[row][col] == board[row+1][col-1]\
                    == board[row+2][col-2] == board[row+3][col-3])\
                    and (board[row][col] != EMPTY):
                    return board[row][col]

    return "None"
    
def main():
    print ("Welcome to Connect 4!")
    outcome = "None"
    isDraw = False
    
    #creates and prints blank board
    board = createBoard()

    #player plays against another player or computer
    opponent = versus()

    #while game hasn't finished
    #and draw = False and board isn't full
    while (outcome != PLAYER1 and outcome != PLAYER2 and isDraw == False):

        #player make moves and validates if the spot chosen is empty
        loc = move(board)
        
        #changes board after player1's move
        newBoard = change(loc, board)

        #checks for a draw
        isDraw = draw(board)
        
        #Checks for winner after player1's move
        outcome = winner(isDraw, newBoard)
        
        if (outcome != PLAYER1 and outcome != PLAYER2 and isDraw == False):
            #player2 or computer makes move
            loc2 = move2(board, opponent)

            #takes in player2's  move choice and adds them to board then
            #prints board
            finalBoard = printBoard(loc2, newBoard)

            #checks for a draw
            isDraw = draw(board)
            
            #checks if there's a winner
            outcome = winner(isDraw, finalBoard)

    if (outcome == PLAYER1):
        print ("Player 1 wins!")
        replay = input("Play again? (y/n)")
        if replay == "y":
            main()
    elif (outcome == PLAYER2):
        print ("Player 2 wins!")
        replay = input("Play again? (y/n)")
        if replay == "y":
            main()
    elif (isDraw == True):
        print ("It's a draw!")
        replay = input("Play again? (y/n)")
        if replay == "y":
            main()
main()
