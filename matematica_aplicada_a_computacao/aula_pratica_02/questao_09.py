# 2023.08.14

def getHexadecimalDigit (decimal):
    if (decimal >= 0 and decimal <= 9):
        return str(decimal)

    elif (decimal == 10): return 'A'
    elif (decimal == 11): return 'B'
    elif (decimal == 12): return 'C'
    elif (decimal == 13): return 'D'
    elif (decimal == 14): return 'E'
    elif (decimal == 15): return 'F'

def getHexadecimal (num):
    aux = num
    hex = ''

    while (aux > 0):
        rest = aux%16
        intDiv = aux//16

        hex += getHexadecimalDigit(rest)
        aux = intDiv
    
    return hex[::-1];

# 9. Escreva, por meio do Python, a forma hexadecimal do número decimal 15487.

print(getHexadecimal(15487));