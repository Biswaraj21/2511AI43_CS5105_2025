class DSU:
    def __init__(self,V):
        self.parent=[i for i in range(V)]
        self.rank=[1]*V
    def find(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.find(self.parent[u])
        return self.parent[u]
    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)
        if pu==pv:
            return False
        if self.rank[pu]>self.rank[pv]:
            self.parent[pv]=pu
        elif self.rank[pv]>self.rank[pu]:
            self.parent[pu]=pv
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1
        return True

def kruskal(V,edge):
    edge.sort(key=lambda x:x[2])
    edge_count=0
    mst=[]
    wt=0
    dsu=DSU(V)
    for u,v,w in edge:
        if dsu.union(u,v):
            mst.append((u,v))
            wt+=w
            edge_count+=1
        if edge_count==V-1:
            break
    print('MST weight: ',wt)
    print('MST: ',mst)

V = 5
edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

kruskal(V, edges)