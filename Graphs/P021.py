def brute(V,edge):
    adj=[[] for _ in range(V)]
    for u,v in edge:
        adj[u].append(v)
    visited=[False]*V
    recStack=set()
    def dfs(node):
        visited[node]=True
        recStack.add(node)
        for nei in adj[node]:
            if not visited[nei]:
                return dfs(nei)
            elif node in recStack:
                return True
        recStack.remove(node)
        return False
    for i in range(V):
        if not visited[i]:
            if dfs(i):
                return True
    return False

from collections import deque
def optimal(V,edge):
    adj=[[] for _ in range(V)]
    indegree=[0]*V
    for u,v in edge:
        adj[u].append(v)
        indegree[v]+=1
    q=deque()
    for i in range(V):
        if indegree[i]==0:
            q.append(i)
    count=0
    while q:
        node=q.popleft()
        count+=1
        for nei in adj[node]:
            indegree[nei]-=1
            if indegree[nei]==0:
                q.append(nei)
    return count!=V

V = 4
edges = [(0, 1), (1, 2), (2, 0), (2, 3)]
print("Brute: ", brute(V, edges))
print("Optimal: ",optimal(V,edges))