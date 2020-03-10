# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user
# guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the
# wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes
# throughout teh game and tell the user at the end.

# Say the number generated by the computer is 1038. An example interaction could look like this:

#  Welcome to the Cows and Bulls Game!
#  Enter a number:
#  >>> 1234
#  2 cows, 0 bulls
#  >>> 1286
#  1 cow, 1 bull
#  ...
#  Until the user guesses the number.

from random import randint
import time

begin = time.time()

guess = 0


def rng_number():
    numbers = []
    ok = True
    while ok:
        rnd_n = randint(0, 9)
        if rnd_n not in numbers :
            numbers.append(rnd_n)
        if len(numbers) == 1:
            if numbers[0] == 0:
                numbers.remove(0)
        if len(numbers) == 4:
            ok = False
    return numbers


def check_answer(digit, n):
    cows = 0
    bulls = 0
    got = [0,0,0,0]
    got_n = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
    for i in range(0, len(digit)):
        if str(digit[i]) == str(n[i]):
            cows += 1
            got[i] = 1
            got_n[n[i]] = 1
    for i in range(0, len(n)):
        if got[i] == 0 and got_n[n[i]] == 0:
            for x in range(0, len(n)):
                if str(n[i]) == str(digit[x]):
                    bulls += 1
                    got_n[n[i]] += 1
    #print(got, "\n", got_n)

    game = [cows, bulls]
    return game


nbr2guess = rng_number()

print("Ho generato un numero di 4 cifre da 0 a 9.\nLa prima cifra non può essere 0.")

MainLoop = True
while MainLoop:
    print(nbr2guess)
    check = True
    while check:
        try:
            guess = int(input("Indovina il numero -> "))
            if guess > 9999 or guess < 1000:
                print("Devi inserire un numero inferiore a 9999 e maggiore di 999")
            else:
                check = False
        except(ValueError):
            print("Devi inserire un numero.")

    answ = check_answer(nbr2guess, str(guess))

    if answ[0] != 4:
        print("Hai", answ[0], "mucche e", answ[1], "buoi.")
    else:
        print("Hai", answ[0], "mucche e", answ[1], "buoi!!")
        print("HAI VINTO!\nIl numero corretto era", nbr2guess)
        MainLoop = False

print("Hai sprecato", str((time.time() - begin) / 60)[:5], "minuti della tua vita. Complimenti.")



