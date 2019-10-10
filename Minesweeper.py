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
    for i in playerBoard[1:-1]:
        print(*i[1:-1])

def print_errorcheck(board):
    for i in board:
        print(*i)

def turn():
    userInput = input('>>> ').split()
    x = int(userInput[0])
    y = int(userInput[1])
    print(solution[x][y]) # debug
    print(playerBoard[x][y]) # debug
    print_errorcheck(solution)
    if len(userInput) == 2:
        # reveal
        if solution[x][y] == '*':
            # end game
            pass
        elif solution[x][y] != 0:
            playerBoard[x][y] = solution[x][y]
        elif solution[x][y] == 0:
            reveal_zero(x, y, solution)

    elif len(userInput) == 3:
        # flag
        if playerBoard[x][y] == '៙':
            playerBoard[x][y] = '⚐'
        elif playerBoard[x][y] == '⚐':
            playerBoard[x][y] = '៙'
        
def reveal_zero(x, y, board):
    for r in range(y - 1, y + 2):
        for c in range(x - 1, x + 2):
            if playerBoard[c][r] == '៙':
                playerBoard[c][r] = board[c][r]
                if board[c][r] == 0:
                    reveal_zero(c, r, solution)


#---------------------
# Main Code
#---------------------

height = int(sys.argv[1]) + 2
width = int(sys.argv[2]) + 2
mines = int(sys.argv[3])

solution = [[0]*width for i in range(height)]
playerBoard = [['៙']*width for i in range(height)]

add_mines(solution)
print_answer_board(solution)
print_player_board(solution)
for i in solution:
    i[0] = 1
    i[-1] = 1
solution[0] = [1 for i in solution[0]]
solution[-1] = [1 for i in solution[-1]]
turn()
print_player_board(playerBoard)
turn()
print_player_board(playerBoard)