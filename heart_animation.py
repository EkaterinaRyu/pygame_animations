import pygame as pg
import math
from time import sleep
from operator import itemgetter
pg.init()
clock = pg.time.Clock()
fps_limit = 60

scale = 600
game_sc = pg.display.set_mode((scale, scale))
pg.display.set_caption("my_heart")


center = (scale/2, scale/2)


def make_polar(x, y):
    # конвертация
    return { 'radius': math.sqrt(x ** 2 + y ** 2),
             'angle': math.atan2(y, x) }

rad_0 = 15

def make_deck(di):
    radius = di.get('radius')
    angle = di.get('angle')
    x = math.cos(angle) * radius
    y = math.sin(angle) * radius
    return x, y


heart_angles = []


def star(highs, lines, hard):
    #highs = 7
    #lines = 4
    #hard = 0.7
    star_angles = []
    for angle in range(0, 361):
        ra = (math.cos((2 * math.asin(hard) + (math.pi * lines)) / (2 * highs))) / (math.cos((2 * math.asin(hard * math.cos(highs * angle)) + (math.pi * lines)) / (2 * highs)))
        star_angles.append({ 'radius': ra*200, 'angle': angle })
    return sorted(star_angles, key=itemgetter('angle'))


def heart(param):
    x = 16 * (math.sin(param)) ** 3
    y = 13 * math.cos(param) - 5 * math.cos(2 * param) - 2 * math.cos(3 * param) - math.cos(4 * param)
    return -x * 10 + scale/2, -y * 10 + scale/2


def get_heart_angles():
    for angle in range(0, 361):
        x, y = heart(angle)
        heart_angles.append(make_polar(x, y))
    return sorted(heart_angles, key=itemgetter('angle'))


run = True

while run:
    clock.tick(fps_limit)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:

                sor = get_heart_angles()

                game_sc.fill((0, 0, 0))
                for i in sor:
                    x1, y1 = make_deck(i)
                    sleep(0.01)
                    pg.draw.circle(game_sc, (255, 105, 180), [x1, y1], 1)
                    pg.display.flip()

                game_sc.fill((0, 0, 0))
                for i in range(len(sor)):
                    x1, y1 = make_deck(sor[i])
                    sleep(0.01)
                    pg.draw.aaline(game_sc, (255, 255, 0), center, [x1, y1])
                    pg.display.flip()

                game_sc.fill((0, 0, 0))
                sor_1 = star(5, 3, 1)
                for i in sor_1:
                    x1, y1 = make_deck(i)
                    sleep(0.01)
                    pg.draw.aaline(game_sc, (255, 255, 0), center, [x1 + scale/2, y1 + scale/2])
                    #pg.draw.aaline(game_sc, (255, 255, 0), center, [x1, y1])
                    pg.display.flip()

                game_sc.fill((0, 0, 0))
                sor_1 = star(9, 4, 0.7)
                for i in sor_1:
                    x1, y1 = make_deck(i)
                    sleep(0.01)
                    pg.draw.aaline(game_sc, (255, 255, 0), center, [x1 + scale/2, y1 + scale/2])
                    # pg.draw.aaline(game_sc, (255, 255, 0), center, [x1, y1])
                    pg.display.flip()



pg.quit()