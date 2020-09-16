from random import randint
# GLOBALS

x=''
matgame = [
    [x,x,x],
    [x,x,x],
    [x,x,x],
]

def printmat(m):
    for i in m:
        print("_________________________")
        for x in i:
            print('|\t' + x + '\t', end='')
        print('|')
    print("_________________________")


def sceltains():
    sceltax, sceltay = None, None
    ins = False
    while not ins:
        try:
            sceltay = int(input("Scegli una riga! -> "))
            if not 1 <= sceltay <= 3:
                print("Devi inserire un valore da 1 a 3!")
            else:
                ins = True
        except ValueError:
            print("Devi inserire un numero!!")

    ins = False
    while not ins:
        try:
            sceltax = int(input("Scegli una colonna! -> "))
            if not 1 <= sceltax <= 3:
                print("Devi inserire un valore da 1 a 3!")
            else:
                ins = True
        except ValueError:
            print("Devi inserire un numero!!")

    return [sceltay, sceltax]


def smarty(mat):
    flipmat = []
    for i in range(0,3):
        rows = []
        for x in range(0,3):
            rows.append(mat[x][i])
        flipmat.append(rows)

    for i in range(0,3):
        if mat[i].count('O') == 2 and '' in mat[i]:
            return [i, mat[i].index('')]

    for i in range(0, 3):
        if flipmat[i].count('O') == 2 and '' in flipmat[i]:
            return [flipmat[i].index(''), i]

    d1 = [mat[0][0], mat[1][1], mat[2][2]]
    d2 = [mat[2][0], mat[1][1], mat[0][2]]

    if d1[0] == 'O' and d1[1] == 'O' and d1[2] == '' :
        return [2, 2]
    if d1[0] == 'O' and d1[1] == '' and d1[2] == 'O' :
        return [1, 1]
    if d1[0] == '' and d1[1] == 'O' and d1[2] == 'O':
        return [0, 0]

    if d2[0] == 'O' and d2[1] == 'O' and d2[2] == '' :
        return [0, 2]
    if d2[0] == 'O' and d2[1] == '' and d2[2] == 'O' :
        return [1, 1]
    if d2[0] == '' and d2[1] == 'O' and d2[2] == 'O':
        return [2, 0]


def pcchoose(mat):
    while True:
        x, y = randint(0,2), randint(0,2)
        sm = smarty(mat)
        if sm is not None:
            x, y = sm[0], sm[1]
        if matgame[x][y] == '':
            matgame[x][y] = 'O'
            break
    return mat

def winner(mat):
    w = ''
    # diagonale 1
    if mat[0][0] == 'X' and mat[1][1] == 'X' and mat[2][2] == 'X':
        w = 'X'
    # diagonale 2
    elif mat[2][0] == 'X' and mat[1][1] == 'X' and mat[0][2] == 'X':
        w = 'X'
    # orizzontali
    elif mat[0][0] == 'X' and mat[0][1] == 'X' and mat[0][2] == 'X':
        w = 'X'
    elif mat[1][0] == 'X' and mat[1][1] == 'X' and mat[1][2] == 'X':
        w = 'X'
    elif mat[2][0] == 'X' and mat[2][1] == 'X' and mat[2][2] == 'X':
        w = 'X'
    # verticali
    elif mat[0][0] == 'X' and mat[1][0] == 'X' and mat[2][0] == 'X':
        w = 'X'
    elif mat[0][1] == 'X' and mat[1][1] == 'X' and mat[2][1] == 'X':
        w = 'X'
    elif mat[0][2] == 'X' and mat[1][2] == 'X' and mat[2][2] == 'X':
        w = 'X'

    if mat[0][0] == 'O' and mat[1][1] == 'O' and mat[2][2] == 'O':
        w = 'O'
    # diagonale 2
    elif mat[2][0] == 'O' and mat[1][1] == 'O' and mat[0][2] == 'O':
        w = 'O'
    # orizzontali
    elif mat[0][0] == 'O' and mat[0][1] == 'O' and mat[0][2] == 'O':
        w = 'O'
    elif mat[1][0] == 'O' and mat[1][1] == 'O' and mat[1][2] == 'O':
        w = 'O'
    elif mat[2][0] == 'O' and mat[2][1] == 'O' and mat[2][2] == 'O':
        w = 'O'
    # verticali
    elif mat[0][0] == 'O' and mat[1][0] == 'O' and mat[2][0] == 'O':
        w = 'O'
    elif mat[0][1] == 'O' and mat[1][1] == 'O' and mat[2][1] == 'O':
        w = 'O'
    elif mat[0][2] == 'O' and mat[1][2] == 'O' and mat[2][2] == 'O':
        w = 'O'
    return w


def aretherespaces(mat):
    space = False
    for row in mat:
        for el in row :
            if el == '':
                space = True
    return space

playing = True
firsttime = True
while playing:
    if firsttime and randint(0,1) :
        print("Comincia il pc...")
        matgame = pcchoose(matgame).copy()
        printmat(matgame)

    firsttime = False
    sceltaok = True
    while sceltaok:
        p = sceltains()
        if matgame[p[0]-1][p[1]-1] == '':
            # inserimento scelta umano
            matgame[p[0]-1][p[1]-1] = 'X'
            # inserimento scelta computer
            sceltaok = False
            matgame = pcchoose(matgame).copy()
        else:
            print("Posizione già occupata... Scegline un'altra!")


    printmat(matgame)

    if not aretherespaces(matgame):
        print("NON VINCE NESSUNO!")
        playing = False
    else:
        x = winner(matgame)
        if x != '':
            if x == 'X':
                print("Ha vinto il giocatore umano!")
                playing = False
            elif x == 'O':
                print("HO VINTO IO BRUTTO PORCO")
                playing = False

