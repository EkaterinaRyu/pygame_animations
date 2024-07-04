import pygame as pg
import math
pg.init()
clock = pg.time.Clock()
fps_limit = 60

scale = 600
game_sc = pg.display.set_mode((scale, scale))
pg.display.set_caption("circle")

angle = 0
rad_b = scale/3
rad_m = 10
orb_r = rad_b + rad_m
center = (scale/2, scale/2)


def generate_coords(angle):
    #angle += 0.1
    x = scale / 2 + math.cos(angle) * orb_r
    y = scale / 2 + math.sin(angle) * orb_r
    print(x, y, angle)
    return x, y  # возвращаем координаты центра спутника


# x, y = generate_coords(angle)


run = True


while run:
    clock.tick(fps_limit)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        else:

            #game_sc.fill((0, 0, 0))
            pg.draw.aaline(game_sc, (255, 255, 0),[scale/2, scale/2], generate_coords(angle), rad_m)
            angle += 0.1
            pg.display.flip()


pg.quit()
