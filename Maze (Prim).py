# George Trammell
# Prim's Algorithm
import random

board = [[0]*10 for i in range(10)]
height, width = range(10), range(10)
visitedNodes = []


def create_board():
    for y in height:
        for x in width:
            board[y][x] = random.randint(1,9)

def pretty_print():
    for i in board:
        print(*i)

create_board()
pretty_print()

def scan(board):
    for i in range(10):
        y = random.randint(1, 8)
        x = random.randint(1, 8)
        print(x, y, 'COORDS', board[y][x])
        prim(x, y, board)

def prim(x, y, board):
    lowestWeight = 10
    for r in range(y - 1, y + 2):
        for c in range(x - 1, x + 2):
            print(board[r][c], 'VALUE')
            if lowestWeight > board[r][c] and (c, r) not in visitedNodes:
                lowestWeight = board[r][c]
                targetNode = (c, r)
    print(targetNode, 'LOWEST NEAREST')
    visitedNodes.append(targetNode)
    return targetNode

print(scan(board))