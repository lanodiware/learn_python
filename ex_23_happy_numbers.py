
from time import sleep
import os


def is_this_number_happy(number):
    sequence = []
    seq_counters = {}
    execute = True
    while execute:
        txtnumber = str(number)
        somma = 0
        for i in range(0, len(txtnumber)):
            somma += int(txtnumber[i])**2
        number = somma

        if number == 1:
            return True

        # pattern detection

        if number not in sequence:
            sequence.append(number)
            seq_counters[number] = 0
        else:
            seq_counters[number] += 1
        #print(seq_counters)
        if list(seq_counters.values())[len(seq_counters)-1] == 2:
            return False


def i_esimo_felice(limite):
    happy = []
    i = 0
    while len(happy) < limite:
        print("Iterazione ", i, "...", sep='')
        if is_this_number_happy(i):
            happy.append(i)
        i += 1
    return happy[len(happy)-1]


main_loop = True 
while main_loop:

    do_this = ''
    scelta_numero = ''
    
    input_1 = True
    while input_1:
        try:
            do_this = int(input("Puoi decidere se:\n\t1-\tInserire un numero per sapere se è felice.\n\t2-\t"
                                "Inserire l'i-esima posizione di cui si vuole sapere il numero felice.\nScegli -> "))
            if do_this not in [1, 2]:
                print("Devi inserire uno dei numeri del menu.")
            else:
                input_1 = False
        except(ValueError):
            print("Devi inserire un numero!")
    
    if do_this == 1:
        sceltaok = True
        while sceltaok:
            try:
                scelta_numero = int(input("Inserisci un numero per sapere se sia felice o no. -> "))
                if scelta_numero < 1:
                    print("Devi inserire un numero maggiore o uguale a 1! ")
                else:
                    sceltaok = False
            except(ValueError):
                print("Devi inserire un numero.")
    
        print("Hai scelto: ", scelta_numero, ". Calcolo...", sep='')
    
        if is_this_number_happy(scelta_numero):
            print("Questo numero è felice!")
        else:
            print("Questo numero è infelice.")
    else:
        sceltaok = True
        while sceltaok:
            try:
                scelta_numero = int(input("Inserisci l'i-esimo numero che si desidera conoscere -> "))
                if scelta_numero < 1:
                    print("Devi inserire un numero maggiore o uguale a 1! ")
                else:
                    sceltaok = False
            except(ValueError):
                print("Devi inserire un numero.")
    
        print("Hai scelto: ", scelta_numero, ". Calcolo...", sep='')
        print("Il numero", scelta_numero, "della lista di numeri felici è:", i_esimo_felice(scelta_numero))
    sleep(2)
    scelta_exit = True 
    while scelta_exit:
        ch = input("Vuoi ripetere? [y/n] -> ")
        if ch == 'y':
            print("\n\nRicomincio.\n\n")
            scelta_exit = False
        elif ch == 'n':
            print("\n\nConcludo il programma!")
            main_loop = False
            scelta_exit = False
        else:
            print("Scelta errata.")
