# variáveis globais

ru = 4467027
total = 0
pedidoAberto = True

print(f'Olá, Bem vindo(a) à lanchonete do Elias Inácio Chavier Neto! ({ru})')
print('Insira o código do produto para adicioná-lo ao pedido.')


print("""
 _________________________________________
|_________>>_TABELA_DE_PREÇOS_<<__________|
|__Cod._|______Descrição_________|__Valor_|
|__100__|_Cachorro-Quente________|___9,00_|
|__101__|_Cachorro-Quente_Duplo__|__11,00_|
|__102__|_X-Egg__________________|__12,00_|
|__103__|_X-Salada_______________|__12,00_|
|__104__|_X-Bacon________________|__14,00_|
|__105__|_X-Tudo_________________|__17,00_|
|__200__|_Refrigerante_Lata______|___5,00_|
|__201__|_Chá_Gelado_____________|___4,00_|
""")

while pedidoAberto: # enquanto o pedido estiver em aberto, recebe os itens e adiciona ao pedido
    opt = input('Digite o código do lanche: ') # código do lanche
    print('')

    # valida a opção recebida e soma o valor do lanche ao total
    if (opt == '100'):
        print('1 Cachorro-Quente adicionado ao seu pedido (+ R$ 9,00)')
        total += 9
    elif (opt == '101'): 
        print('1 Cachorro-Quente Duplo adicionado ao seu pedido (+ R$ 11,00)')
        total += 11
    elif (opt == '102'): 
        print('1 X-Egg adicionado ao seu pedido (+ R$ 12,00)')
        total += 12
    elif (opt == '103'): 
        print('1 X-Salada adicionado ao seu pedido (+ R$ 13,00)')
        total += 13
    elif (opt == '104'): 
        print('1 X-Bacon adicionado ao seu pedido (+ R$ 14,00)')
        total += 14
    elif (opt == '105'): 
        print('1 X-Tudo adicionado ao seu pedido (+ R$ 17,00)')
        total += 17
    elif (opt == '200'): 
        print('1 Refrigerante Lata adicionado ao seu pedido (+ R$ 5,00)')
        total += 5
    elif (opt == '201'): 
        print('1 Chá Gelado adicionado ao seu pedido (+ R$ 4,00)')
        total += 4
    else:
        # caso a opção não exista, volta para o inícioe questiona nova,eente o código
        print('Código inválido. Por favor, digite novamente. \n')
        continue

    print('')

    # pergunta se vai encerrar, se a resposta for válida decide se encerra ou não
    # se a resposta não for correta repete a pergunta
    while True:
        opt2 = input('Deseja mais alguma coisa? [S] Sim / [N] Não ')

        if (opt2 == 'S' or opt2 == 's'):
            pedidoAberto = False
            break
        elif (opt2 == 'N' or opt2 == 'n'):
            pedidoAberto = True
            break
        else:
            print('\nErro. Tente novamente. \n')
            continue
    
    print('')
    if pedidoAberto:
        break

# retorna o valor total do pedido ao usuário
print(f'Total do seu pedido: R$ {total:.2f}'.replace('.', ','))