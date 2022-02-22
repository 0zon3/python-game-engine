import pygame as pg
import math

from sympy import Ray2D
#sit comments by
def screen(xres, yres):
    global skerm
    skerm = pg.display.set_mode([xres, yres])

class Game:
    def __init__(self, tickrate, xresolution, yresolution):
        global yres
        self.running = True
        self.tickrate = tickrate
        self.xres = xresolution
        self.yres = yresolution
        yres = self.yres
        screen(self.xres, self.yres)
        self.instances = instance_list

    def run(self):
        klok = pg.time.Clock()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
        klok.tick(self.tickrate)
        pg.display.flip()
        skerm.fill((10, 10, 10))
    def showall(self):
        for x in instance_list:
            x.show()

    def key(self, Key):
        self.g = Key
        sleutel = pg.key.get_pressed()[self.g]
        return sleutel

    def quit(self):
        self.running = False

class Player:
    def __init__(self, diameter, colour, xposition, yposition, thickness, speed, rotation_speed):
        self.size = diameter
        self.colour = colour
        self.xpos = xposition
        self.ypos = yposition
        self.thickness = thickness
        self.speed = speed
        self.pos = self.xpos, self.ypos
        self.direction = 0.5
        self.dir_speed = rotation_speed
        self.final_colour = (0, 0, 0)
        if self.colour == "red":
            self.final_colour = (255, 0, 0)
        elif self.colour == "green":
            self.final_colour = (0, 255, 0)
        elif self.colour == "blue":
            self.final_colour = (0, 0, 255)
        elif self.colour == "grey":
            self.final_colour = (100, 100, 100)
    
    def show(self):
        pg.draw.circle(skerm, self.final_colour, (self.xpos, self.ypos), (self.size / 2), self.thickness)
        pg.draw.aaline(skerm, self.colour, (self.xpos, self.ypos), (self.xpos + math.cos(self.direction) * self.size, self.ypos + math.sin(self.direction) * self.size))

    def rotate_left(self):
        if self.direction >= -6.27999:
            self.direction -= self.dir_speed
        else:
            self.direction = 0
        

    def rotate_right(self):
        if self.direction <= 6.27999:
            self.direction += self.dir_speed
        else:
            self.direction = 0

    def move_forward(self):
        self.xpos += math.cos(self.direction) * self.speed
        self.ypos += math.sin(self.direction) * self.speed

    def move_backward(self):
        self.xpos -= math.cos(self.direction) * self.speed
        self.ypos -= math.sin(self.direction) * self.speed

instance_list = []
class Block:
    def __init__(self, xposition, yposition, xwidth, ywidth, colour, line_thickness):
        instance_list.append(self)
        self.xpos = xposition
        self.ypos = yposition
        self.xwidth = xwidth
        self.ywidth = ywidth
        self.colour = colour
        self.thickness = line_thickness
        self.final_colour = (0, 0, 0)
        if self.colour == "red":
            self.final_colour = (255, 0, 0)
        elif self.colour == "green":
            self.final_colour = (0, 255, 0)
        elif self.colour == "blue":
            self.final_colour = (0, 0, 255)
        elif self.colour == "grey":
            self.final_colour = (100, 100, 100)

    def show(self):
        pg.draw.rect(skerm, self.final_colour, pg.Rect(self.xpos, self.ypos, self.xwidth, self.ywidth), self.thickness)

    def hide(self):
        self.xpos = -3
        self.ypos = -3
        self.xwidth = 0
        self.ywidth = 0

class Projectile:
    def __init__(self, size, speed, colour, width, xposition, yposition, direction):
        self.size = size
        self.speed = speed
        self.colour = colour
        self.xpos = xposition
        self.ypos = yposition
        self.width = width
        self.direction = direction
        self.final_colour = (0, 0, 0)
        if self.colour == "red":
            self.final_colour = (255, 0, 0)
        elif self.colour == "green":
            self.final_colour = (0, 255, 0)
        elif self.colour == "blue":
            self.final_colour = (0, 0, 255)
        elif self.colour == "grey":
            self.final_colour = (100, 100, 100)

    def show(self):
        pg.draw.circle(skerm, self.final_colour, (self.xpos, self.ypos), (self.size * 2), self.width)

    def shoot(self):
        self.xpos += math.cos(self.direction) * self.speed
        self.ypos += math.sin(self.direction) * self.speed

class Collision:
    def __init__(self, object, block):
        self.object = object
        self.block = block
        self.check = False
        if self.object.xpos <= self.block.xpos + self.block.xwidth:
            if self.object.ypos <= self.block.ypos + self.block.ywidth:
                if self.object.xpos >= self.block.xpos:
                    if self.object.ypos >= self.block.ypos:
                        self.check = True
class CollisionCords:
    def __init__(self, object, xposition, yposition, xwidth, ywidth):
        self.object = object
        self.xpos = xposition
        self.ypos = yposition
        self.xwidth = xwidth
        self.ywidth = ywidth
        self.xend = self.xpos + self.xwidth
        self.yend = self.ypos + self.ywidth
        self.check = False
        if self.object.xpos >= self.xpos:
            if self.object.ypos >= self.ypos:
                if self.object.xpos <= self.xend:
                    if self.object.ypos <= self.yend:
                        self.check = True
#ek het nog nooit so lank an n projek gewerk nie!
class Render:
    def __init__(self, object_xpos, object_ypos, direction, line_start_x, line_start_y, render_distance, y_resulution, bool_render, blok_lys):
        global render_yres
        #self.bloklys
        self.xpos = object_xpos
        self.ypos = object_ypos
        self.direction = direction
        self.sx = line_start_x
        self.sy = line_start_y
        self.render_distance = render_distance
        self.yres = y_resulution
        render_yres = self.yres
        self.show_render = bool_render
        self.lyn_lys = blok_lys
        if self.lyn_lys[0] == self.lyn_lys[2]:
            self.orientasie = 1
        else:
            self.orientasie = 0 

        self.ex = math.cos(self.direction) * self.render_distance
        self.ey = math.sin(self.direction) * self.render_distance
        
        self.point_start_x = 0
        self.point_start_y = 0
        self.point_end_x = 0
        self.point_end_y = 0
        self.distance_lys = []

        self.x = 0
        self.y = 0
    
    def calculate(self, direction, xpos, ypos):
    #self.orientasie
    #     pg.draw.aaline(skerm, (200, 200, 200), (xpos, ypos), (self.ex, self.ey))
    #lengte = (ypos - int(lyn[1])) / math.cos(math.atan((self.ex - xpos) / (self.ey - ypos)))
        teller = 0
        for lyn in self.lyn_lys:
            if (teller % 2) == self.orientasie:#gebruik dan die original virgelyking.
                lengte = (ypos - int(lyn[1])) / math.cos(math.atan((self.ex - xpos) / (self.ey - ypos)))
                print(lengte)
            teller += 1
            #doen wisk op papier, vind ook uit wat die koordinaate van die trefpunt is, dan kyk jy of dit in die lynstuk val.