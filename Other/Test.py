class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
    
    def __str__(self):
        return str(self.val)
    

# Recursive Pre-Order
def pre_order_dfs(node):
    if not node:
        return
    
    print(node)
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)
        

def pre_order_dfs_iterative(node):
    stack = [node]

    while stack:
        node = stack.pop()
        print(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# BFS
from collections import deque

def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    
def dfs_search(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True
    
    return dfs_search(node.right, target) or dfs_search(node.left, target)

# BST's
def search_bst(node,target):
    if not node:
        return False
    
    if node.val == target:
        return True
    
    if target<node.val: return search_bst(node.left, target)
    else: return search_bst(node.right,target)


# HEAPS

A = [-4,3,1,0,2,5,10,8,12,9]

import heapq
heapq.heapify(A)

heapq.heappush(A,4)

minn = heapq.heappop(A)

# Heap Sort
def heapsort(arr):
    heapq.heapify(arr)

    n = len(arr)

    new_list = [0]*n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    
    return new_list


# Max Heap
B = [-4,3,1,0,2,5,10,8,12,9]

n = len(B)

for i in range(n):
    B[i] = -B[i]


heapq.heapify(B)

largest = -heapq.heappop(B)


# Putting tuples of items on the heap

D = [5,4,3,5,4,3,5,5,4]

from collections import Counter

counter = Counter(D)

heapp = []

for k,v in counter.items():
    heapq.heappush(heapp,(v,k))