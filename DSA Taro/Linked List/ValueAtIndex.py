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

def get_index_value(head,index):
    current = head

    index_count = 0

    while current is not None:
        if index_count == index:
            return current.val
        
        index_count += 1
        current = current.next

print(get_index_value(a,3))