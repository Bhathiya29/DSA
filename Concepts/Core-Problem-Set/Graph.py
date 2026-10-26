class Graph:
    def __init__(self):
        self.adj = {}
    
    def add_vertex(self,v):
        self.adj.setdefault(v,[])
    
    def add_edge(self,u,v, weight = 1, directed = False):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append((v,weight))
        if not directed:
            self.adj[v].append((u,weight))
        
    def neighbors(self, v):
        return self.adj.get(v,[])
    
