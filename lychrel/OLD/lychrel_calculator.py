
import time
import datetime

with open("track_lychrel.txt", "r") as f:
    THE_NUMBER = int(f.read())
with open("iter.txt", "r") as f:
    counter = int(f.read())

print("Numeri di partenza:\n", THE_NUMBER, "\n", counter)

a = THE_NUMBER

timer = time.time()

with open("results.txt", 'a+') as f:
    f.write("Lancio: " + str(datetime.datetime.today()) + "\n")
    f.close()


while True:
    a = str(a)
    b = a[len(a)::-1]
    s = int(a) + int(b)
    s = str(s)
    if s == s[len(s)::-1]:
        with open("palindrome.txt", "w") as f:
            f.write(s)
            f.close()
        break
    a = s
    #print("Iterazione:", counter, "digits:", len(a))
    counter += 1
    if float(time.time() - timer) > 10:
        print("Iterazione: " + str(counter) + " digits: " + str(len(a)) + "\n")
        with open("iter.txt", 'w') as f:
            f.write(str(counter))
            f.close()
        with open("results.txt", 'a+') as f:
            f.write("Iterazione: " + str(counter) + " digits: " + str(len(a)) + "\n")
            f.close()
        with open("track_lychrel.txt", 'w') as f:
            f.write(str(s))
            f.close()
        timer = time.time()


