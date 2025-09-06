def brute(V,edge):
    adj=[[] for _ in range(V)]
    for u,v,w in edge:
        adj[u].append((v,w))
    min_dist=[float('inf')]*V
    min_dist[0]=0
    def dfs(node,dist):
        for nei,w in adj[node]:
            if min_dist[nei]>dist+w:
                min_dist[nei]=dist+w
                dfs(nei,dist+w)
    dfs(0,0)
    return [d if d!=float('inf') else -1 for d in min_dist]

from collections import deque
def optimal(V,edge):
    adj=[[] for _ in range(V)]
    for u,v,w in edge:
        adj[u].append((v,w))
    topo=[]
    q=deque()
    indegree=[0]*V
    for u,v,w in edge:
        indegree[v]+=1
    for i in range(V):
        if indegree[i]==0:
            q.append(i)
    while q:
        node=q.popleft()
        topo.append(node)
        for nei,w in adj[node]:
            indegree[nei]-=1
            if indegree[nei]==0:
                q.append(nei)
    mindist=[float('inf')]*V
    mindist[0]=0
    for i in topo:
        if mindist[i]!=float('inf'):
            for nei,w in adj[i]:
                if mindist[nei]>mindist[i]+w:
                    mindist[nei]=mindist[i]+w
    return [d if d!=float('inf') else -1 for d in mindist]

if __name__ == "__main__":
    V = 6
    edges = [
        (0, 1, 2), (0, 4, 1),
        (1, 2, 3), (4, 2, 2),
        (4, 5, 4), (2, 3, 6),
        (5, 3, 1)
    ]

    print("Brute Force:", brute(V, edges))
    print("Optimal TopoSort:", optimal(V, edges))