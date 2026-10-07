# Array of Edges
n = 8
A=[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7]]

# Array of edges to Adjacency matrix
M = []

for i in range(n):
    M.append([0]*n)

for u,v in A:
    M[u][v] = 1
    #  For directed
    #M[v][u] = 1

# Adjacency List
from collections import defaultdict
D = defaultdict(list)

for u,v in A:
    D[u].append(v)
    # if undirected
    D[v].append(u)

# DFS with recursion
def dfs_recursive(node):
    print(node)

    for neighbor in D[node]:
        if neighbor not in seen:
            seen.add(neighbor)
            dfs_recursive(neighbor)

source = 0
seen = set()
seen.add(source)

dfs_recursive(source)


# iterative DFS with stack
source = 0
seen = set()
seen.add(source)
stack = [source]

while stack:
   node = stack.pop()
   print(node)

   for neighbor in D[node]:
       if neighbor not in seen:
            seen.add(neighbor)
            stack.append(neighbor)  

# BFS with queue
source = 0

from collections import deque

seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
    node = stack.pop()
    print(node)

    for neighbor in D[node]:
        if neighbor not in seen:
            seen.add(neighbor)
            q.append(neighbor)

# Creating a graph
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def __str__(self):
        return f"Node({self.value})"

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.neighbors.append(B)
B.neighbors.append(A)

C.neighbors.append(D)
D.neighbors.append(C)

