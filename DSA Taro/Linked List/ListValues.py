class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next =b
b.next =c
c.next =d

def convert_to_list(head):
    vals = []

    current = head
    while current is not None:
        vals.append(current.val)
        current = current.next
    
    return vals

print(convert_to_list(a))