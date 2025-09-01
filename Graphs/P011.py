def brute(stones):
    n=len(stones)
    adj=[[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                adj[i].append(j)
                adj[j].append(i)
    visited=[False]*n
    def dfs(node):
        visited[node]=True
        for nei in adj[node]:
            if not visited[nei]:
                dfs(nei)
    C=[0]
    for i in range(n):
        if not visited[i]:
            dfs(i)
            C[0]+=1
    return n-C[0]


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
        if self.rank[pu]>self.rank[pv]:
            self.parent[pv]=pu
        elif self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1

def optimal(stones):
    n=len(stones)
    row=col=0
    for r,c in stones:
        row=max(row,r)
        col=max(col,c)
    offset=row+1
    dsu=DSU(row+col+2)
    for r,c in stones:
        dsu.union(r,c+offset)
    C=len(set(dsu.find(r) for r,c in stones))
    return n-C

if __name__ == "__main__":
    stones = [[0,0],[0,1],[1,0],[1,2],[2,2],[2,3]]
    print("Brute Force:", brute(stones))
    print("Optimal DSU:", optimal(stones))