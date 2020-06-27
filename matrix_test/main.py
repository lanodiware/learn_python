# coding : utf-8

from time import sleep 
from random import randint 

matrix = [[[],[],[]],[[],[],[]],[[],[],[]]]
numbers = [1,2,3,4,5,6,7,8,9]

def gen_sudoku(mat):
	# cicla quadrati della matrice 
	for squares in mat : 
		alrdch = []
		# cicla righe dei quadrati 
		for row in squares :
			# riempi le righe con 3 numeri random 
			i = 0
			while i < 3 :			
				rnd = randint(1,9)
				if rnd not in row and rnd not in alrdch : 
					row.append(rnd)
					alrdch.append(rnd)
					i += 1
				else:
					continue
	return(mat)

print(gen_sudoku(matrix))


