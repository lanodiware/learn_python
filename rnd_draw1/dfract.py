import turtle
from PIL import Image
import os
from time import sleep

f = turtle.Turtle()

turtle.screensize(500, 500)
f.speed('fastest')


def eps2png(file):
    print("Processo:\t", file)
    Image.open(file).save(file.replace('.eps', '.png'), "PNG")
    os.remove(file)


def drawthis(lar, deg, limit):
    f.penup()
    f.setposition(0, 0)
    f.pendown()
    i = 0
    while True:
        i += lar
        f.forward(i)
        f.right(deg)
        f.forward(i)
        f.right(deg//3)
        print(f.pos())
        if abs(f.pos()[0]) >= limit or abs(f.pos()[1]) >= limit :
            break
    f.clear()
    f.penup()
    f.setposition(1000, 1000)
    f.pendown()
    return f.getscreen()


## Main

def maincycle(name, l, angle, lim):
    dname = "{}_{}.eps".format(name, angle)
    drawthis(l, angle, lim).getcanvas().postscript(file=dname)
    eps2png(dname)


maincycle("test", 2, 170, 25)