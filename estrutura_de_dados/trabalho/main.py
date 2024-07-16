# Trabalho Estrutura de dados Questão 1
# Elias Inácio Chavier Neto - 4467027

def getPatientColor():
    while True:
        color = input('Informe a cor da prioridade do paciente. Use [V] para Verde e [A] para Amarelo. \n >> ')

        if (not color or (color != 'A' and color != 'V')):
            print('\nErro. Tente novamente. \n')
            continue

        else:
            break
    return color

def getPatientNumber():
    while True:
        try:
            print('')
            number = int(input('Informe o número do paciente. \n >> '))

        except:
            print('\nInválido. Digite novamente.\n')
            continue

        break
    return number
    
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

        if (current.color == 'V'):
            node.next = current
            self.head = node
            return

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
        color = getPatientColor()
        number = getPatientNumber()

        if (color == 'V'):
            node = Node(number, color)
            self.insertWithoutPriority(node)
        else:
            node = Node(number, color)
            self.insertWithPriority(node)

        print('\nInserido com sucesso!\n')
        
    def receivePatient(self):
        if self.head is not None:
            self.head = self.head.next

        print(' Paciente atendido! \n')

            
    def printMenu(self):
        print(' ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐ ')
        print(' │                   MENU                  │ ')
        print(' └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘ ')
        print(' ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐ ')
        print(' │ [1] Inserir novo paciente               │ ')
        print(' │ [2] Exibir lista de pacientes           │ ')
        print(' │ [3] Atender próximo paciente            │ ')
        print(' │ [4] Encerrar                            │ ')
        print(' └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘ ')


    def printList(self):
        current = self.head

        while current:
            print(f'{current.number} {current.color}', end=' > ')
            current = current.next
        print('None')
        print('')


def main():
    mainList = LinkedList()
    
    while True:
        mainList.printMenu()

        try:
            opt = int(input(' >> '))
            print('')

            if (not opt or opt < 1 or opt > 4): raise Exception()

            if (opt == 1):
                mainList.insert()
                continue
            if (opt == 2):
                mainList.printList()
                continue
            if (opt == 3):
                mainList.receivePatient()
                continue
            if (opt == 4):
                print('\nPrograma encerrado.')
                break
            
        except: 
            print('\nInválido. Digite novamente.\n')
            continue    

main()