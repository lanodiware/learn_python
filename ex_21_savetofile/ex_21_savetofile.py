# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some
# different code, use the code from the solution), and instead of printing the results to a screen, write the
# results to a txt file. In your code, just make up a name for the file you are saving to.

# Extras:

# Ask the user to specify the name of the output file that will be saved.
import os

phrase = input("Inserisci una frase a caso -> ")
filename = input("Inserisci il nome del file con cui vuoi salvare i tuoi dati -> ")
filename += '.txt'

with open(filename, 'w') as f:
    f.write(phrase)
    f.close()

print("Ho salvato il file", filename, "in", os.getcwd() + '\\')
