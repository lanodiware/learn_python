# Write a program that asks the user how many Fibonnaci lychrel to generate and then generates them.
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number
# of lychrel in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of lychrel where the next number
# in the sequence is the sum of the previous two lychrel in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)



1
1
2
3
5
8
13


def fibonacci_n(c_number):
    fibo = []
    for i in range(0, c_number):
        if i == 0:
            fibo.append(1)
        elif i == 1:
            fibo.append(1)
        else:
            fibo.append(fibo[i-1]+fibo[i-2])
    print(fibo)
    return fibo[c_number-1]



while True:
    try:
        scelta = int(input("Inserisci il numero N di cui trovare la corrispondenza di fibonacci -> "))
        if scelta < 1:
            print("Devi inserire un numero maggiore di 0")
        else:
            break
    except(ValueError):
        print("Devi inserire un numero")


print("L'N esimo numero \"" + str(scelta) + "\" di fibonacci è " + str(fibonacci_n(scelta)))

