# File: design3.txt
# Author: Humza Faraz
# Date: 12/4/18
# Section: 19
# E-mail: hfaraz1@umbc.edu
# Description: Sudoku game

# Constants
MIN_LENGTH = 1
MAX_LENGTH = 9

#prettyPrint() prints the board with row and column labels,
#              and spaces the board out so it looks nice
#Input:        board;     the square 2D game board (of integers) to print
#Output:       None;      prints the board in a pretty way
def prettyPrint(board):
    # print column headings and top border
    print("\n    1 2 3 | 4 5 6 | 7 8 9 ")
    print("  +-------+-------+-------+")

    for i in range(len(board)):
        # convert "0" cells to underscores  (DEEP COPY!!!)
        boardRow = list(board[i])
        for j in range(len(boardRow)):
            if boardRow[j] == "0":
                boardRow[j] = "_"
                
                
        # fill in the row with the numbers from the board
        print( "{} | {} {} {} | {} {} {} | {} {} {} |".format(i + 1,
                boardRow[0], boardRow[1], boardRow[2],
                boardRow[3], boardRow[4], boardRow[5],
                boardRow[6], boardRow[7], boardRow[8]))

        # the middle and last borders of the board
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")


#savePuzzle() writes the contents of the sudoku puzzle out
#             to a file in a comma seperated list
#Input:       board;      the square 2D game board (of integers) to write to a file
#Output:      fileName;   the name of the file to use for writing to
def savePuzzle(board, fileName):
    ofp = open(fileName, "w")
    for i in range(len(board)):
        rowStr = ""
        for j in range(len(board[i])):
            rowStr += str(board[i][j]) + ","
        # don't write the last comma to the file
        ofp.write(rowStr[ : len(rowStr)-1] + "\n")
    ofp.close()

#fileName() asks user for file name of board
#Input:     choice; the name of the file
#Output:    board; the 2D game board
def choiceFile(fileName):
    textFile = open(fileName)
    board = textFile.readlines()
    textFile.close()
    return board

#move()  Asks user if they want to play the game or solve the puzzle
#Input:  None
#Output: choice; the user's choice
def move():
    moveChoice = input("play number(p), save(s), undo(u), quit(q): ")
    return move

#solve() User tries to solve puzzle if they chose this option in move()
#Input:  choice; user's move choice from move() function
#Ouput:  result; whether user correctly solved puzzle or not
def check(row, col, solved, board):
    correct = True
    num = int(input("Enter a number to put in cell put in (" + str(row)+ \
                    "," + str(col) + ")"))
    board[row-1][col-1] = str(num)
    if solved[row-1][col-1] != board[row-1][col-1]:
        correct = False
        board[row-1][col-1] = "0"

    return correct
    
#play() User makes their play if they chose to in move()
#Input: None
#Ouput: board;  board after move has been made
def play(row, col, board):
    print("(If correct checker is on please enter the number one more time.)")
    num = int(input("Enter a number to put in cell put in (" + str(row)+ \
                    "," + str(col) + ")"))
    while num not in range (MIN_LENGTH, MAX_LENGTH + 1):
        print ("Invalid! Out of range.")
        num = int(input("Enter a number to put in cell put in (" + str(row)+ \
                        "," + str(col) + ")"))
    board[row-1][col-1] = num
    
#valid() checks if user's move choice is valid
#Input:     loc; user's move location
#Output:    validation; whether the user's move is valid or not
def valid(row,col, board):
    isValid = True
    if board[row-1][col-1] != "0":
        isValid = False

    return isValid
    
#winner() checks for a winner
#Input:   board;  the square 2D game board to compare to solved puzzle
#Ouput:   result; if there's a winner or not
def winner(board, solved):
    count = 0
    winner = False
    area = MAX_LENGTH * MAX_LENGTH
    for i in range(len(board)):
        for j in range (len(board)):
            if board[i][j] == solved [i][j]:
                count += 1
    if count == area:
        winner = True

    return winner
    
#correctCheck() user decides if they want correctness checker on or off
#Input:         None
#Output:        correctness; whether user wants the checker on or off
def correctCheck():
    check = input("Would you like correctness checker on (y/n)? ")
    while check != "y" and check != "n":
        print ("Invalid! Enter 'y' for yes and 'n' for no")
        check = input("Would you like correctness checker on (y/n)? ")
    return check


def main():
    fileName = input("Enter the name of the file you would like to open: ")
    openFile = open(fileName)
    board = openFile.readlines()
    openFile.close()
    
    prettyBoard = []
    for i in range(len(board)):
        row = []
        for j in range (len(board[i])):
            if board[i][j] != "\n" and board[i][j] != ",":
                row.append(board[i][j])
        prettyBoard.append(row)

    prettyPrint(prettyBoard)

    #opens solved puzzle
    baseSolved = fileName[0:7]
    solvedFile = baseSolved + "_solved.txt"
    openSolved = open(solvedFile)
    solved = openSolved.readlines()
    openSolved.close()

    prettySolved = []
    for i in range(len(solved)):
        row = []
        for j in range (len(board[i])):
            if solved[i][j] != "\n" and solved[i][j] != ",":
                row.append(solved[i][j])
        prettySolved.append(row)

    
    choice = input("Would you like to play(p) or solve(s)?")
    #if user chooses to play
    if (choice == "p"):
        correct = correctCheck()
        if correct == False:
            isCorrect = True
                
        win = False
        choice = input("play number(p), save(s), undo(u), quit(q): ")
        while (win == False and choice != "q"):
            
            #if user chooses to play
            if (choice == "p"):

                #user inputs row and column location of cell
                row = int(input("Enter row number (1-9): "))
                while row not in range(MIN_LENGTH, MAX_LENGTH + 1):
                    print("Invalid! out of range.")
                    row = int(input("Enter row number (1-9): "))
                col = int(input("Enter column number (1-9): "))
                while row not in range(MIN_LENGTH, MAX_LENGTH + 1):
                    print("Invalid! out of range.")
                    col = int(input("Enter column number (1-9): "))
                isValid = valid(row, col, prettyBoard)
                if correct == "y":
                    isCorrect = check(row, col, prettySolved, prettyBoard)    

                #input on whether user's input location was valid or not and if it's correct
                if isValid == False:
                    print("Invalid! Cell is already taken.")
                    choice = input("play number(p), save(s), undo(u), quit(q): ")
                elif isValid == True:
                    if isCorrect == True:
                        play(row, col, prettyBoard)
                        prettyPrint(prettyBoard)
                        win = winner(board, solved)
                        if win == False:
                            choice = input("play number(p), save(s), undo(u), quit(q): ")
                            #if user chooses to undo last move
                            if choice == "u":
                                prettyBoard[row-1][col-1] = "0"
                                prettyPrint(prettyBoard)
                                choice = input("play number(p), save(s), undo(u), quit(q): ")
                    elif isCorrect == False:
                        print("That isn't correct!")
                        choice = input("play number(p), save(s), undo(u), quit(q): ")

            #if user chooses to save
            elif (choice == "s"):
                print ("Saving...")
                savePuzzle(board, fileName)
                choice = input("play number(p), save(s), undo(u), quit(q): ")

            #if user chooses to undo again (first undo is in play statement)
            elif (choice == "u"):
                print ("Invalid! You can only undo the last move you did.")
                choice = input("play number(p), save(s), undo(u), quit(q): ")

            elif (choice == "q"):
                print ("Thanks for playing!")
                
    #if user chooses to see solution
    elif (choice == "s"):
        #print solution or solve rescursively
        print("Solution...")
        prettyPrint(prettySolved)
                    

main()
