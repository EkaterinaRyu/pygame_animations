import pygame as pg
from time import sleep
from colour import Color

pg.init()
clock = pg.time.Clock()
fps_limit = 60

scale = 600
game_sc = pg.display.set_mode((scale, scale))
pg.display.set_caption("hilbert")


center = (scale/2, scale/2)

counts = 1023
depth = 5  # = 5 for hilbert

start_x = 5
start_y = 5

start_len = 19
next_x = start_x
next_y = start_y

pink = Color('#FF88E7')
blue = Color('#0000C3')
light_blue = Color('#99FEFE')


# colors = list(pink.range_to(blue, round(counts/2)))
# colors = colors + (list(blue.range_to(light_blue, round(counts/2))))
colors = list(Color('red').range_to(Color('green'), counts))
count = 0


def drawing(dx, dy):
    global next_x, next_y, colors, count
    # pg.draw.line(game_sc, colors[count].hex_l, (next_x + dx, next_y + dy), (next_x, next_y), 11)
    pg.draw.aaline(game_sc, colors[count].hex_l, (next_x + dx, next_y + dy), (next_x, next_y))
    count += 1
    next_x += dx
    next_y += dy
    sleep(0.01)
    pg.display.flip()


def hilbert(depth, x, y):
    if depth > 1:
        hilbert(depth - 1, y, x)  # рекурсивно спускаемся до глубины 1, "поворачивая" плоскость
    drawing(x, y)  # направо
    if depth > 1:
        hilbert(depth - 1, x, y)
    drawing(y, x)  # вниз
    if depth > 1:
        hilbert(depth - 1, x, y)
    drawing(-x, -y)  # налево
    if depth > 1:
        hilbert(depth - 1, -y, -x)


run = True

while run:
    clock.tick(fps_limit)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                game_sc.fill((0, 0, 0))
                hilbert(depth, start_len, 0)
                start_x = 5
                start_y = 5
                next_x = start_x
                next_y = start_y
                count = 0

