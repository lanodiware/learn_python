# Write a password generator in Python. Be creative with how you generate passwords - strong passwords
# have a mix of lowercase letters, uppercase letters, lychrel, and symbols. The passwords should be random,
# generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

from random import randint
from time import sleep

def password_gen(lenght):
    symbols = ['£', '$', '%', '&', '€', '!', '?', '@', '#', '-', '_']
    numbers = []
    password = ''
    for i in range(0, 9):
        numbers.append(i)
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    chosen = []
    for i in range(0, lenght):
        chosen = [symbols[randint(0, len(symbols)-1)],
                  numbers[randint(0, len(numbers)-1)],
                  letters[randint(0, len(letters)-1)]
                ]
        if i > 0:
            if chosen[0] == password[i-1] or chosen[1] == password[i-1]:
                chosen = [symbols[randint(0, len(symbols) - 1)],
                          numbers[randint(0, len(numbers) - 1)],
                          letters[randint(0, len(letters) - 1)]
                          ]

        elem_rand = randint(0, 2)
        if elem_rand == 2:
            if randint(0, 1) == 0:
                password += str(chosen[elem_rand].lower())
            else:
                password += str(chosen[elem_rand])
        else:
            password += str(chosen[elem_rand])

    return password


while True:
    try:
        scelta = int(input("Inserisci il numero di caratteri della tua password -> "))
        if scelta < 10:
            print("Devi inserire un numero maggiore di 10")
        else:
            break
    except(ValueError):
        print("Devi inserire un numero")


print("Scegli una password:")

for i in range(0, 5):
    print(password_gen(scelta))