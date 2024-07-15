# Exigência 1 [OK]
# Exigência 2 [OK]
# Exigência 3 [OK]

# Deve-se implementar a função inserir() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7]; 
#     Deve-se solicitar ao usuário a cor (“A” ou “V”) e o número (inteiro). 
#     Deve-se criar um nodo com a cor e o número fornecidos pelo usuário. 
#     Se a lista estiver vazia, a cabeça (head) da lista deve apontar para o nodo criado. 
#     Senão, se a cor do nodo for “V”, deve-se chamar a função inserirSemPrioridade(nodo). 
#     Senão, se a cor do nodo for “A”, deve-se chamar a função inserirComPriordade(nodo). 
# Deve-se implementar a função imprimirListaEspera() em que: [EXIGÊNCIA DE CÓDIGO 5 de 7]; 
#     Deve-se imprimir todos os cartões e seus respectivos números a partir do primeiro até o último da lista. 
# Deve-se implementar a função atenderPaciente() em que: [EXIGÊNCIA DE CÓDIGO 6 de 7]; 
#     Deve-se remover o primeiro paciente da fila e imprimir uma mensagem chamando o paciente para atendimento informando o número do seu cartão. 
# Deve-se implementar um menu para utilização do sistema em que: [EXIGÊNCIA DE CÓDIGO 7 de 7]; 
#     Deve-se apresentar as opções (1 – adicionar paciente a fila, 2 – mostrar pacientes na fila, 3 – chamar paciente, 4 – sair) 
#     Se escolhida a opção 1, chamar a função inserir(). 
#     Se escolhida a opção 2, chamar a função imprimirListaEspera(). 
#     Se escolhida a opção 3, chamar a função atenderPaciente(). 
#     Se escolhida a opção 4, encerrar o programa. 
#     Se escolhida uma opção diferente as opções disponíveis, voltar ao item G.a. 


# Para testar o software, execute os seguintes passos e apresente a saída do console conforme exemplo de saída de console (próxima página): 
# Deve-se testar o sistema inserindo três (3) pacientes com cartão de cor “V”, dois (2) pacientes com cartão de cor “A”, dois (2) pacientes com cartão “V” e três (3) pacientes com cartão de cor “A”, nessa respectiva ordem. [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 3]; 
# Deve-se apresentar na saída de console a impressão da lista de espera (opção 2 do menu principal). [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 3];   
# Deve-se apresentar na saída de console o atendimento de dois (2) pacientes (opção 3 do menu principal) e em seguida mostrar a lista de espera (opção 2 do menu principal). [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 3];   


class Node:
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertWithoutPriority(self, node):
        if self.head is None:
            self.head = node
            return
        
        current = self.head

        while current.next != None:
            current = current.next
        
        current.next = node
        return


    def insertWithPriority(self, node):        
        if not self.head:
            self.head = node
        else:
            current = self.head
            prev = None
        
        current = self.head

        nodeAdded = False

        while current and nodeAdded != True and (
            (current.color == 'A' and current.number < node.number) or 
            (current.color == 'V' and current.number < node.number and node.color == 'V')
        ):
            if (current.next.color == 'V' or current.next == None):
                node.next = current.next
                prev = current
                prev.next = node
                nodeAdded = True
                break

            current = current.next
    

    def insert(self):
        print(' ┌ ─ ─ ─ ─ ── ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐ ')
        print(' │                   MENU                 │ ')
        print(' └ ─ ─ ─ ─ ── ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘ ')
        print(' │ [1] Inserir                            │ ')
        print(' │ [2] Inserir                            │ ')
        print(' │ [3] Inserir                            │ ')
        print(' └ ─ ─ ─ ─ ── ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘ ')


    def print(self):
        current = self.head

        while current:
            print(f'{current.number} {current.color}', end=' -> ')
            current = current.next
        print('None')

mainList = LinkedList()

# mainList.insertWithPriority(Node(1, 'A'));
# mainList.print()
# mainList.insertWithoutPriority(Node(1, 'V'));
# mainList.print()
# mainList.insertWithoutPriority(Node(2, 'V'));
# mainList.print()
# mainList.insertWithPriority(Node(3, 'A'));
# mainList.print()
# mainList.insertWithPriority(Node(2, 'A'));
# mainList.print()
# mainList.insertWithoutPriority(Node(8, 'V'));
# mainList.print()
# mainList.insertWithPriority(Node(4, 'A'));
# mainList.print()

mainList.insert()