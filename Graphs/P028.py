def brute(n,edge):
    adj=[[]for _ in range(n)]
    for u,v in edge:
        adj[u].append(v)
        adj[v].append(u)
    distmin=[float('inf')]*n
    def dfs(node,target,dist,visited):
        if node==target:
            distmin[node]=min(distmin[node],dist)
            return
        visited[node]=True
        for nei in adj[node]:
            if not visited[nei]:
                dfs(nei,target,dist+1,visited)
        visited[node]=False
    for i in range(n):
        visited=[False]*n
        dfs(0,i,0,visited)
    for i in range(n):
        if distmin[i]==float('inf'):
            distmin[i]=-1 
    return distmin

from collections import deque
def optimal(n,edge):
    adj=[[]for _ in range(n)]
    for u,v in edge:
        adj[u].append(v)
        adj[v].append(u)
    distmin=[float('inf')]*n
    q=deque([(0,0)])
    distmin[0]=0
    while q:
        node,dist=q.popleft()
        for nei in adj[node]:
            if distmin[nei]>dist+1:
                distmin[nei]=dist+1
                q.append((nei,dist+1))
    for i in range(n):
        if distmin[i]==float('inf'):
            distmin[i]=-1 
    return distmin

if __name__ == "__main__":
    V = 6
    edges = [(0,1),(0,2),(1,3),(2,3),(3,4)]

    print("Brute : ", brute(V, edges))
    print("Optimal :", optimal(V, edges))