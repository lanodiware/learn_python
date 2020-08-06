import sys
from time import sleep
import re
import math

def calc_lychrel(n, max=None):
    c = 0
    codd = 0
    ceven = 0
    while True:
        n += int(str(n)[::-1])
        if n % 2 == 0:
            ceven += 1
        else:
            codd += 1
        if str(n) == str(n)[::-1]:
            return [n, c]
        if c == max:
            return str(max) + "\t" + str(ceven) + "\t" + str(codd) + "\t" + str(ceven-codd)
        c += 1



with open("results.txt", 'w') as f:
    f.close()

print("Calcolo lychrel di 196...:")
for i in range(10000, 50500, 500):
    lychn = calc_lychrel(196, i)
    print(lychn)
    with open("results.txt", 'a') as f:
        f.write(lychn + '\n')
        f.close()
#print("L'iterazione 500 del numero di Lychrel è: {}\nLunghezza: {} caratteri".format(str(lychn), len(str(lychn))))

