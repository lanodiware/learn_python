from random import randint

def chooseword():
    with open("660000_parole_italiane.txt", "r") as f:
        words = f.read().split('\n')
        word = words[randint(0, len(words))].upper()
        words = None
        f.close()
    return word


def alterguessline(word, guessedletter, hidl):
    indexes = [ i for i in range(0, len(word)) if word[i] == guessedletter.upper()]
    #print(word)
    return "".join([ word[i].upper() if i in indexes or hidl[i] != '_' else '_' for i in range(0, len(word)) ])

w = chooseword()
hiddenword = w[0] + '_'*(len(w)-2) + w[-1]
print("\t", hiddenword)
playing = True
win = False
letter = ''
tent = 5
i = 0
while i < tent:
    scelta = True
    while scelta:
        letter = input("Inserisci una lettera! -> ").upper()
        if letter.isnumeric():
            print("Devi inserire una lettera!")
        else:
            scelta = False

    if letter in w:
        hiddenword = alterguessline(w, letter, hiddenword)
        print("La lettera {} è presente nella parola!\n\t{}".format(letter, hiddenword))
    else:
        print("La lettera {} non è presente nella parola!\n\t{}".format(letter, hiddenword))

    if hiddenword.count('_') < len(w):
        ch = True
        while ch :
            scelta = input("Vuoi provare ad indovinare la parola? (y/n) -> ")
            if scelta == 'y':
                gword = input("Inserisci la parola!\n-> ")
                if gword == w :
                    print("Hai indovinato!!")
                    win = True
                else:
                    print("Ritenta, sarai più fortunato.")
                ch = False
            elif scelta == 'n':
                print("Comprensibile.")
                ch = False
            else:
                print("Devi inserire y o n...")
    print("==========================================")
    if win:
        break
    i += 1
    if i >= tent:
        print("HAI PERSO HAHAHA!\nLa parola era:", w)
    else:
        print("Ti restano {} tentativi.".format(tent - i))
