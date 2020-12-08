"""
this class is for the View of the Game
"""

import pygame as p
import GameModel

p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = WIDTH // DIMENSION
MAX_FPS = 15
IMAGES = {}

"""
to load the Images Only one time
"""
def loadImages():
    image_name = ["BB", "BK", "BN", "BP", "BQ", "BR", "WB", "WK", "WN", "WP", "WQ", "WR"]
    for piece in image_name:
        IMAGES[piece] = p.transform.scale(p.image.load("image/" + str(piece) + ".png"), (SQ_SIZE, SQ_SIZE))


"""
the Main of the game
"""
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = GameModel.GameState()
    loadImages()
    running = True
    sqSelected = ()  # to save the last click of player ,this is tuple
    plClicks = []  # to save all the click

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                loc = p.mouse.get_pos()  # to get the location of the mouse
                col = loc[0]//SQ_SIZE
                row = loc[1]//SQ_SIZE
                if sqSelected == (row, col):  # to check if the player click twice on the same place
                    sqSelected = ()
                    plClicks = []
                else:
                    sqSelected = (row, col)
                    plClicks.append(sqSelected)
                if len(plClicks) == 2:  # this mean the two click are different
                    move = GameModel.Move(plClicks[0], plClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = ()
                    plClicks = []

        drawTheGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


"""
this function is for draw the Board
"""
def drawBoard(screen):
    colors = [p.Color("bisque4"), p.Color("bisque2")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(screen, color, p.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
this function is for draw the Pieces Icons
"""
def drawPieces(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
this function is for draw the game
"""
def drawTheGameState(screen, gs):
    drawBoard(screen)  # to draw the board
    drawPieces(screen, gs.board)  # to draw the current state in the game


if __name__ == '__main__':
    main()
