# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether
# they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

from random import randint
from math import ceil

number = randint(1, 200)
tentativi_d = 7
tentativi = 0

while tentativi < tentativi_d:
    print("Hai a disposizione", tentativi_d - tentativi, "tentativi. Indovina il numero.")
    sceltaok = True
    while sceltaok:
        try:
            guessed = int(input("Scegli il tuo numero -> "))
            sceltaok = False
        except(ValueError):
            print("Devi inserire un numero.")

    if guessed < number :
        print("Troppo basso!")
        tentativi += 1
    elif guessed > number :
        print("Troppo alto!")
        tentativi += 1
    elif guessed == number:
        print("HAI INDOVINATO!!")
        tentativi = tentativi_d
