import List as L

def main():
    mainList = L.LinkedList()
    mainList.insertAtTheStart(L.Element("1"))
    mainList.insertAtTheStart(L.Element("2"))
    mainList.insertAtTheStart(L.Element("3"))
    
    for node in mainList:
        print(f"{node}", end=" > ")
    print("None")

main()