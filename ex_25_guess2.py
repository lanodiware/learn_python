
lown = 0
highn = 5000
print("Pensa un numero da %s a %s" % (lown, highn))

counter = 0
thinking = True
while thinking:
    counter += 1
    print(lown, highn)
    guess = int((highn+lown)/2)
    inp_ok = True

    while inp_ok:
        try:
            print("Il numero è %s?" % guess)
            print("\t1. più alto\n\t2. più basso\n\t3. Numero Corretto!")
            scelta = int(input("Scegli -> "))
            if scelta < 1 or scelta > 3:
                print("Devi inserire un numero della lista!")
            else:
                inp_ok = False
        except ValueError():
            print("Devi inserire un numero!!")

    if scelta == 1:
        lown = guess
    elif scelta == 2:
        highn = guess
    else:
        print("Ci ho messo %s tentativi a capire il numero! Stupido umano!" % counter)
        print("FUCK YEA.")
        thinking = False
