

def is_harshad(num):
    if num != 0:
        sdigit = sum([int(i) for i in str(num) ])
        return num % sdigit == 0
    return False


for i in range(1, 1000):
    if is_harshad(i):
        print("{} è un numero di Harshad!".format(i))