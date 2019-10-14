# File: Minesweeper.py
# Name: George Trammell
# Start Date: 10/1/19
# End Date: 10/13/19
# Desc: Text-based Minesweeper using 2D arrays. Includes turn count and various unicode characters. The program is split into several functions
#       for organization and readability. The hardest part of this project was finding a consistent and concise zero-clearing algorithm, and then
#       turning those cleared zeros into user-friendly unicode characters, which I eventually solved using a recurring grid search function and a
#       list comprehension.
# Sources: None (Beginning functions from class)
# On my honor, I have neither given nor received unauthorized aid.

import sys, random

#---------------------
# Functions
#---------------------

def add_mines(board): # randomly adds mines to board
    for i in range(mines):
        y = random.randint(1, height - 2)
        x = random.randint(1, width - 2)
        while board[y][x] == '💣':
            y = random.randint(1, height - 2)
            x = random.randint(1, width - 2)
        board[y][x] = '💣'
        increase_around_mines(x, y, board)

def increase_around_mines(x, y, board): # creates numbers around bombs
    for r in range(y - 1, y + 2):
        for c in range(x - 1, x + 2): # 3x3 grid search
            if board[r][c] != '💣':
                board[r][c] += 1

def print_answer_board(board): # prints solution board
    for i in board[1:-1]:
        print(*i[1:-1])

def print_player_board(board): # prints visibile board
    # sets zeros to empty box characters, nicer on the eyes
    m = -1
    for i in board:
        m+=1
        b = -1
        for x in i: # iterates through the the 2d array and uses m and b variables to keep track of index
            b+=1
            if x == 0:
                board[m][b] = '⌑' # sets board value at [m][b]

    for i in board[1:-1]: # prints board without gutters
        print(*i[1:-1])

def print_errorcheck(board): # prints board with gutters
    for i in board:
        print(*i)

def turn(): # main turn function
    global turnCount
    userInput = input_check() # user input
    x = int(userInput[0])
    y = int(userInput[1])
    turnCount += 1 # keeps track of user turns for reporting at the end

    if len(userInput) == 2: # reveal square
        if solution[y][x] == '💣': # user selects bomb, loses
            print('\n\nBOOM!')
            again = input('Would you like to play again? y/n: ').strip().lower()[0]
            if again == 'y':
                start_game() # restarts game, resets boards
            else:
                print('Thanks for playing!')
                sys.exit(1)

        elif solution[y][x] != 0: # basic number reveal
            playerBoard[y][x] = solution[y][x]
        elif solution[y][x] == 0:
            reveal_zero(x, y, solution)

    elif len(userInput) == 3: # flag or unflag
        if playerBoard[y][x] == '⊠':
            playerBoard[y][x] = '⚐'
        elif playerBoard[y][x] == '⚐':
            playerBoard[y][x] = '⊠'
        
def reveal_zero(x, y, board): # reveal zero algorithm
    for r in range(y - 1, y + 2):
        for c in range(x - 1, x + 2): # 3x3 grid around selection
            if playerBoard[r][c] == '⊠': # if unrevealed, reveal it
                playerBoard[r][c] = board[r][c]
                if board[r][c] == 0: # if another zero is found, call again
                    reveal_zero(c, r, solution)

def start_game(): # initiates boards, title card
    global solution
    global playerBoard
    global turnCount
    print('\n\n')
    print(' MINESWEEPER '.center(80, '*')) # title card
    print('\n\nWelcome to Minesweeper! Type two numbers with a space in between (x y) to guess a spot, \nor two numbers followed by an \'f\' (x y f) to place a flag.\n\n')
    solution = [[0]*width for i in range(height)] # empty board creations
    playerBoard = [['⊠']*width for i in range(height)]
    turnCount = 0
    add_mines(solution)
    for i in solution: # sets gutters to 1 to prevent indexing errors
        i[0] = 1
        i[-1] = 1
        solution[0] = [1 for i in solution[0]]
        solution[-1] = [1 for i in solution[-1]]
    for i in playerBoard: # sets gutters to 1 to prevent indexing errors (needed on the playerBoard so gutter zeros don't lead to unfairly-revealed squares)
        i[0] = 1
        i[-1] = 1
        playerBoard[0] = [1 for i in playerBoard[0]]
        playerBoard[-1] = [1 for i in playerBoard[-1]]
    print_player_board(playerBoard)
    gameflow()
    # turn()
    # print_player_board(playerBoard)

def input_check(): # checks user input for errors
    while True:
        userInput = input('>>> ').split()
        if (len(userInput) < 2) or (len(userInput) > 3): # checks for invalid length
            print('Please select a valid space.')
            continue
        try: # checks for invalid entry
            int(userInput[0])
            int(userInput[1])
        except ValueError:
            print('Please give a valid input.')
            continue
        try:
            solution[int(userInput[1])][int(userInput[0])]
        except IndexError:
            print('Please select a valid space.')
            continue
        else: # returns valid entry
            return userInput

def gameflow(): # runs the main game functions under a win condition
    while ((mines - (sum(row.count('⊠') for row in playerBoard) + sum(row.count('⚐')for row in playerBoard)))) != 0: # win condition
        turn()
        print_player_board(playerBoard)

#---------------------
# Main Code
#---------------------

# user assigned length/width/bomb count
height = int(sys.argv[1]) + 2
width = int(sys.argv[2]) + 2
mines = int(sys.argv[3])
if (height > 22) or (width > 22): # only 20x20 board allowed
    print('Please load the game with a valid board size (20x20 max).')
    sys.exit(1)
elif ((mines+1) > ((height - 2)*(width - 2))): # number of mines can't be greater than board area
    print('Please load the game with a plable amount of mines.')
    sys.exit(1)

turnCount = 0
solution = []
playerBoard = []

start_game() # initial game start

print('You won! You took %s turns. Thanks for playing!' % (turnCount))
again2 = input('Would you like to play again? y/n: ').strip().lower()[0] # play again on win
if again2 == 'y':
    start_game()
print('Thanks for playing!')
print('*' * 93) # end card