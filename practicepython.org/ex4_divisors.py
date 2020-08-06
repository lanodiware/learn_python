# Create a program that asks the user for a number and then prints out a list of
# all the divisors of that number. (If you don’t know what a divisor is, it is a number
# that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

while True:
    try:
        number = int(input("Inserisci un numero -> "))
        if number <= 0:
            print("Devi inserire un numero maggiore di 0")
        break
    except(ValueError):
        print("Devi inserire un numero.")

divisors = []
for i in range(number, 0, -1):
    if number % i == 0:
        divisors.append(i)

print("I numeri per cui", number, "è divisibile sono:\n", divisors)