# coding : utf-8

from random import randint
from time import sleep
import os
import copy

change = True


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
    counters = []

    for i in range(0, 9):
        counters.append(copy.deepcopy(counter))

    # righe
    for i in range(0, 9):
        # numeri
        for x in m[i]:
            counters[i][str(x)] += 1

    # colonne
    for i in range(1, 10):
        for rows in m:
            counters[i-1][str(rows[i-1])] += 1

    # quadrati
    q1 = 0
    q2 = 3
    divider = 0
    list_q = []
    quad = []
    for j in range(0,7,3):
        for rows in m:
            for i in range(q1+j, q2+j):
                quad.append(rows[i])
            divider += 1
            if divider % 3 == 0:
                list_q.append(quad)
                quad = []

    # count q
    for i in range(0, 9):
        # numeri
        for x in list_q[i]:
            counters[i][str(x)] += 1

    change = False

    for i in range(0, 9):
        for x in range(0, 9):
            if m[i][x] != 0:
                if counters[i][str(m[i][x])] > 1:
                    m[i][x] = 0
                    change = True
    return m


def pop_matrix(m):
    for i in range(0, 9):
        for x in range(0, 9):
            if m[i][x] == 0:
                m[i][x] = randint(1, 9)
    return m

def print_mat(m):
    for i in m:
        print(i)


def init_matrix():
    matrix = []
    for i in range(0, 9):
        rows = []
        for x in range(0, 9):
            rows.append(0)
        matrix.append(rows)
    return matrix

matrix = init_matrix()
lav = 0
while change:
    matrix = pop_matrix(matrix)
    #print_mat(matrix)
    matrix = check_mat(matrix)
    lav += 1
    print("Lavoro...", lav)

print_mat(matrix)

