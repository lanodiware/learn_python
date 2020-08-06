from PIL import Image, ImageColor


def calc_lychrel(n):
    iter = 0
    while True:
        n += int(str(n)[::-1])
        if iter > 20000 or str(n) == str(n)[::-1]:
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
    sizeh = len(str(lych)) // 10 if len(str(lych)) >= 10000 else 20
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


while True:
    try:
        n = int(input("Inserisci un numero -> "))
        break
    except ValueError:
        print("Devi inserire un numero!")

drawmylychrel(n)
print("Finito")