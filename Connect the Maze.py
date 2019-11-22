# File: Connect the Maze!
# Name: George Trammell
# Start Date: 11/7/19
# End Date: 11/21/19
# Desc: My own spin on the maze project: Connect the Maze! This program generates an a random maze with a
#       bit of a twist - the user must not only reach the end of the maze, but connect all the dots along the way.
#       I thought that this was a good way to spice up the regular maze experience, and it can
#       also be a way to compete against other players in a time trial or a minimum distance trial.
#
#       The beginning of this project was tough for me, as I tried to do as much work on my own as possible to
#       see what I was able to make without too much outside influence. I had a lot of fun thinking about various
#       implementations of Prim's Algorithm, and although I was eventually able to create a semi-functional text-based
#       draft, my original algorithm turned out to be too hard to translate to an actual visual maze. I sat down with a fresh
#       mind and redesigned my code based on the provided pseudocode and some help from my classmates, and I am thoroughly happy
#       with the result.
#
#
#####   This program is run using a single system dimension argument, as the maze can only be a square.
#####   The dimension argument is limited between 5 and 15 (inclusive).
#
#
# Sources: Prim's Algorithm learning (https://www.youtube.com/watch?time_continue=1&v=PzznKcMyu0Y&feature=emb_logo)
#          Pseudocode from Ms. Healey
#          Discussed many ideas with classmates, especially the implementation of Prim's Algorithm. Worked mainly with Marc, Liam, and Sam.
# On my honor, I have neither given nor received unauthorized aid.

import sys, random
from PIL import Image

#---------------------
# FUNCTIONS
#---------------------

def user_input_checker(): # checks the user system input, and lets the user retry if entered incorrectly
    global dim
    if dim < 5 or dim > 15: # limited between 5x5 and 15x15
        dim = int(input('Please enter a dimension between 5 and 15 (inclusive): ').strip())
        user_input_checker() # recursive call to check again

def create_board(): # creates a backend board full of random weights using a method similar to Minesweeper
	for x in range(1, dim + 1):
		for y in range(1, dim + 1):
			board[y][x] = random.randint(1, 9)

def create_user_board(imgx,imgy): # creates frontend board via PIL
	for w in range(0, dim): # for each step in the user-defined dimension,
		for x in range(0, imgx): # for all x pixel values,
			for y in range((w*50) - 3,(w*50) + 3): # paint a neon green grid across x axis; w, the outermost iterating variable, is scaled to the image dimensions, and is then used to draw the walls accurately.
				image.putpixel((x, y), (57, 253, 20))
	for w in range(0, dim):
		for y in range(0, imgy):
			for x in range((w*50) - 3,(w*50) + 3): # paint neon green grid across y axis
				image.putpixel((x, y), (57, 253, 20))

def pretty_print(board): # pretty printing function, for backend debugging and visuals
	for i in board[1:-1]:
		print(*i[1:-1])

def gather_nearbyNodes(x, y, board): # checks each of the surrounding nodes, and eventually passes them to Prim
    global nearbyNodes # list of nearby node weights
    global nearbyNodes_coords # list of those node's coordinate locations
    global vertical # vertical movement checker, decides which walls to break later
    board[y][x] = '+' # set board at location to 'visited'
    if (y, x) not in visitedNodes:
        visitedNodes.append((y, x)) # if the node isn't in the visit list, add it
    if board[y - 1][x] != '+': # checks each surrounding node, as long as it marked 'visited'
        up_down_left_right(x, y, board, 'up') # calls information function on that node
    if board[y + 1][x] != '+':
        up_down_left_right(x, y, board, 'down')
    if board[y][x + 1] != '+':
        up_down_left_right(x, y, board, 'right')
    if board[y][x - 1] != '+':
        up_down_left_right(x, y, board, 'left')
    end() # checks if all nodes have been visited, if so ends the game
    check_nearbyNodes(x, y) # calls Prim on the gathered information

def up_down_left_right(x, y, board, dir): # information function; adds info on each surrounding node to lists
    if dir == 'up': # gather the node above's info
        nearbyNodes.append(board[y - 1][x]) # weight
        nearbyNodes_coords.append((y - 1, x)) # coordinates
        vertical.append(1) # wall-breaking direction
    if dir == 'down': # gather the node below's info, etc.
        nearbyNodes.append(board[y + 1][x])
        nearbyNodes_coords.append((y + 1, x))
        vertical.append(0)
    if dir == 'left':
        nearbyNodes.append(board[y][x - 1])
        nearbyNodes_coords.append((y, x - 1))
        vertical.append(1)
    if dir == 'right':
        nearbyNodes.append(board[y][x + 1])
        nearbyNodes_coords.append((y, x + 1))
        vertical.append(0)

