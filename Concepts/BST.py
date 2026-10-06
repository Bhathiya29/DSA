# Binary Trees

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.value)
    

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

print(A)


# RECRUSIVE TRAVERSAL DFS (Pre-order))
def pre_order(node):
    if not node:
        return
    
    print(node.value)
    pre_order(node.left)
    pre_order(node.right)


pre_order(A)

def in_order(node):
    if not node:
        return
    
    in_order(node.left)
    print(node.value)
    in_order(node.right)

# Iterative Traversal DFS (Pre-order)
def pre_order_iterative(node):
    stack = []
    stack.append(node)

    while stack:
        curr = stack.pop()
        print(curr.value)

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

pre_order_iterative(A)

# BFS

from collections import deque

def bfs(node):
    q = deque()
    q.append(node)

    while q:
        curr = q.popleft()
        print(curr.value)

        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)


# check if Value exists in a binary tree (DFS)

def search(node, target):
    if not node:
        return False
    
    if node.value == target:
        return True
    
    return search(node.left, target) or search(node.right, target)


print(search(A, 10))  

def bst_search(node, target):
    if not node:
        return False
    
    if node.value == target:
        return True

    if target < node.value:
        return bst_search(node.left, target)
    else:
        return bst_search(node.right, target)
    
    
