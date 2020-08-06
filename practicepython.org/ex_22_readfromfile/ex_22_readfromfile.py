
import os

names = []
with open('names.txt', 'r') as f:
    for lines in f:
        names.append(lines.replace('\n', ''))
    f.close()


distinct_names = []
for i in names:
    if i not in distinct_names :
        distinct_names.append(i)

j = 0
for i in distinct_names:
    for x in names:
        if i == x:
            j += 1
    print("Ho trovato il nome", i, "per", j, "volte")