def check_nearbyNodes(x, y): # Prim's Algorithm; finds lowest weight node and breaks a wall
    global board
    global nearbyNodes
    global nearbyNodes_coords
    global vertical
    if len(nearbyNodes) == 0: # if all nearby nodes have been visited, jump to a different random location
        if x > 1 and y > 1 and x < dim and y < dim: # creates the 'connect the dots' idea and simultaneously prevents the program from being unsolvable
            destroy_wall(y, x, x-1, y, 'forward')
        randomProcessedNode = random.choice(visitedNodes) # random node choice
        nearbyNodes, nearbyNodes_coords, vertical = [], [], [] # reset lists
        gather_nearbyNodes(randomProcessedNode[0], randomProcessedNode[1], board) # recursive call on new random node
    else: # greedy algorithm; picks lowest-weighted node and destroys wall to get there
        targetNodeX = nearbyNodes_coords[nearbyNodes.index(min(nearbyNodes))][0]
        targetNodeY = nearbyNodes_coords[nearbyNodes.index(min(nearbyNodes))][1]
        if vertical[nearbyNodes.index(min(nearbyNodes))] == 0:
            destroy_wall(targetNodeX, targetNodeY, x, y, 'forward') # wall direction
        else:
            destroy_wall(targetNodeX, targetNodeY, x, y, 'backwards') # wall direction
        nearbyNodes, nearbyNodes_coords, vertical = [], [], [] # reset lists
        gather_nearbyNodes(targetNodeY, targetNodeX, board) # recursive function call

def destroy_wall(targetNodeX, targetNodeY, x, y, dir): # destroys the target walls
    global image
    if dir == 'forward':
        wallX1, wallY1 = ((y*50) - 47), ((x*50) - 47) # find the target wall
        wallX2, wallY2 = ((targetNodeX*50) - 3), ((targetNodeY*50) - 3)
    if dir == 'backwards': # find the target wall
        wallX1, wallY1 = ((targetNodeX*50) - 47), ((targetNodeY*50) - 47)
        wallX2, wallY2 = ((y*50) - 3), ((x*50) - 3)
    for x in range(wallX1, wallX2): # paints black over 'destroyed' wall
        for y in range(wallY1, wallY2):
            image.putpixel((x, y), (0, 0, 0))

def end(): # maze generation end function; creates start and end dots and finalizes program
    if len(visitedNodes) == ((dim**2)): # only triggers when every node has been visited
        for x in range(40, 60): # starting dot on (1, 1) node
            for y in range(40, 60):
                image.putpixel((x,y),(0, 180, 256))
        for x in range((imgx - 60),(imgx - 40)): # ending dot on (dim, dim) node
            for y in range((imgy - 60),(imgy - 40)):
                image.putpixel((x, y), (255, 120, 0))
        image.save("Connect the Maze, Trammell.png","PNG")
        print(' Complete. '.center(80, '*'), '\n\n') # end card
        quit()

#---------------------
# DEFINITIONS & EXECUTION
#---------------------

print('\n\n', ' Connect the Maze! '.center(80, '*')) # title card
print('\nWelcome to Connect the Maze! This program will generate a maze PNG file (called \nConnect the Maze) with several dots. The player(s) should start at the Blue dot, \nend at the Red dot, and connect every dot in between in either the minimum \ndistance or the fastest time. Doubling back on yourself is allowed when necessary. \n\nGood luck!\n') # game instructions

dim = int(sys.argv[1].strip()) # user-defined sqaure dimension, single argument
user_input_checker()
board = [['+']*(dim + 2) for i in range(dim + 2)] # empty board creation using list comprehension
visitedNodes = [] # list of nodes that the algorithm has already passed through
imgx, imgy = (dim * 50), (dim * 50) # image size, based on the user-defined grid
nearbyNodes, nearbyNodes_coords, vertical = [], [], [] # node lists for Prim's
image = Image.new("RGB", (imgx, imgy))


create_board()
board[1][1] = '+' # start generation at (1, 1)
create_user_board(imgx,imgy)
gather_nearbyNodes(1, 1, board) # start generation at (1, 1)

"""
Running Log of Classmate/Teacher Feedback:
- Try and create entrance and exit openings (REPLACED WITH START/END DOTS FOR CONNECT THE MAZE)
- Use Unicode characters for a good maze design (TRANSFERED TO PIL)
- Change colors to be more visible, higher contrast? (DONE)
- Thicker lines to be easier on the eyes (DONE)
- Maximum Maze Size Limit and Cubed Dimensions (DONE)
"""