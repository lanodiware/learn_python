# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:#
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

poss = {1: "rock", 2: "paper", 3: "scissors"}

def judge(dec):
    if dec[0] == 2 and dec[1] == 1:
        return 1
    elif dec[0] == 3 and dec[1] == 1:
        return 2
    elif dec[0] == 1 and dec[1] == 2:
        return 2
    elif dec[0] == 3 and dec[1] == 2:
        return 1
    elif dec[0] == 1 and dec[1] == 3:
        return 1
    elif dec[0] == 2 and dec[1] == 3:
        return 2
    elif dec[0] == dec[1]:
        return 0

repeat = 0
while True:
    dec = []
    for i in range(0, 2):
        chosen = True
        while chosen:
            try:
                print("Hello player %s." % str(i + 1))
                scelta = int(input("\nRock, Paper or Scissors?\n\t1. Rock\n\t2. Paper\n\t3. Scissors\n-> "))
                if scelta > 3 or scelta < 1:
                    print("Devi inserire un numero da 1 a 3 per la tua scelta.")
                else:
                    dec.append(scelta)
                    chosen = False

            except(ValueError):
                print("Devi inserire un numero!")

    # poss = {1: "rock", 2: "paper", 3: "scissors"}

    print(str("P1: " + poss[dec[0]]).upper(), str("P2: " + poss[dec[1]]).upper())

    if judge(dec) == 1:
        print("PLAYER 1 WINS")
    elif judge(dec) == 2:
        print("PLAYER 2 WINS")
    elif judge(dec) == 0:
        print("TIE")

    repeat += 1
    if repeat > 10:
        break


