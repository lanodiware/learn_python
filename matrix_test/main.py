
import gensud

try:
    qty = int(input("Quanti sudoku tu servono? -> "))
except ValueError:
    print("Devi inserire un numero!")

with open("sudokus.txt", "w") as f:
    f.close()

for i in gensud.requestsudoku(qty):
    with open("sudokus.txt", "a") as f:
        f.write("Sudoku:\n\n")
        for x in i:
            f.write(str(x) + "\n")
        f.write("\n=======================\n\n")
        f.close()

print("Fatto. Guarda il file: sudokus.txt")