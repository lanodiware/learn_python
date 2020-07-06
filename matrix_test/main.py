# coding : utf-8

from random import randint
from time import sleep
import os
import copy

def check_mat(m):
    counter = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0
    }
    counters_r = []
    counters_c = []
    counters_q = []
    for i in range(0, 9):
        counters_r.append(copy.deepcopy(counter))
        counters_c.append(copy.deepcopy(counter))
        counters_q.append(copy.deepcopy(counter))

    # righe
    for i in range(0, 9):
        # numeri
        for x in m[i]:
            counters_r[i][str(x)] += 1

    numat = []
    # flip table
    for i in range(0, 9):
        nurow = []
        for x in range(0, 9):
            nurow.append(m[x][i])
        numat.append(nurow)

    # colonne
    for i in range(0, 9):
        # numeri
        for x in numat[i]:
            counters_c[i][str(x)] += 1

    # quadrati 

def pop_matrix():
    m = []
    for i in range(0, 9):
        rows = []
        for x in range(0, 9):
            rows.append(randint(1, 9))
        m.append(rows)
    return m

def print_mat(m):
    print("Matrice:")
    for i in m:
        print(i)

matrix = pop_matrix()
print_mat(matrix)
check_mat(matrix)
#print_mat(matrix)
