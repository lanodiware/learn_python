# Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# Instead of printing the elements one by one, make a new list that has all the
# elements less than 5 from this list in it and print out this new list.
# Ask the user for a number and return a list that contains only elements from
# the original list a that are smaller than that number given by the user.

from random import randint

while True:
    try:
        max = int(input("Inserisci un numero di controllo -> "))
        break
    except(ValueError):
        print("Devi inserire un numero.")

the_list = []
n_of_numbers = 50
for x in range(0, n_of_numbers):
    the_list.append(randint(-30, 30))
new_list = []
for i in the_list:
    if i < max:
        new_list.append(i)

the_list.sort()
new_list.sort()

print("La lista originale:\n", the_list)
print("I numeri minori di 5 sono:\n", new_list)
