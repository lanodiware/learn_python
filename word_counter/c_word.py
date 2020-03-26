from time import sleep

def strip_symbol(parola):
    symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '_', '+', '=', '{', '}', ']', '[', '|',
               '\\', '`', ',', '.', '/', '?', ';', ':', '\'', '"', '<', '>']
    parola = parola.strip()
    for x in symbols:
        parola = parola.replace(x, '')
    return parola

def word_counter(bookpath):
    with open(bookpath, 'r') as f:
        book = f.read().split(' ')
        f.close()
    words = {}
    for i in book:
        i = strip_symbol(i)
        if i != '':
            if i not in words:
                words[i] = 1
            else:
                words[i] += 1

    sorted_words = {k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)}

    return sorted_words


with open('dizionario_italiano.txt', 'r') as f:
    dizionario = f.read().split('\n')
    f.close()

counted = word_counter('nuova_riveduta.txt')


count = 0
for i in counted:
    if i.lower() in dizionario :
        print(str(i) + "\t" + str(counted[i]))
        count += 1
        if count > 100:
            break