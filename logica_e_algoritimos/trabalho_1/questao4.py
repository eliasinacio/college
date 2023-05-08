ru = 4467027
print('Olá, Esse é o controle de estoque do Elias Inácio Chavier Neto!')

menu1 = '''
----------------------------------
Insira abaixo a opção desejada:
1 - Cadastrar Peça
2 - Consultar Peça
3 - Remover Peça
4 - Sair
----------------------------------'''

menu2 = '''
----------------------------------
Insira abaixo a opção desejada:
1 - Consultar todas as peças
2 - Consultar peças por código
3 - Consultar peças por Fabricante
4 - Retornar
----------------------------------'''

todasAsPecas = []
numeroDePecasCadastradas = 0    # usado na geração de código para sempre gerar um diferente

def cadastrarPeca ():   # cadastra a peça retornada pela função criarPeca
    print('\nCadastro de nova peça:')
    peca = criarPeca()
    todasAsPecas.append(peca)
    print(f"\n{peca['nome']} cadastrada com sucesso. (Código: {peca['codigo']})")

def criarPeca():    # cria um dicionário padrão para a peça, recebe as informações do usuário e retorna a peça
    global numeroDePecasCadastradas
    peca = {'nome': '', 'fabricante': '', 'valor': 0}

    for chave in peca: # para cada key da peca, é associado o valor que o usuário informar
        while True:
            try:
                res = input(chave.capitalize() + ': ')

                if (res == ''):     # trata também como erro uma resposta vazia do usuário
                    raise Exception("Campo não pode ficar vazio.")

                if (chave == 'valor'):     # passa para float especificamente no campo 'valor'
                    res = float(res)

                peca[chave] = res    # associa cada valor a sua chave no dicionário 
                break
            except:
                print('Valor inválido. Por favor digite novamente.')
    
    numeroDePecasCadastradas += 1     # geração do código da peça
    codigo = numeroDePecasCadastradas   
    peca['codigo'] = str(codigo).zfill(3)    # ajuste para todas as peças terem o mesmo padrão '001'
    
    return peca

def consultarPeca():    # consulta de peças. dispara o menu, recebe as opções, e dispara as funções correspondentes.
    while True:
        print(menu2)
        opt2 = input('> ')

        if (opt2 == '1'):
            mostrarTodasAsPecas()
        elif (opt2 == '2'):
            mostrarPecaPorCodigo()
        elif (opt2 == '3'):
            mostrarPecasPorFabricante()
        elif (opt2 == '4'):
            break
        else:
            print('Opção inválida.')
            continue

def mostrarTodasAsPecas ():
    print('\nTodas as peças cadastradas\n')
    mostrarPecas(todasAsPecas)

def mostrarPecaPorCodigo ():
    codigo = input('\nCódigo: ')
    codigo = codigo.zfill(3) # tratativa para códigos como 1, 01 e 001 serem aceitos
    
    pecas = []

    for peca in todasAsPecas:
        if (codigo == peca['codigo']): # tratativa para códigos como 1, 01 e 001 serem aceitos
            pecas.append(peca)

    print(f'\nPeças cadastradas com código {codigo}:\n')
    mostrarPecas(pecas)

def mostrarPecasPorFabricante ():
    fabricante = input('\nFabricante: ')
    fabricante = fabricante.lower()
    
    pecas = []

    for peca in todasAsPecas:
        if (fabricante == peca['fabricante'].lower()): # tratativa para códigos como 1, 01 e 001 serem aceitos
            pecas.append(peca)

    print(f'\nPeças cadastradas do fabricante {fabricante}:\n')
    mostrarPecas(pecas)

def mostrarPecas(pecas):    # função apenas para mostrar as peças passadas como parâmetro. formatando-as e mostrando.
    print('-' * 78)
    print(f" Código | {'Nome':30} | {'Fabricante':20} | {'Valor':5s}")
    print('-' * 78)
    
    for peca in pecas:
        print(f" {peca['codigo']:>6} | {peca['nome']:30} | {peca['fabricante']:20} | R$ {peca['valor']:5.2f}")
    
    if (len(pecas) == 0):
        print(' Nenhuma peça encontrada.')

    print('-' * 78)

def removerPeca():
    codigo = input('\nCódigo da peça: ')
    codigo = codigo.zfill(3)    # equaliza códigos como 1, 01 e 001

    for peca in todasAsPecas:    # procura a peça e remove-a
        if (peca['codigo'] == codigo):
            x = todasAsPecas.index(peca)
            todasAsPecas.pop(x)

            print('\nPeça removida.\n')


# programa principal com o menu principal
while True:
    print(menu1)
    opt = input('> ')

    if opt == '1':
        cadastrarPeca()
        continue

    elif opt == '2':
        consultarPeca()

    elif opt == '3':
        removerPeca()

    elif opt == '4':
        print('Encerrando...')
        break

    else:
        print('\nOpção inválida')