def kosaraju(V,adj):
    visited=[False]*V
    stack=[]
    def dfs(node,adjm):
        visited[node]=True
        for nei in adjm[node]:
            if not visited[nei]:
                dfs(nei,adjm)
        stack.append(node)
    dfs(0,adj)
    visited=[False]*V
    rev=[[]for _ in range(V)]
    for u in range(V):
        for v in adj[u]:
            rev[v].append(u)
    SSC=0
    while stack:
        node=stack.pop()
        if not visited[node]:
            dfs(node,rev)
            SSC+=1
    return SSC

V = 5
adj = [
    [2, 3],   
    [0],      
    [1],      
    [4],      
    []       
]
print("SCC Count:", kosaraju(V, adj))