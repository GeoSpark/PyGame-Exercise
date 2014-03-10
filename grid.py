import random, time, pygame, sys, copy
from pygame.locals import *
from time import sleep

FPS = 30 # frames per second to update the screen

BOARDWIDTH = 64 # how many columns in the board
BOARDHEIGHT = 64 # how many rows in the board
SQUARESIZE = 16 # width & height of each space in pixels

PURPLE    = (255,   0, 255)
LIGHTBLUE = (170, 190, 255)
BLUE      = (  0,   0, 255)
RED       = (255, 100, 100)
BLACK     = (  0,   0,   0)
BROWN     = ( 85,  65,   0)

GRIDCOLOR = BLUE # color of the game board


# constants for direction values
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# The amount of space to the sides of the board to the edge of the window
# is used several times, so calculate it once here and store in variables.
XMARGIN = 4
YMARGIN = 4

WINDOWWIDTH = BOARDWIDTH * SQUARESIZE + (XMARGIN * 2)
WINDOWHEIGHT = BOARDHEIGHT * SQUARESIZE + (YMARGIN * 2)

gameBoards = []
board = 0


def main():
    global FPSCLOCK, DISPLAYSURF, GEMIMAGES, GAMESOUNDS, BASICFONT, BOARDRECTS
    # Initial set up.

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Life')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 36)
    # Create pygame.Rect objects for each board space to
    # do board-coordinate-to-pixel-coordinate conversions.
    BOARDRECTS = []
    for x in range(BOARDWIDTH):
        BOARDRECTS.append([])
        for y in range(BOARDHEIGHT):
            r = pygame.Rect((XMARGIN + (x * SQUARESIZE),
                             YMARGIN + (y * SQUARESIZE),
                             SQUARESIZE,
                             SQUARESIZE))
            BOARDRECTS[x].append(r)

    global gameBoards
    global board
    gameBoards = [getBlankBoard(), getBlankBoard()]

    DISPLAYSURF.fill(BLACK)

    while True:
        drawBoard()

        bb = (board + 1) % len(gameBoards)

        for x in xrange(BOARDWIDTH):
            for y in xrange(BOARDHEIGHT):
                gameBoards[bb][x][y] = rules(x, y)

        # for x in xrange(BOARDWIDTH):
        #     for y in xrange(BOARDHEIGHT):
        #         gameBoards[board][x][y] = 0

        board = bb


def getBlankBoard():
    # Create and return a blank board data structure.
    board = []

    for x in range(BOARDWIDTH):
        board.append([0] * BOARDHEIGHT)

    board[10][10] = 1
    board[11][10] = 1
    board[12][10] = 1
    board[12][9] = 1
    board[11][8] = 1
    return board


def count_neighbours(x, y):
    count = 0

    count += gameBoards[board][(x - 1) % BOARDWIDTH][y]
    count += gameBoards[board][(x - 1) % BOARDWIDTH][(y - 1) % BOARDHEIGHT]
    count += gameBoards[board][x][(y - 1) % BOARDHEIGHT]
    count += gameBoards[board][(x + 1) % BOARDWIDTH][(y - 1) % BOARDHEIGHT]
    count += gameBoards[board][(x + 1) % BOARDWIDTH][y]
    count += gameBoards[board][(x + 1) % BOARDWIDTH][(y + 1) % BOARDHEIGHT]
    count += gameBoards[board][x][(y + 1) % BOARDHEIGHT]
    count += gameBoards[board][(x - 1) % BOARDWIDTH][(y + 1) % BOARDHEIGHT]

    return count


def rules(x, y):
    value = gameBoards[board][x][y]
    count = count_neighbours(x, y)

    if value == 1 and count == 2:
        if count == 2:
            return 1

    if count == 3:
        return 1

    return 0


def drawBoard():
    for x in xrange(BOARDWIDTH):
        for y in xrange(BOARDHEIGHT):
            gemToDraw = gameBoards[board][x][y]

            if gemToDraw == 1:
                DISPLAYSURF.fill(RED, BOARDRECTS[x][y])
            else:
                DISPLAYSURF.fill(BLACK, BOARDRECTS[x][y])
                #    DISPLAYSURF.blit(GEMIMAGES[gemToDraw], BOARDRECTS[x][y])

            pygame.draw.rect(DISPLAYSURF, (128, 128, 128), BOARDRECTS[x][y], 1)

    pygame.display.update()


if __name__ == '__main__':
    main()
