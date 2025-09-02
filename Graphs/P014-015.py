from collections import deque
def brute(V,edge):
    adj=[[] for _ in range(V)]
    for u,v in edge:
        adj[u].append(v)
        adj[v].append(u)
    def bfs(u,v,banned):
        q=deque([u])
        visited=[False]*V
        visited[u]=True
        while q:
            node=q.popleft()
            if node==v:
                return True
            for nei in adj[node]:
                if (node,nei)==banned or (nei,node)==banned:
                    continue
                if not visited[nei]:
                    visited[nei]=True
                    q.append(nei)
        return False
    for u,v, in edge:
        if bfs(u,v,(u,v)):
            return True
    return False

class DSU:
    def __init__(self,V):
        self.parent=[i for i in range(V)]
        self.rank=[1]*V
    def find(self,u):
        if self.parent[u]==u:
            return u
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
            self.parent[pu]=pv
            self.rank[pv]+=1
        return True
    
def optimal(V,edge):
    adj=[[] for _ in range(V)]
    for u,v in edge:
        adj[u].append(v)
        adj[v].append(u)
    dsu=DSU(V)
    for u,v in edge:
        if not dsu.union(u,v):
            return True
    return False

from collections import deque
def bfs_cycle(V,edge):
    adj=[[] for _ in range(V)]
    for u,v in edge:
        adj[u].append(v)
        adj[v].append(u)
    visited=[False]*V
    visited[0]=True
    q=deque([(0,-1)])
    while q:
        node,parent=q.popleft()
        for nei in adj[node]:
            if not visited[nei]:        
                visited[node]=True
                q.append((nei,node))
            elif nei!=parent:
                return True
    return False

def dfs_cycle(V,edge):
    adj=[[] for _ in range(V)]
    for u,v in edge:
        adj[u].append(v)
        adj[v].append(u)
    visited=[False]*V
    #visited[0]=True
    def dfs(node,parent):
        for nei in adj[node]:
            if not visited[nei]:
                visited[nei]=True
                if dfs(nei,node):
                    return True
            elif nei!=parent:
                return True
        return False
    for i in range(V):
        if not visited[i]:
            if dfs(i,-1):
                return True
    return False

if __name__ == "__main__":
    V = 5
    edges = [(0,1),(1,2),(2,3),(3,4),(4,1)] 

    print("Brute Force:", brute(V, edges))
    print("Optimal :", optimal(V, edges))
    print("By BFS: ",bfs_cycle(V,edges))
    print("By DFS: ",dfs_cycle(V,edges))