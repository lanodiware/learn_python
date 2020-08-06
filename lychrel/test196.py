import time

inizio = time.time()
it = 0
n = 196
step = 1000
while True:
    num = str(n)[::-1]
    n += int(num)
    if str(n) == num :
        with open("result.txt", 'a') as f:
            f.write(n)
            f.close()
        break
    if it == step :
        print('Ho raggiunto {} iterazioni'.format(it))
        step += 1000
    if it == 50000:
        break
    it += 1

print("Esecuzione {}".format(time.time() - inizio ))