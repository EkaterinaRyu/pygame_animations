import pygame as pg
import sys
import time

pg.init()
clock = pg.time.Clock()
fps_limit = 60

scale = 600
pg.display.set_caption("tic_tak_toe")
game_sc = pg.display.set_mode((scale, scale + 100))

# declaring the global variables
x_o = 'bulbasaur'  # for storing the 'x' or 'o'
winner = None
draw = None

white = (255, 255, 255)
black = (0, 0, 0)
red = (250, 0, 0)
reddish = (250, 70, 70)

board = [[None] * 3, [None] * 3, [None] * 3]


# loading the images as python object
x_img = pg.transform.scale(pg.image.load("bulbasaur.png"), (150, 150))
o_img = pg.transform.scale(pg.image.load("slowpoke.png"), (150, 150))
logo = pg.transform.scale(pg.image.load("Pokemon_GO_logo.png"), (2560 / 5, 1536 / 5))


def button(screen, position, text, color):
    screen.fill(white)
    screen.blit(logo, (scale/2 - 2560 / 5 /2, scale/2 - 2560 / 5 /2))
    font = pg.font.Font("Montserrat-VariableFont_wght.ttf", 50)
    text_render = font.render(text, True, white)
    x, y, w, h = text_render.get_rect()
    x_center, y_center = position
    x, y = x_center - w/2, y_center - h/2
    pg.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pg.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pg.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pg.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pg.draw.rect(screen, color, (x, y, w, h))
    return screen.blit(text_render, (x, y))


def make_board():

    new_surf = pg.Surface((scale, scale))
    new_surf.fill(white)

    # drawing vertical lines
    pg.draw.line(new_surf, black, (scale / 3, 0), (scale / 3, scale), 7)
    pg.draw.line(new_surf, black, (scale / 3 * 2, 0), (scale / 3 * 2, scale), 7)

    # drawing horizontal lines
    pg.draw.line(new_surf, black, (0, scale / 3), (scale, scale / 3), 7)
    pg.draw.line(new_surf, black, (0, scale / 3 * 2), (scale, scale / 3 * 2), 7)

    game_sc.blit(new_surf, (0, 0))
    pg.display.flip()
    text_status()


def text_status():
    global draw

    if winner is None:
        message = x_o.capitalize() + "'s turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = "Draw!"

    font = pg.font.Font("Montserrat-VariableFont_wght.ttf", 50)
    text = font.render(message, True, (255, 255, 255))

    game_sc.fill(black, (0, scale, scale, 100))
    text_rect = text.get_rect(center=(scale / 2, scale + 50))
    game_sc.blit(text, text_rect)
    pg.display.update()


def check_win():
    global board, winner, draw

    # checking for winning rows
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None):
            winner = board[row][0]
            pg.draw.line(game_sc, red, (0, (row + 1) * scale / 3 - scale / 6),
                                       (scale, (row + 1) * scale / 3 - scale / 6), 4)
            break

    # checking for winning columns
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None):
            winner = board[0][col]
            pg.draw.line(game_sc, red, ((col + 1) * scale / 3 - scale / 6, 0),
                                       ((col + 1) * scale / 3 - scale / 6, scale), 4)
            break

    # game won diagonally left to right
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner = board[0][0]
        pg.draw.line(game_sc, reddish, (0, 0), (scale, scale), 4)

    # game won diagonally right to left
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner = board[0][2]
        pg.draw.line(game_sc, reddish, (scale, 0), (0, scale), 4)

    if all([all(row) for row in board]) and winner is None:
        draw = True
    text_status()


def draw_x_o(row, col):
    global board, x_o
    posx, posy = 0, 0

    if row == 1:
        posx = 30
    if row == 2:
        posx = scale / 3 + 30
    if row == 3:
        posx = scale / 3 * 2 + 30

    if col == 1:
        posy = 30
    if col == 2:
        posy = scale / 3 + 30
    if col == 3:
        posy = scale / 3 * 2 + 30

    board[row - 1][col - 1] = x_o  # marking the board

    if x_o == 'bulbasaur':
        game_sc.blit(x_img, (posy, posx))
        x_o = 'slowpoke'

    else:
        game_sc.blit(o_img, (posy, posx))
        x_o = 'bulbasaur'
    pg.display.update()


def user_click():

    x, y = pg.mouse.get_pos()  # get coordinates of mouse click

    if x < scale / 3:  # get column
        col = 1
    elif x < scale / 3 * 2:
        col = 2
    elif x < scale:
        col = 3
    else:
        col = None

    if y < scale / 3:  # get row
        row = 1
    elif y < scale / 3 * 2:
        row = 2
    elif y < scale:
        row = 3
    else:
        row = None

    if row and col and board[row - 1][col - 1] is None:
        global x_o
        draw_x_o(row, col)  # drawing
        check_win()


def reset_game():
    global board, winner, x_o, draw
    x_o = 'bulbasaur'
    draw = False
    make_board()
    winner = None
    board = [[None] * 3, [None] * 3, [None] * 3]


new_surf = pg.Surface((scale, scale+100))
butt_start = button(new_surf, (scale/2, scale - 50), 'Play!', reddish)
game_sc.blit(new_surf, (0, 0))

able = True

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if butt_start.collidepoint(pg.mouse.get_pos()) and able:
                able = False
                time.sleep(1)
                make_board()
            else:
                user_click()
            if winner or draw:
                time.sleep(3)
                reset_game()
    pg.display.update()
    clock.tick(fps_limit)
