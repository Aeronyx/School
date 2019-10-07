import sys, random

#---------------------
# Functions
#---------------------

def add_mines(board):
    for i in range(mines):
        y = random.randint(1, height - 2)
        x = random.randint(1, width - 2)
        while board[y][x] == '*':
            y = random.randint(1, height - 2)
            x = random.randint(1, width - 2)
        board[y][x] = '*'
        increase_around_mines(x, y, board)

def increase_around_mines(x, y, board):
    for r in range(y - 1, y + 2):
        for c in range(x - 1, x + 2):
            if board[r][c] != '*':
                board[r][c] += 1

def print_answer_board(board):
    for i in board[1:-1]:
        print(*i[1:-1])

def print_player_board(board):
    for i in board[1:-1]:
        playerBoard = ['៙' for i in solution]
        print(*playerBoard[1:-1])

# def create_player_board(board):
#     for row in playerBoard:
#         print(*playerBoard)
        

def print_errorcheck(board):
    for i in board:
        print(*i)

def turn():
    userInput = input('>>> ').split()
    print(playerBoard[2])
    print(playerBoard)
    print(playerBoard[int(userInput[1])][int(userInput[0])])
    if len(userInput) == 2:
        # reveal
        pass
    elif len(userInput) == 3:
        # flag
        if playerBoard[int(userInput[1])][int(userInput[0])] == '៙':
            playerBoard[int(userInput[1])][int(userInput[0])] == '⚐'
        elif solution[int(userInput[1])][int(userInput[0])] == '⚐':
            solution[int(userInput[1])][int(userInput[0])] == '៙'
        

#---------------------
# Main Code
#---------------------

height = int(sys.argv[1]) + 2
width = int(sys.argv[2]) + 2
mines = int(sys.argv[3]) 

solution = [[0]*width for i in range(height)]

add_mines(solution)
print_answer_board(solution)
print_player_board(solution)
# print_errorcheck(solution)
turn()
print_player_board(solution)