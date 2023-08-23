# 4. Para a entrada em uma residência, foram criadas 5 senhas numéricas: 452012, 323233, 787910, 528917 e 683524.
#    Por meio do Python, crie um programa que armazena estas senhas em um conjunto e verifica se a senha 
#    digitada pelo usuário está ou não neste conjunto para permitir ou proibir a entrada na residência.


import numpy as np

passwords = [452012, 323233, 787910, 528917, 683524]

while True:
    tentative = input('Password: ')

    try:
        tentative = int(tentative)

        if (tentative in passwords):
            print('\nAccess granted!\n')
            break
        else:
            print('\nAccess denied\n')
    
    except:
        print('\nAccess denied\n')
