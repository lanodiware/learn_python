# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
# a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.


def is_prime(n):
    prime = True
    for i in range(n-1, 1, -1):
        if n % i == 0:
            return False
    return prime

counter_p = 0
counter_np = 0
p = []
np = []
min = 2
max = 200
for i in range(min, max):
    number = i
    if is_prime(number):
        counter_p += 1
        p.append(number)
    else:
        counter_np += 1
        np.append(number)

print("Numeri primi:\n", p)
print("Numeri primi:\n", np)
print("Tra", min, "e", max, "Ci sono: ")
print("Numeri primi", counter_p, "Numeri non primi", counter_np)
