def brute(n,m,mat):
    if m<n-1: return -1
    adj=[[] for _ in range(n)]
    for u,v in mat:
        adj[u].append(v)
        adj[v].append(u)
    visited=[False]*n
    C=[0]
    def dfs(node,visited):
        visited[node]=True
        for v in adj[node]:
            if not visited[v]:
                dfs(v,visited)
    for i in range(n):
        if not visited[i]:
            dfs(i,visited)
            C[0]+=1
    return C[0]-1

class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[1]*n
    def find(self,u):
        if self.parent[u]==u:
            return u    
        self.parent[u]=self.find(self.parent[u])
        return self.parent[u]
    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)
        if pu==pv:
            return
        if self.rank[pu]>self.rank[pv]:
            self.parent[pv]=pu
        elif self.rank[pv]>self.rank[pu]:
            self.parent[pu]=pv
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1

def optimal(n,m,mat):
    if m<n-1:
        return -1
    dsu=DSU(n)
    for u,v in mat:
        dsu.union(u,v)
    C=len(set(dsu.find(i) for i in range(n)))
    return C-1

if __name__ == "__main__":
    n=m= 6
    edges = [[0,1],[0,2],[0,3],[1,2],[1,3],[4,5]]

    print("Brute Force:", brute(n,m,edges))
    print("Optimal DSU:", optimal(n,m,edges))