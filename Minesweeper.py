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
    for i in playerBoard:
        print(*i)

# def create_player_board(board):
#     for row in playerBoard:
#         print(*playerBoard)
        

def print_errorcheck(board):
    for i in board:
        print(*i)

def turn():
    userInput = input('>>> ').split()
    x = int(userInput[0])
    y = int(userInput[1])
    if len(userInput) == 2:
        # reveal
        print(solution[x][y])
        print_errorcheck(solution)
        if solution[x][y] == '*':
            # end game
            pass
        elif solution[x][y] != 0:
            playerBoard[x-1][y-1] = solution[x][y]
        elif solution[x][y] == 0:
            reveal_zero(x, y, solution)

    elif len(userInput) == 3:
        # flag
        if playerBoard[x-1][y-1] == '៙':
            playerBoard[x-1][y-1] = '⚐'
        elif playerBoard[x-1][y-1] == '⚐':
            playerBoard[x-1][y-1] = '៙'
        
def reveal_zero(x, y, board):
    for r in range(y - 1, y + 2):
        for c in range(x - 1, x + 2):
            print(r, c)
            playerBoard[r][c] = board[r][c]

#---------------------
# Main Code
#---------------------

height = int(sys.argv[1]) + 2
width = int(sys.argv[2]) + 2
mines = int(sys.argv[3])

solution = [[0]*width for i in range(height)]
playerBoard = [['៙']*(width - 2) for i in range(height - 2)]

add_mines(solution)
print_answer_board(solution)
print_player_board(solution)
# print_errorcheck(solution)
turn()
print_player_board(playerBoard)
turn()
print_player_board(playerBoard)