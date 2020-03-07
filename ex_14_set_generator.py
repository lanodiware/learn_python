# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
# list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

from random import randint


def set_from_list(thelist):
    new_list = set()
    for i in thelist:
        if i not in new_list:
            new_list.add(i)

    return new_list


min = 1
max = 100
len = 40
elements = []
for i in range(0, len):
    elements.append(randint(min, max))

print("List:\n", elements)
print("Set from list:\n", set_from_list(elements))