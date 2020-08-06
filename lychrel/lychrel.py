
def calc_lychrel(n):
    norig = n
    iter = 0
    while True:
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return "{};{}".format(iter, n)
        if iter > 10000:
            return ">10000k\t?".format(norig)
        iter += 1

with open("results.csv", "w") as f :
    f.close()
for i in range(5000):
    with open("results.csv", "a") as f :
        print(i)
        f.write("{};{}".format(i, calc_lychrel(i)) + "\n")
        f.close()