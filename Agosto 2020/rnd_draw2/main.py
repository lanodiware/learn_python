import turtle
from random import randint
import time
import os
from PIL import Image


f = turtle.Turtle()
turtle.screensize(500, 500)
f.speed('fastest')
f.pensize(2)

def eps2png(file):
    print("Processo:\t", file)
    Image.open(file).save(('pngs/' + file).replace('.eps', '.png'), "PNG")
    os.remove(file)
    print("Ho creato il file {}".format(file.replace('.eps', '.png')))

def moveaway():
    f.penup()
    f.setposition(2000,2000)
    f.pendown()

def nowdraw(name, draw_seconds, linelength, angle):
    print("Disegno...")

    now = time.time() + draw_seconds
    while time.time() <= now :
        #f.forward(linelength*randint(1,4)*randint(1,4)*0.5)
        f.forward(linelength)
        if randint(0,1):
            f.right(randint(1, 180 // angle) * angle)
        else:
            f.right(-angle//randint(1,4))
        pos = f.position()
        if abs(pos[0]) >= 200 or abs(pos[1]) >= 200:
            f.penup()
            #f.setposition(-pos[0], -pos[1])
            f.setposition(0, 0)
            f.pendown()
    moveaway()
    name += '.eps'
    f.getscreen().getcanvas().postscript(file=name)
    eps2png(name)


for i in range(10,180,10):
    nowdraw('random_draw_{}'.format('d'), 10, 15, i)
    f.clear()

