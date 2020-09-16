from random import randint
import time
import os

def printmat(mat):
    print("Matrice: ")
    for i in mat:
        print(i)

def flipmat(mat):
    nm = []
    for i in range(0,9):
        nm.append([])
        for x in range(0,9):
          nm[i].append(mat[x][i])
    return nm


def matsquares(mat):
    quads = []
    nm = []
    for j in range(0,9,3):
        for i in range(0,9):
            for x in range(0+j,3+j):
                quads.append(mat[i][x])
            if len(quads) == 9:
                nm.append(quads)
                quads = []
    return nm


def isinsquare(rnd, mat, i, x):
    sqmat = matsquares(mat)
    if 0 <= i <= 2 and 0 <= x <= 2:
        return rnd in sqmat[0]
    if 3 <= i <= 5 and 0 <= x <= 2:
        return rnd in sqmat[1]
    if 6 <= i <= 9 and 0 <= x <= 2:
        return rnd in sqmat[2]
    if 0 <= i <= 2 and 3 <= x <= 5:
        return rnd in sqmat[3]
    if 3 <= i <= 5 and 3 <= x <= 5:
        return rnd in sqmat[4]
    if 6 <= i <= 9 and 3 <= x <= 5:
        return rnd in sqmat[5]
    if 0 <= i <= 2 and 6 <= x <= 9:
        return rnd in sqmat[6]
    if 3 <= i <= 5 and 6 <= x <= 9:
        return rnd in sqmat[7]
    if 6 <= i <= 9 and 6 <= x <= 9:
        return rnd in sqmat[8]

def checkzeropos(mat):
    pos = []
    for i in range(0, 9):
        for x in range(0, 9):
            if mat[i][x] == 0:
                pos.append('{}{}'.format(i,x))
    return pos

def blank(mat, row, col):
    for i in range(0, 9):
        mat[int(row)][i] = 0
    for i in range(0, 9):
        mat[i][int(col)] = 0
    return mat


def checksudoku(m):
    ok1 = [len(set(m[i])) == 9 for i in range(0, 9)]
    ok2 = [len(set(flipmat(m)[i])) == 9 for i in range(0, 9)]
    ok3 = [len(set(matsquares(m)[i])) == 9 for i in range(0, 9)]
    return all(ok1) and all(ok2) and all(ok3)


def initmat():
    mat = []
    for i in range(0, 9):
        mat.append([])
        for x in range(0, 9):
            mat[i].append(0)
    return mat


def populatesudoku():

    print("Genero Sudoku...")

    # Inizializzazione matrice
    mat = initmat()

    iter = 0
    timeout = time.time() + 60

    while True:
        i = randint(0, 8)
        x = randint(0, 8)
        rnd = randint(1, 9)

        # check numero random per inserimento
        if rnd not in mat[i] and rnd not in flipmat(mat)[x] and not isinsquare(rnd, mat, i, x):
            mat[i][x] = rnd

        # se dopo 5 minuti sto ancora dentro il while, resetto tutta la matrice
        if time.time() > timeout:
            mat = initmat()

        # se dopo 50.000 iterazioni ci sono ancora zeri 'ostinati' resetta riga e colonna corrispondente a 0
        ck = checkzeropos(mat)
        if iter == 50000 and len(ck) > 0:
            for j in ck:
                blank(mat, j[0], j[1])
            iter = 0

        # condizione di uscita

        # Se non ci sono più zeri
        if '0' not in str(mat):
            # se il sudoku è valido (no duplicati in riga, colonna o quadrato corrispondente)
            if checksudoku(mat):
                break
            else:
                # se non valido, ricomincia
                mat = initmat()

        iter += 1

    return mat


def requestsudoku(n):
    i = 0
    sudokus = []
    while i < n:
        sudokus.append(populatesudoku())
        i += 1
    return sudokus
