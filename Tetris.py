# Load necessary libraries
import pygame
import random

 

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

 

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
 
# 
pygame.font.init()
 

# GLOBALS VARS
s_width = 800 # screen width
s_height = 700 # screen height
play_width = 300  # meaning 300 // 10 = 30 width per block; where we can play
play_height = 600  # meaning 600 // 20 = 20 height per block; where we can play
block_size = 30

BLACK = (0, 0, 0) # define color 'black'
WHITE = (255, 255, 255) # define color 'white'
RED = (255, 0, 0) # define color 'red'
GRAY = (128, 128, 128) # define color 'gray'
LIME = (0, 255, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
MAROON = (128, 0, 128)

top_left_x = (s_width - play_width) // 2 # Let's us deal with collision on the x axis
top_left_y = s_height - play_height # Let's us deal with collision on the y axis
 

 

# SHAPE FORMATS
 
# Creates the tetris shape for 'S'
S = [[
    '.....',
    '......',
    '..00..',
    '.00...',
    '.....'],
    [
    '.....',
    '..0..',
    '..00.',
    '...0.',
    '.....'
    ]]
 
# Creates the tetris shape for 'Z'
Z = [[
    '.....',
    '.....',
    '.00..',
    '..00.',
    '.....'],
    [
    '.....',
    '..0..',
    '.00..',
    '.0...',
    '.....'
    ]]
 
# Creates the tetris shape for 'I' (makes a bar)
I = [[
    '..0..',
    '..0..',
    '..0..',
    '..0..',
    '.....'],
    [
    '.....',
    '0000.',
    '.....',
    '.....',
    '.....'
    ]]
 
# Creates the tetris shape for 'O' (makes a square)
O = [[
    '.....',
    '.....',
    '.00..',
    '.00..',
    '.....'
    ]]
 
# Creates the tetris shape for 'J'
J = [[
    '.....',
    '.0...',
    '.000.',
    '.....',
    '.....'],
    [
    '.....',
    '..00.',
    '..0..',
    '..0..',
    '.....'],
    [
    '.....',
    '.....',
    '.000.',
    '...0.',
    '.....'],
    [
    '.....',
    '..0..',
    '..0..',
    '.00..',
    '.....'
    ]]
 
# Creates the tetris shape for 'L'
L = [[
    '.....',
    '...0.',
    '.000.',
    '.....',
    '.....'],
    [
    '.....',
    '..0..',
    '..0..',
    '..00.',
    '.....'],
    [
    '.....',
    '.....',
    '.000.',
    '.0...',
    '.....'],
    [
    '.....',
    '.00..',
    '..0..',
    '..0..',
    '.....']]
 
# Creates the tetris shape for 'T'
T = [[
    '.....',
    '..0..',
    '.000.',
    '.....',
    '.....'],
    [
    '.....',
    '..0..',
    '..00.',
    '..0..',
    '.....'],
    [
    '.....',
    '.....',
    '.000.',
    '..0..',
    '.....'],
    [
    '.....',
    '..0..',
    '.00..',
    '..0..',
    '.....']]
 

shapes = [S, Z, I, O, J, L, T] # List holds all shapes for easier indexing
shape_colors = [(LIME), (RED), (CYAN), (YELLOW), (ORANGE), (BLUE), (MAROON)] # List holds all block colors fro easier indexing
# index 0 - 6 represent shape
 

 

class Piece(object): 

    rows = 20  # y 
    columns = 10  # x

    def __init__(self, column, row, shape): # Gives the aspects of a various shape
        self.x = column 
        self.y = row 
        self.shape = shape # Picks a shape 
        self.color = shape_colors[shapes.index(shape)] # Takes the index of that shape and applies the color in the corresponding index place of the colors list
        self.rotation = 0 # Whenever click UP arrow key, increase this number by one (later in the code)
 

def create_grid(locked_pos={}):
    grid = [[(BLACK) for x in range(10)] for x in range(20)] # Create a list for every row in grid. Each 'sublist' will have 10 colors (10 squares, or rows, in each of 20 cols). All blocks are drawn in 'black'

    # Change the color from 'black' to whatever corresponding shape color that is 'locked' in position
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos: # If row and column piece is included in the locked grid position...
                c = locked_pos[(j, i)] # Make a key that is set to the value of that block.
                grid[i][j] = c # Take the corresponding block properties and assign it to the grid piece.
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions



def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == BLACK] for i in range(20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]

    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True

 

