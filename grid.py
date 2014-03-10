import pygame

BOARDWIDTH = 64  # how many columns in the board
BOARDHEIGHT = 64  # how many rows in the board
SQUARESIZE = 16  # width & height of each space in pixels

GRIDCOLOR = (0, 0, 255)


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
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BOARDRECTS
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
    gameBoards = [get_blank_board(), get_blank_board()]

    DISPLAYSURF.fill((0, 0, 0))

    while True:
        draw_board()

        bb = (board + 1) % len(gameBoards)

        for x in xrange(BOARDWIDTH):
            for y in xrange(BOARDHEIGHT):
                gameBoards[bb][x][y] = rules(x, y)

        board = bb

        FPSCLOCK.tick(30)


def get_blank_board():
    # Create and return a blank board data structure.
    the_board = []

    for x in range(BOARDWIDTH):
        the_board.append([0] * BOARDHEIGHT)

    the_board[10][10] = 1
    the_board[11][10] = 1
    the_board[12][10] = 1
    the_board[12][9] = 1
    the_board[11][8] = 1
    return the_board


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

    if (value == 1 and count == 2) or count == 3:
        return 1

    return 0


def draw_board():
    for x in xrange(BOARDWIDTH):
        for y in xrange(BOARDHEIGHT):

            if gameBoards[board][x][y] == 1:
                DISPLAYSURF.fill((255, 0, 0), BOARDRECTS[x][y])
            else:
                DISPLAYSURF.fill((0, 0, 0), BOARDRECTS[x][y])

            pygame.draw.rect(DISPLAYSURF, (128, 128, 128), BOARDRECTS[x][y], 1)

    pygame.display.update()


if __name__ == '__main__':
    main()
