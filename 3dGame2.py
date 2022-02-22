import game_basis as gb
from pygame.constants import K_RIGHT, K_LEFT, K_DOWN, K_UP, K_1
import pygame as pg


map_name = input("Map name:")
file = open("/home/markus/programeer/game_engine/{}.txt".format(map_name), "r")
coords = []
xcoord = []
ycoord = []
for x in file.readlines():
    coords.append(x.split())
spawn = coords[-1]
coords.remove(coords[-1])

lyn_lys = []
for lyn in coords:
    lyn_lys.append((lyn[0], lyn[1], (lyn[0] + lyn[2]), lyn[1]))
    lyn_lys.append((lyn[0], lyn[1], lyn[0], (lyn[3] + lyn[1])))
    lyn_lys.append(((lyn[0] + lyn[2]), (lyn[1] + lyn[3]), lyn[0], (lyn[1] + lyn[3])))
    lyn_lys.append(((lyn[0] + lyn[2]), (lyn[1] + lyn[3]), (lyn[0] + lyn[2]), lyn[1]))
#print(lyn_lys)

game = gb.Game(40, 500, 500)
speeler = gb.Player(10, "blue", int(spawn[0]), int(spawn[1]), 2, 5, 0.1)
blok = gb.Block(0, 0, 3, 3, "green", 1)
render = gb.Render(0, 0, 1, 30, 30, 300, 160, True, lyn_lys)

teller = 0
speeler_prepos = [0]
while game.running == True:
    for blk in coords:
        speeler_raak = gb.CollisionCords(speeler, int(blk[0]), int(blk[1]), int(blk[2]), int(blk[3]))
        pg.draw.rect(gb.skerm, (200, 200, 200), pg.Rect(int(blk[0]), int(blk[1]), int(blk[2]), int(blk[3])))#comment hierdie uit vir vinaale game
        if speeler_raak.check == True:
            speeler.xpos = speeler_prepos[0][0]
            speeler.ypos = speeler_prepos[0][1]

    game.run()
    game.showall()
    speeler.show()#comment hierdie uit in vinaale game

    speeler_prepos[0] = (int(speeler.xpos), int(speeler.ypos))
    if game.key(K_LEFT):
        speeler.rotate_left()
    if game.key(K_RIGHT):
        speeler.rotate_right()
    if game.key(K_UP):
        speeler.move_forward()
    if game.key(K_DOWN):
        speeler.move_backward()

    render.calculate(speeler.direction, speeler.xpos, speeler.ypos)


file.close()

