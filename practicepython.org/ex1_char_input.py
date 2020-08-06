
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another
# number and printing out that many copies of the previous message.
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)

import datetime

year_now = datetime.datetime.now().year
name = input("Ciao! Inserisci il tuo nome -> ")
print("Ciao", name, "!")
while True:
    try:
        age = int(input("Inserisci la tua età -> "))
        if age < 0:
            print("Inserisci un'età valida.")
        break
    except(ValueError):
        print("Devi inserire un numero, figaaaa!!")



year_fut = year_now + 100 - age

if age > 100:
    print("Hai già più di 100 anni da", age - 100, "anni, vecchio di merda!")
    msg = "Hai già più di 100 anni da " + str(age - 100) + " anni, vecchio di merda!"
else:
    print(name,", avrai 100 anni nel ", year_now + 100 - age, "! :O")
    msg = name + " avrai 100 anni nel " + str(year_now + 100 - age) + "! :O"

while True:
    try:
        times = int(input("Inserisci il numero di volte in cuui vuoi ripetere il precedente messaggio! -> "))
        if times <= 0:
            print("Devi inserire un numero positivo")
        break
    except(ValueError):
        print("Devi inserire un numeroooooo")

for i in range(1, times+1):
    print(i, ".", msg)
