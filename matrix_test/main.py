# coding : utf-8

from random import randint
from time import sleep
import os

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
    for rows in m:
        for i in range(1, 10):
            if i in rows:
            	c = counter
                for x in rows:
                    if x == i:
                        c[str(i)] += 1

        print("Conteggio riga:", rows)
        print(c)
        sleep(1)


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
