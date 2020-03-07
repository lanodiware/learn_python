# Ask the user for a number. Depending on whether the number is even or odd, print out
# an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and
# one number to divide by (check). If check divides evenly into num,
# tell that to the user. If not, print a different appropriate message.

from math import floor

while True:
    try:
        number = int(input("Inserisci un numero -> "))
        break
    except(ValueError):
        print("Devi inserire un numero")

if number % 2 == 0:
    print("Il nummero inserito è pari.")
    if number % 4 == 0:
        print("Il numero è un multiplo di 4")
else:
    print("Il numero è dispari.")

# 2

print("Wow. Prossimo esercizio:")

while True:
    try:
        number = int(input("Inserisci un numero -> "))
        break
    except(ValueError):
        print("Devi inserire un numero")

while True:
    try:
        number2 = int(input("Inserisci un altro numero -> "))
        break
    except(ValueError):
        print("Devi inserire un numero")

ris = floor(number/number2)

if ris % 2 == 2:
    print(number, "diviso", number2, "fa", ris, "ed è un numero pari")
else:
    print(number, "diviso", number2, "fa", ris, "ed è un numero dispari")
