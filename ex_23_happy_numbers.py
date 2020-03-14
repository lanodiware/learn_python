
from time import sleep


def happy_number_gen(maximum):
    happy_numbers = []
    sequence = []
    seq_counters = {}
    for number in range(0, 500000):
        #print(number)
        orig_numb = number
        execute = True
        while execute:
            txtnumber = str(number)
            somma = 0
            for i in range(0, len(txtnumber)):
                somma += int(txtnumber[i])**2
            number = somma

            if number == 1:
                sequence = []
                seq_counters = {}
                execute = False
                happy_numbers.append(orig_numb)

            # pattern detection

            if number not in sequence:
                sequence.append(number)
                seq_counters[number] = 0
            else:
                seq_counters[number] += 1
            #print(seq_counters)
            if list(seq_counters.values())[len(seq_counters)-1] == 3:
                sequence = []
                seq_counters = {}
                execute = False
        if len(happy_numbers) >= maximum:
            break

    return happy_numbers[maximum-1]

scelta = 6

print("Il numero felice numero", scelta, "è", happy_number_gen(scelta))
