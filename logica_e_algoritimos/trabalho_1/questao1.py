ru = 4467027
print(f'Olá, Bem vindo(a) à calculadora de descontos do Elias Inácio Chavier Neto! ({ru})\n')

while True: # repete enquanto não receber um valor válido
    try:
        valor = float(input('Informe o valor do produto: '))  # valor do produto

    except:
        print('\nInválido. Digite novamente\n')
        continue # reinicia caso valor seja inválido

    break # finaliza o loop caso o valor seja válido

while True:
    try:
        quandade = int(input('Quantidade do produto: '))  # quantidade do produto

    except:
        print('\nInválido. Digite novamente.\n')
        continue

    break

totalSemDesconto = valor * quandade  # valor total sem desconto

if (quandade <= 9):   # validação do desconto baseando na quantidade
    desconto = 0
elif (quandade <= 99):
    desconto = 5
elif (quandade <= 999):
    desconto = 10
else:
    desconto = 15

valorDoDesconto = totalSemDesconto * desconto/100   # valor do desconto 
total = totalSemDesconto - valorDoDesconto    # valor final com desconto

print(f'\nSem desconto o valor a pagar seria R$ {totalSemDesconto:.2f} reais.')
print(f'Com o desconto de {desconto}%, o valor a pagar será de R$ {total:.2f} reais.')