def check_lost(positions):
    for pos in positions:
        x, y = pos 
        if y < 1:
            return True

    return False


def get_shape():
    global shapes, shape_colors
 
    return Piece(5, 0, random.choice(shapes))
 

 
def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
 
    surface.blit(label, (top_left_x + play_width/2 - (label.get_width() / 2), top_left_y + play_height/2 - label.get_height()/2))
   

def draw_grid(surface, row, col):
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pygame.draw.line(surface, (GRAY), (sx, sy+ i*30), (sx + play_width, sy + i * 30))  # horizontal lines
        for j in range(col):
            pygame.draw.line(surface, (GRAY), (sx + j * 30, sy), (sx + j * 30, sy + play_height))  # vertical lines



def clear_rows(grid, locked):
    # need to see if row is clear the shift every other row above down one
 
    inc = 0
    for i in range(len(grid)-1,-1,-1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            # add positions to remove from locked
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)
 

 

def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255))
 
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)
 
    surface.blit(label, (sx + 10, sy- 30))

 
def update_score(nscore):
    score = max_score()

    with open('scores.txt', 'w') as f:
        if int(score) > nscore:
            f.write(str(score))
        else:
            f.write(str(score))   


def max_score():
    with open('scores.txt', 'r') as f:
        lines = f.readlines()
        score = lines[0].strip()
    
    return score



def draw_window(surface, grid, score=0, last_score = 0):
    surface.fill((BLACK))
    # Tetris Title
    font = pygame.font.SysFont('helvetica', 60)
    label = font.render('TETRIS', 1, (WHITE))
 
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    # Current Score
    font = pygame.font.SysFont('helvetica', 30)
    label = font.render('Score: ' + str(score), 1, WHITE)

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100

    surface.blit(label, (sx + 20, sy + 160))
 
    # Last Score
    label = font.render('High Score: ' + last_score, 1, WHITE)

    sx = top_left_x - 200
    sy = top_left_y + 200

    surface.blit(label, (sx + 20, sy + 160))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0)
 
    # draw grid and border
    draw_grid(surface, 20, 10)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)
    # pygame.display.update()
 
def main():
    last_score = max_score()
    global grid
 
    locked_positions = {}  # (x,y):(255,0,0)
    grid = create_grid(locked_positions)
 
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
 
    while run:
        fall_speed = 0.27
 
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()
 
        # PIECE FALLING CODE
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
 
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)
 
                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
 
                if event.key == pygame.K_SPACE:
                   while valid_space(current_piece, grid):
                       current_piece.y += 1
                   current_piece.y -= 1
                   print(convert_shape_format(current_piece)) # todo fix
 
        shape_pos = convert_shape_format(current_piece)
 
        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
 
        # IF PIECE HIT GROUND
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
 
            # call four times to check for multiple clear rows
            clear_rows(grid, locked_positions)
 
        draw_window(win, grid, score, last_score)
        draw_next_shape(next_piece, win)
        pygame.display.update()
 
        # Check if user lost
        if check_lost(locked_positions):
            run = False
 
    draw_text_middle("You Lost", 40, (WHITE), win)
    pygame.display.update()
    pygame.time.delay(2000)


def main_menu():
    run = True
    while run:
        win.fill((0,0,0))
        draw_text_middle('Press any key to begin.', 60, (255, 255, 255), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
 
            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()
 
 
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
 
main_menu()  # start game