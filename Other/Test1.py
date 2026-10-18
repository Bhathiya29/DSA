n = 8
A =[[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]

# Making the matrix
M =[]

for i in range(n):
    M.append([0]*n)

for u,v in A:
    M[u][v] = 1

    # if undirected
    # M[v][u] = 1

# Making the list

from collections import defaultdict

D = defaultdict(list)

for u,v in A:
    D[u].append(v)

    #if undirected
    D[v].append(u)


# DFS
def dfs_recursive(node):
    print(node)
    for nei_nodes in D[node]:
        if nei_nodes not in seen:
            seen.add(nei_nodes)
            dfs_recursive(nei_nodes)

source =0

seen = set()
seen.add(source)
dfs_recursive(source)


