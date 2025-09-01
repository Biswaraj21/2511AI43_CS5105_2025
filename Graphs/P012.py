def dfs_traversal(n,edge):
    adj=[[] for _ in range(n)]
    for r,c in edge:
        adj[r].append(c)
        adj[c].append(r)
    visited=[False]*n
    res=[]
    def dfs(node):
        visited[node]=True
        res.append(node)
        for nei in adj[node]:
            if not visited[nei]:
                dfs(nei)
    for i in range(n):
        if not visited[i]:
            dfs(i)
    return res

n = 5
edges = [[0,1],[0,2],[1,3],[1,4]]

print(dfs_traversal(n, edges))