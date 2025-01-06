class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


a = Node(5)
b = Node (12)
c = Node (6)
d = Node (4)

a.next = b
b.next = c
c.next = d

def list_sum(head):
    sum = 0
    
    current = head
    while current is not None:
        sum+=current.val
        current = current.next
    
    return sum

def sum_list(head):
    if head is None:
        return 0
    
    return head.val + sum_list(head.next)

print(list_sum(a))
print(sum_list(a))