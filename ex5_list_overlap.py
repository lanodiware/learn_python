# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common
# between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

from random import randint

list_one = []
list_two = []
list_three = []

for i in range(0, randint(1, 200)):
    list_one.append(randint(0, 2000))

for x in range(0, randint(1, 200)):
    list_two.append(randint(0, 2000))

for i in list_one:
    for x in list_two:
        if i == x and i not in list_three:
            list_three.append(i)

list_three.sort()
print(list_three)
