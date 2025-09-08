def brute(n, connections):
    from collections import defaultdict
    adj =defaultdict(list)
    for u,v in connections:
        adj[u].append(v)
        adj[v].append(u)
    def dfs(node, visited):
        visited.add(node)
        for nei in adj[node]:
            if nei not in visited:
                dfs(nei,visited)
    bridges = []
    for u, v in connections:
        adj[u].remove(v)
        adj[v].remove(u)
        visited = set()
        dfs(0,visited)
        if len(visited)<n:
            bridges.append([u,v])
        adj[u].append(v)
        adj[v].append(u)
    return bridges

def optimal(n,connections):
    adj=[[]for _ in range(n)]
    for u,v in connections:
        adj[u].append(v)
        adj[v].append(u)
    tin=[-1]*n
    low=[-1]*n
    time=[0]
    visited=[False]*n
    res=[]
    def dfs(node,parent):
        tin[node]=low[node]=time[0]
        time[0]+=1
        visited[node]=True
        for nei in adj[node]:
            if nei==parent:
                continue
            if not visited[nei]:
                dfs(nei,node)
                low[node]=min(low[node],low[nei])
                if low[nei]>tin[node]:
                    res.append((node,nei))
            else:
                low[node]=min(low[node],tin[nei])
    dfs(0,-1)
    return res

n=4
connections =[[0,1],[1,2],[2,0],[1,3]]
print('Brute: ',brute(n, connections))
print('Optimal: ',optimal(n,connections))