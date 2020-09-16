from random import randint


dmintwenty = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
}
overnineteen = {
    "2": "twenty",
    "3": "thirty",
    "4": "fourty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}

def hundredspeak(n):
    if int(n) == 0 :
        return ''
    if int(n) > 99 :
        lastn = ''
        hund = dmintwenty[str(n)[0]] + " hundred " if int(str(n)[-2:]) != 0 else dmintwenty[str(n)[0]] + " hundred"
        if int(str(n)[-2:]) > 19:
            overhund = overnineteen[str(n)[1]] if str(n)[1] != 0 else ''
            lastn = '-' + dmintwenty[str(n)[2]] if str(n)[2] != '0' else ''
        else:
            overhund = dmintwenty[str(int(str(n)[-2:]))] if int(str(n)[-2:]) != 0 else ''
        return hund + overhund + lastn
    else :
        n = str(int(n))
        if int(n) <= 19:
            return dmintwenty[n]
        else:
            return overnineteen[n[0]] + '-' + dmintwenty[n[1]] if n[1] != '0' else overnineteen[n[0]]

def thousandspeak(n):
    if int(n) == 0 :
        return ''
    if int(n) > 99 :
        lastn = ''
        hund = dmintwenty[str(n)[0]] + " thousand " if int(str(n)[-2:]) != 0 else dmintwenty[str(n)[0]] + " thousand"
        if int(str(n)[-2:]) > 19:
            overhund = overnineteen[str(n)[1]] if str(n)[1] != 0 else ''
            lastn = '-' + dmintwenty[str(n)[2]] if str(n)[2] != '0' else ''
        else:
            overhund = dmintwenty[str(int(str(n)[-2:]))] if int(str(n)[-2:]) != 0 else ''
        return hund + overhund + lastn
    else :
        n = str(int(n))
        if int(n) <= 19:
            return dmintwenty[n] + ' thousand'
        else:
            return overnineteen[n[0]] + '-' + dmintwenty[n[1]]  if n[1] != '0' else overnineteen[n[0]]

def number2words(numb):
    numb = str(numb)
    if int(numb) <= 19:
        return dmintwenty[numb]
    else :
        if int(numb) > 999:
            majtho = thousandspeak(numb[:len(numb)-3]) + ' ' + hundredspeak(numb[-3:])
            return majtho.rstrip(' ')
        else:
            return hundredspeak(numb).rstrip(' ')

nmbrs = []
for i in range(500):
    nmbrs.append(randint(1,999999))

print("\"", number2words(1003), "\"")