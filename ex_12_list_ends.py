# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
# the first and last elements of the given list. For practice, write this code inside a function.
from random import randint


def ends(numeri):
    result = []
    result.append(numeri[0])
    result.append(numeri[len(numeri)-1])
    return result


numbers = []
for i in range(1, randint(1, 31)):
    numbers.append(randint(1, 500))

first_last = ends(numbers)

print("Lista originale\n", numbers)
print("Primo numero della lista:", first_last[0], "\nUltimo numero della lista:", first_last[1])
