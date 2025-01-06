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

def find_node(head,target):
    current = head

    while current is not None:
        if current.val == target:
            return True

        current = current.next

    return False


print(find_node(a,'D')) 