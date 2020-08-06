
phrase = input("inserisci una frase palindroma -> ")

print("norm:", phrase)
print("reve:", phrase[::-1])

if phrase == phrase[::-1]:
    print("La frase inserita è palindroma!")
else:
    print("La frase inserita non è palindroma!")

