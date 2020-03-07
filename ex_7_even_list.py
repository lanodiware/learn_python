# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python
# that takes this list a and makes a new list that has only the even elements of this list in it.

from random import randint

list = []

for i in range(randint(1, 500)):
    list.append(randint(1, 100))

# Appende i alla nuova lista prendendola dalla lista vecchia, secondo il TRUE della condizione
# if i % 2 !=  -> append to new_list

new_list = [i for i in list if i % 2 != 0]

print(new_list)