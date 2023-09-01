#singly linked list tut
class Node():
    #Creating data attribute in constructor
    def __init__(self, data):
        self.data = data
        self.next = None
class Linkedlist():
    #Empty linked list
    def __init__(self):
        self.head = None
        self.n = 0 # Gives count of nodes in the linked list
        
    # Length of Linked list
    def __len__(self):
        return self.n
    
    def print(self):
        temp = None
        
    def insert_head(self, value):
        new_node = Node(value)
        
        new_node.next = self.head
        self.head = new_node
        self.n = self.n + 1
    
    def traverse(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next
            
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n += 1
    
    def insert_after(self, item, value):
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == item:
                break
            curr = curr.next
            
        if curr != None:
            temp = curr.next
            curr.next = new_node
            new_node.next = temp
            self.n += 1
        else:
            return "Item not found"
        
    def clear(self):
        self.head = None
        self.n = 0
        
    def delete_head(self):
        if self.head == None:
            return "Empty List"
        self.head = self.head.next
        self.n -= 1 
        
    def pop(self):
        curr = self.head
        if curr.next == None:
            curr = None
            return
        elif self.head == None:
            return "Empty LinkedList"
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n -= 1
    
    def remove(self, value):
        
        if self.head == None:
            return "empty Linked List"
        if self.head.data == value:
            self.n -= 1
            return self.delete_head
        
        curr = self.head
        
        while curr.next.data != value:
            break
        curr = curr.next
        
        if curr.next == None:
            return "Item not found"
        else:
            curr.next = curr.next.next
            self.n -= 1
            
    def find(self, value):
        curr = self.head
        t = 0
        while curr != None:
            if curr.data == value:
                return t
            curr = curr.next
            t += 1
        return "Not found"

mylist = Linkedlist() #Here mylist is the linked list
# a = Node(1)    # Node 1
# b = Node(20)   # Node 2 
# c = Node(3)    # Node 3
# mylist.head = a
# a.next = b
# b.next = c

mylist.insert_head(1)
mylist.insert_head(2)
mylist.insert_head(3)
mylist.insert_head(4)
mylist.insert_head(5)
mylist.insert_head(6)
# mylist.traverse()
# mylist.insert_after(3, 9)
# mylist.traverse()
mylist.find(9)
