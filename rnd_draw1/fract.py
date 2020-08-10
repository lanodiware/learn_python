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
        if f.pos()[0] >= limit:
            break
    return f.getscreen()


## Main

def maincycle():
    fromthis, tothis = 1, 376
    for angle in range(fromthis, tothis):
        f.clear()
        l, a, lim = (1, angle, 150)
        f.penup()
        f.setposition(1000, 1000)
        f.pendown()
        dname = "drawing_{}.eps".format(angle)
        drawthis(l, a, lim).getcanvas().postscript(file=dname)
        eps2png(dname)

maincycle()
