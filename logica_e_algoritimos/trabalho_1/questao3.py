ru = 4467027
print(f'Olá, Essa é a calculadora de valores do Elias Inácio Chavier Neto! {ru}\n')

rotas = """
Cód    Rota 
[RS] - De Rio de Janeiro até São Paulo
[SR] - De São Paulo até Rio de Janeiro
[BS] - De Brasília até São Paulo
[SB] - De São Paulo até Brasília
[BR] - De Brasília até Rio de Janeiro
[RB] - Rio de Janeiro até Brasília"""

def dimensoesObjeto():
    # Pergunta ao usuário as dimensões, calcula o volume e retorna a taxa

    while True: 
        dimensoes = {'altura': 0, 'comprimento': 0, 'largura': 0} # dimensões

        # para cada dimensão, mostra o id referente e recebe seu valor.
        # caso o usuário digite algo incorreto, repete.
        for d in dimensoes:
            while True:
                try:
                    dimensoes[d] = float(input(d + ' (cm): ')) 
                    break
                except:
                    print('\nValor inválido. Por favor digite novamente.\n')

        # calcula o volume
        volume = dimensoes['altura'] * dimensoes['comprimento'] * dimensoes['largura']

        print(f'\nVolume do seu objeto: {volume:.1f} cm³')

        # retorna a taxa, caso o volume seja válido
        # repete as questões caso o volume exceda
        if (volume < 1000):
            return 10
        elif (volume < 10000):
            return 20
        elif (volume < 30000):
            return 30
        elif (volume < 100000):
            return 50
        else:
            print('\nDimensões excedentes. O volume não pode ultrapassar 100000.\n')
            continue

def pesoObjeto():
    # Pergunta ao usuário o peso e retorna o multiplicador
    # caso esteja incorreto ou inválido, repete

    while True:
        try:
            peso = float(input('peso (kg): '))
        except:
            print('\nPeso inválido. Por favor digite novamente.\n')
            continue

        print(f'\nPeso do seu objeto: {peso:.1f} kg')

        if (peso < 0.1):
            return 1
        elif (peso < 1):
            return 1.5
        elif (peso < 10):
            return 2
        elif (peso < 30):
            return 3
        else:
            print('\nPeso inválido. Por favor digite novamente.\n')
            continue

def rotaObjeto():
    # Pergunta ao usuário a rota e retorna o multiplicador
    # caso a rota seja inválida, repete

    while True:
        print(rotas)
        rota = input('\nrota: ')

        # tratativa caso usuário digite correto mas em letra minúscula
        rota = rota.upper()
    
        if (rota == 'RS' or rota == 'SR'):
            return 1
        elif (rota == 'BS' or rota == 'SB'):
            return 1.25
        elif (rota == 'BR' or rota == 'RB'):
            return 1.5
        else:
            print('\nRota inválida. Por favor digite novamente. ')
            continue

print('Primeiro informe as dimensões do objeto. \n')
valor = dimensoesObjeto()
print('\nAgora informe o peso do objeto. \n')
multiplicador1 = pesoObjeto()
print('\nAgora informe a rota. Exemplo: SR')
multiplicador2 = rotaObjeto()

# calcula o valor total e mostra
total = valor * multiplicador1 * multiplicador2

print(f'\nTotal a pagar: R$ {total:.2f} (valor: {valor} * peso: {multiplicador1} * rota: {multiplicador2})')