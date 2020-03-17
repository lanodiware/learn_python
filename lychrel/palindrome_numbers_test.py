# reverse and add !
# LYCHREL NUMBERS
# somma delle cifre inverse e rilevamento numero palindromo risultante
# al n 196 l'iterazione è infinita(forse?)

import time


def pal_num(n):
    print("calcolando per numero", n, "...")
    orig = n
    count = 0
    while True:
        # cast n to string
        n = str(n)
        # reverse n
        revn = n[len(n)::-1]
        # cast n back to int
        n = int(n)
        # cast reversed n to int
        revn = int(revn)
        # sum lychrel and cast to string
        ris = str(n + revn)
        # if the result is palindrome then return
        if ris == ris[len(ris)::-1]:
            time.sleep(0.5)
            print("Iterazioni:", count)
            return orig, int(ris)
        # if not palindrome set the result as new n and repeat the calc
        n = ris
        # if orig = 196 print count
        if orig == 196:
            print(count)
        count += 1

results = []
for i in range(10, 200):
    results.append(pal_num(i))

print(results)