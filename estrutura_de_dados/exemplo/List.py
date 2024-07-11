class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


    def __repr__(self):
        return self.data
    
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Element(data=nodes.pop(0))
            self.head = node

            for elem in nodes:
                node.next = Element(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")

        return " > ".join(nodes)
    
    def __iter__ (self):
        node = self.head

        while node is not None:
            yield node
            node = node.next


    def insertAtTheStart (self, node):
        node.next = self.head
        self.head = node

    def insertAtTheEnd (self, node):
        if self.head is None:
            self.head = node
            return
        
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
        
        current_node.next = node
        return
    
    def delete (self, data):
        if self.head is None:
            raise Exception("Empty List")
        
        if self.head.data == data:
            self.head = self.head.next
            return
    
        last_node = self.head

        for node in self:
            if node.data == data:
                last_node.next = node.next
                return
            last_node = node

        raise Exception(f"Node {data} not found")