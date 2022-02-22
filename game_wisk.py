import game_basis as gb
import mouseinfo
from pygame.constants import K_1, K_2, K_3, K_0, K_9, K_p
import time
import pygame as pg

plek = input("Level name:")

file = open("/home/markus/Documents/code files/pygame_goed/{}.txt".format(plek), "w")

game = gb.Game(60, 500, 500)
blok = gb.Block(0, 0, 0, 0, "red", 1)
cursor = gb.Block(0, 0, 2, 2, "green", 2)
spawn = gb.Block(0, 0, 3, 3, "green", 2)

start = []
end = []
blok_hide = True
blokke_nommer = 0
output = ""
sx = 0
sy = 0
ex = 0
ey = 0
stoor = False
wys_spawn = False
muis_verskil_x = 0
muis_verskil_y = 0
sync = True
while True:
    if game.key(K_0) == True:
        break
    else:
        game.run()
        muis_verskil_x = mouseinfo._linuxPosition()[0]
        muis_verskil_y = mouseinfo._linuxPosition()[1]

game.running = True
while game.running == True:
    game.run()
    blok.show()
    cursor.show()

    mouse_pos = mouseinfo._linuxPosition()
    mouse_x = mouse_pos[0] - muis_verskil_x
    mouse_y = mouse_pos[1] - muis_verskil_y

    cursor.xpos = mouse_x
    cursor.ypos = mouse_y

    if game.key(K_1):
        start.append((mouse_x, mouse_y))
        blok.xpos = mouse_x
        blok.ypos = mouse_y
        blok_hide = False
        time.sleep(0.2)

    if game.key(K_2):
        blok.hide()
        blok_hide = True
        blokke_nommer += 1
        stoor = True
        end.append((-(blok.xpos - cursor.xpos), -(blok.ypos - cursor.ypos)))
        #end.append((blok.xpos - cursor.xpos))
        end[-1] = (cursor.xpos, cursor.ypos)
        time.sleep(0.2) 

    if game.key(K_3):
        spawn.xpos = cursor.xpos
        spawn.ypos = cursor.ypos
        wys_spawn = True
        time.sleep(0.2)

    if wys_spawn == True:
        spawn.show()

    if blok_hide == False:
        blok.xwidth = -(blok.xpos - cursor.xpos)
        blok.ywidth = -(blok.ypos - cursor.ypos)
    else:
        pass

    for x in range(blokke_nommer):
        sx = start[x][0]
        sy = start[x][1]
        ex = end[x][0] - sx
        ey = end[x][1] - sy
        if ex < 0:
            sx -= -ex
            ex = -ex
        if ey < 0:
            sy -= -ey
            ey = -ey
        pg.draw.rect(gb.skerm, (200, 200, 200), pg.Rect(sx, sy, ex, ey))
    if stoor == True:
        output += (str((sx, sy, ex, ey)) + "\n").replace("(", "").replace(")", "").replace(",", "")
        stoor = False

file.write(output)
file.write(str(spawn.xpos) + " " + str(spawn.ypos))
file.close()