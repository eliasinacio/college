# 2023.08.14

# 8. Por meio do Python, escreva o decimal 12332 na respectiva forma binária.

def getBinary (num):
    aux = num
    binary = ''

    while (aux > 0):
        rest = aux%2
        intDiv = aux//2

        binary += str(rest)
        aux = intDiv
    
    return binary[::-1];

print(getBinary(12332));