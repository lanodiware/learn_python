
def draw_table(d):
    h = dim[0]
    w = dim[1]
    table = ''
    for i in range(0, h):
        for x in range(0, w):
            table += ' ---'
        table += '\n'
        for x in range(0, w+1):
            table += '|\t'
        table += '\n'

    for x in range(0, w):
        table += ' ---'

    return table



print("Questo programma disegna una tavola in base ai numeri dati in input.")

choices = 0
dim = []

while True:
    try:
        scelta = int(input("Inserisci l'altezza della tavola -> "))
        if scelta < 1 or scelta > 10 :
            print("Devi inserire un numero maggiore di 1 e minore di 10")
        else:
            dim.append(scelta)
            break
    except ValueError:
        print("Devi inserire un numero")

while True:
    try:
        scelta = int(input("Inserisci la larghezza della tavola -> "))
        if scelta < 1 or scelta > 10 :
            print("Devi inserire un numero maggiore di 1 e minore di 10")
        else:
            dim.append(scelta)
            break
    except ValueError:
        print("Devi inserire un numero")

table = draw_table(dim)

print(dim)
print("La tavola:\n" + table)
