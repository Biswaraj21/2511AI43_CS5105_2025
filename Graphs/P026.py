def brute(V,adj):
    safe=[False]*V
    visited=set()
    def dfs(node,visited,path):
        if  node in path:
            return False
        if node in visited:
            return True
        path.add(node)
        for nei in adj[node]:
            if not dfs(nei,visited,path):
                return False
        path.remove(node)
        visited.add(node)
        return True
    res=[]
    for i in range(V):
        if dfs(i,visited,set()):
            res.append(i)
    return res

from collections import deque
def optimal(V,adj):
    revgraph=[[]for _ in range(V)]
    outdegree=[0]*V
    for u in range(V):
        for v in adj[u]:
            revgraph[v].append(u)
            outdegree[u]+=1
    q=deque()
    for i in range(V):
        if outdegree[i]==0:
            q.append(i)
    while q:
        node=q.popleft()
        for nei in revgraph[node]:
            outdegree[nei]-=1
            if outdegree[nei]==0:
                q.append(nei)
    res=[]
    for i in range(V):
        if outdegree[i]==0:
            res.append(i)
    return res

V = 7
adj = [[1,2],[2,3],[5],[0],[5],[6],[]]
print('Brute: ',brute(V,adj))
print('Optimal: ',optimal(V,adj))