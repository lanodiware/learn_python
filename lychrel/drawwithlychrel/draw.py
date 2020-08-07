from PIL import Image, ImageColor
import turtle
from time import sleep

def calc_lychrel(n, max=20000):
    iter = 0
    while True:
        n += int(str(n)[::-1])
        if iter > max or str(n) == str(n)[::-1]:
            return n
        iter += 1


def choosecolor(d):
    d = int(d)
    return ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'pink', 'red'][d-1]


def drawmylychrel(n):
    print("Calcolo numero di lychrel di {}... (max 20000 iterazioni)".format(n))
    lych = calc_lychrel(n)
    print("Disegno immagine...")
    # altezza immagine
    sizeh = len(str(lych)) // 10
    # larghezza immagine (lunghezza lych)
    sizel = len(str(lych))
    im = Image.new('RGB', (sizel, sizeh))
    i = 0
    # per ogni colore
    for col in str(lych):
        for h in range(0, sizeh):
            im.putpixel((i, h), ImageColor.getrgb(choosecolor(col)))
        i += 1
    im.save('lychrel_number_{}.png'.format(str(n)))


def drawlychrelcircle(n):
    lych = calc_lychrel(n, 5000)
    circ = turtle.Turtle()
    ll = len(str(lych)) * 3
    turtle.screensize(ll, ll)
    # posizionamento cursore
    circ.penup()
    circ.right(90)
    circ.forward(ll//3)
    circ.right(-90)
    circ.pendown()
    circ.speed("fastest")
    # # # #
    for r in range(len(str(lych)), 1, -1):
        print("Disegno cerchio ", r)
        col = choosecolor(str(lych)[r-1])
        #circ.fillcolor(col)
        circ.pencolor(col)
        #circ.begin_fill()
        circ.circle(r)
        #circ.end_fill()
        #sleep(1)
        circ.penup()
        circ.right(-90)
        circ.forward(1)
        circ.right(90)
        circ.pendown()

    circ.penup()
    circ.forward(10000)
    ts = circ.getscreen()

    filename = "circle_{}".format(n)
    ts.getcanvas().postscript(file=filename, colormode='color')


while True:
    try:
        n = int(input("Inserisci un numero -> "))
        break
    except ValueError:
        print("Devi inserire un numero!")

drawmylychrel(n)
drawlychrelcircle(n)
print("Finito")