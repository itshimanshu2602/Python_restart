class Node():
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
class LinkedList():
    def __init__(self):
        self.head = None
    
    def insertToEmpty(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            print("The list is empty")
    
    
    def insertToEnd(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
            return
        n = self.head
        while n.next is not None:
            n = n.next
            newNode = Node(data)
            n.next = newNode
            newNode.prev = n
            
    def deleteAtStart(self):
        if self.head == None:
            print("The linked is empty")
            return
        
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.start_prev = None
        
    def deleteAtEnd(self):
        if self.head is None:
            print("The list is empty")
            return
        