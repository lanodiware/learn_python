#Write a function that takes an ordered list of lychrel (a list where the elements are in order from smallest to
#largest) and another number. The function decides whether or not the given number is inside the list and returns
#(then prints) an appropriate boolean.

#Extras:

#Use binary search.

import time
from random import randint

def num_finder(new_list, value):
    while True:
        newlist_len = len(new_list)
        halflist = int(newlist_len / 2)
        if value < new_list[halflist]:
            print(value, "<", new_list[halflist], value < new_list[halflist])
            new_list = new_list[0:halflist]
        elif value > new_list[halflist]:
            print(value, ">", new_list[halflist], value > new_list[halflist])
            new_list = new_list[halflist:len(new_list)]
        elif value == new_list[halflist]:
            print("Ho trovato il numero", value, "nella lista num_list")
            break

num_list = []
for i in range(0, 5000000):
    num_list.append(i)

# test
do_this = 0
if do_this == 1:
    while True:
        num_finder(num_list, randint(0, len(num_list)))
else:
    while True:
        try:
            scelta = int(input("Inserisci un numero tra 0 e 50000-> "))
            if scelta < 1:
                print("Devi inserire un numero maggiore di 0")
            else:
                break
        except(ValueError):
            print("Devi inserire un numero")

    num_finder(num_list, scelta)


