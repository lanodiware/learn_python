# somma delle cifre inverse e rilevamento numero palindromo risultante
# al n 196 l'iterazione è infinita(forse?)

import time


def pal_num(n):
    print("calcolando per numero", n, "...")
    orig = n
    count = 0
    while True:
        n = str(n)
        revn = n[len(n)::-1]
        n = int(n)
        revn = int(revn)
        ris = n + revn
        ris = str(ris)
        if ris == ris[len(ris)::-1]:
            time.sleep(0.5)
            print("Iterazioni:", count)
            return orig, int(ris)
        n = ris
        if orig == 196:
            print(count)
        count += 1


results = []
for i in range(10, 200):
    results.append(pal_num(i))

print(results)