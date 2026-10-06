# Fibonacci

def F(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return F(n-1) + F(n-2)

# Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __str__(self):
        return str(self.val)

def reverse(node):
    if not node:
        return None
    
    reverse(node.next)
    print(node)


