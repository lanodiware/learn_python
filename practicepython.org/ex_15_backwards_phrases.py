#Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:
#
#  My name is Michele
# Then I would see the string:
#
#  Michele is name My
#
# shown back to me.

def backwards_l(sentence):
    new_sentence = ''
    len_sent = len(sentence)
    for i in range(len_sent-1, 0, -1):
        new_sentence += str(sentence[i])

    return new_sentence

def backwards_w(sentence):
    words = sentence.split(' ')
    bwords = ''
    for i in reversed(words):
        bwords += i + ' '
    return bwords

phrase = input("Inserisci una frase costituita da più parole:\n-> ")

print("Frase originale:\n", phrase)
print("Frase lettere inverse:\n", backwards_l(phrase))
print("Frase parole inverse:\n", backwards_w(phrase))



