def is_this_number_happy(number):
    sequence = []
    seq_counters = {}
    execute = True
    while execute:
        txtnumber = str(number)
        somma = 0
        for i in range(0, len(txtnumber)):
            somma += int(txtnumber[i])**2
        number = somma

        if number == 1:
            return True

        # pattern detection

        if number not in sequence:
            sequence.append(number)
            seq_counters[number] = 0
        else:
            seq_counters[number] += 1
        #print(seq_counters)
        if list(seq_counters.values())[len(seq_counters)-1] == 2:
            return False

def is_this_number_prime(n):
    l = []
    for i in range(1, n):
        if n % i == 0:
            l.append(i)
    if len(l) == 1:
        return True
    else:
        return False


with open('happy.txt', 'w') as f:
    f.close()
with open('primes.txt', 'w') as f:
    f.close()

counter = 10
h_found = 0
while h_found < 100:
    if is_this_number_happy(counter):
        with open('happy.txt', 'a+') as f:
            f.write(str(counter) + '\n')
            f.close()
        h_found += 1
    counter += 1

counter = 10
pfound = 0
while pfound < 100:
    if is_this_number_prime(counter):
        with open('primes.txt', 'a+') as f:
            f.write(str(counter) + '\n')
            f.close()
        pfound += 1
    counter += 1



with open('happy.txt', 'r') as f:
    happy = f.read().split('\n')
    f.close()
with open('primes.txt', 'r') as f:
    primes = f.read().split('\n')
    f.close()

print("Numeri felici:")
print(happy)
print("Numeri primi:")
print(primes)

common = []
for i in happy:
    if i in primes and i != '':
        common.append(i)

print("Numeri in comune:")
print(common)
