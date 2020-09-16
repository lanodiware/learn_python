from random import randint

with open('sowpods.txt', 'r') as f:
    words = f.read().split('\n')
    f.close()

dlen = len(words)
print(words[randint(1, dlen)])

