def brute(V,adj):
    def dfs(u,visited,removed):
        visited[u]=True
        for v in adj[u]:
            if not visited[v] and v!=removed:
                dfs(v, visited, removed)
    result=[]
    for removed in range(V):
        visited=[False]*V
        start=0 if removed != 0 else 1
        dfs(start,visited,removed)
        count=sum(visited)  
        if count<V - 1:
            result.append(removed)
    return result if result else [-1]

def optimal(V,adj):
    time=[0]
    visited=[False]*V
    tin=[-1]*V
    low=[-1]*V
    res=set()
    def dfs(node,parent):
        tin[node]=low[node]=time[0]
        time[0]+=1
        children=0
        visited[node]=True
        for nei in adj[node]:
            if nei==parent:
                continue
            if not visited[nei]:
                dfs(nei,node)
                low[node]=min(low[node],low[nei])
                if parent!=-1 and low[nei]>=tin[node]:
                    res.add(node)
                children+=1
            else:
                low[node]=min(low[node],tin[nei])
            if parent==-1 and children>1:
                res.add(node)
    dfs(0,-1)
    return list(res)

V = 5
adj = [
    [1, 2],
    [0, 2],
    [0, 1, 3, 4],
    [2, 4],
    [2, 3]
]
print('Brute: ',brute(V,adj))
print("Optimal: ",optimal(V,adj))