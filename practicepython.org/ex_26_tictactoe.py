import random
from time import sleep

board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]


def checkwinner(game):
    countx = 0
    counto = 0
    # controllo vittore orizzontali
    for rows in game:
        for columns in rows :
            if columns == 'X':
                countx += 1
            elif columns == 'O':
                counto += 1
        if countx == 3:
            return 'X'
        elif counto == 3:
            return 'O'
        countx = 0
        counto = 0
    # controllo vittorie verticali
    countx = 0
    counto = 0
    for c in range(0, 3):
        for rows in game:
            if rows[c] == 'X':
                countx += 1
            elif rows[c] == 'O':
                counto += 1
        if countx == 3:
            return 'X'
        elif counto == 3:
            return 'O'
        countx = 0
        counto = 0
    # controllo vittorie diagonali
    if game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
        return 'X'
    elif game[2][0] == 'X' and game[1][1] == 'X' and game[0][2] == 'X':
        return 'X'
    elif game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
        return 'O'
    elif game[2][0] == 'O' and game[1][1] == 'O' and game[0][2] == 'O':
        return 'O'


def printboard():
    for row in board:
        print(row)


x = 0
y = 0
firstmove = random.randint(0,1)
ot = 1
gaming = True
while gaming:
    if firstmove == 0:
        if ot == 1:
            print("A me la prima mossa!")
            ot = 0
        else:
            print("Scelgo...")
            sleep(random.randint(1,3))

        tent = True
        while tent:
            y = random.randint(0, 2)
            x = random.randint(0, 2)
            #print("%sx%s" % (y+1, x+1))
            if board[x][y] == '':
                board[x][y] = 'X'
                tent = False

        printboard()
        firstmove = 1
    else:
        ot = 0
        tent = True
        while tent:

            print("Inserisci una coordinata 3x3")
            dothis = True
            while dothis:
                try:
                    scelta = int(input("scegli la riga -> "))
                    if scelta < 0 or scelta > 3:
                        print("Devi inserire un numero compreso tra 1 e 3")
                    else:
                        print("Hai scelto la riga %s" % scelta)
                        y = scelta - 1
                        dothis = False
                except ValueError:
                    print("Devi inserire un numero!")
            print("Inserisci una coordinata 3x3")
            dothis = True
            while dothis:
                try:
                    scelta = int(input("scegli la colonna -> "))
                    if scelta < 0 or scelta > 3:
                        print("Devi inserire un numero compreso tra 1 e 3")
                    else:
                        print("Hai scelto la colonna %s" % scelta)
                        x = scelta - 1
                        dothis = False
                except ValueError:
                    print("Devi inserire un numero!")

            if board[y][x] == '':
                board[y][x] = 'O'
                firstmove = 0
                printboard()
                tent = False
            else:
                print("La posizione inserita è già occupata!")
                printboard()
    if checkwinner(board) == 'X':
        print("VINCE IL COMPUTER!")
        break
    elif checkwinner(board) == 'O':
        print("VINCE L'UMANO!")
        break