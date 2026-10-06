class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
    

head = Node(1)
A = Node(2)
B= Node(3)

head.next = A
A.next = B


# Traversing a linked list
def traverse(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(curr.data)
        curr = curr.next
    print("->".join(elements))

def search(head, target):
    curr = head
    while curr:
        if curr.data == target:
            return True
        curr = curr.next

    return False

# Doubly linked list
class DNode:
    def __init__(self,data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.data)
    
    def display(data):
        curr = data
        elements = []
        while curr:
            elements.append(curr.data)
            curr = curr.next
        print("<->".join(elements))
    
    def insert_at_beginning(head, tail, data):
        new_node = DNode(data, next = head)
        head.prev = new_node
        return new_node, tail
    
    def insert_at_end(head, tail, data):
        new_node = DNode(data, prev = tail)
        tail.next = new_node
        return head, new_node
    
    





        