def brute(V,adj,S):
    dist=[float("inf")]*V
    visited=[False]*V
    dist[S]=0
    for _ in range(V):
        u=-1
        minDist=float("inf")
        for i in range(V):
            if not visited[i] and minDist>dist[i]:
                minDist=dist[i]
                u=i
        if u==-1:
            break
        visited[u]=True
        for v,w in adj[u]:
            if not visited[v] and dist[v]>w+dist[u]:
                dist[v]=w+dist[u]
    return dist

import heapq

def optimal(V,adj,S):
    pq=[(S,0)]
    dist=[float('inf')]*V
    dist[S]=0
    while pq:
        u,d=heapq.heappop(pq)
        if d>dist[u]:
            continue
        for v,w in adj[u]:
            if w+dist[u]<dist[v]:
                dist[v]=w+dist[u]
                heapq.heappush(pq,(v,dist[v]))
    return dist

if __name__=="__main__":
     V = 5
     adj = {
        0: [[1, 2], [2, 4]],
        1: [[0, 2], [2, 1], [3, 7]],
        2: [[0, 4], [1, 1], [4, 3]],
        3: [[1, 7], [4, 2]],
        4: [[2, 3], [3, 2]]
    }
     S = 0

     print("Brute Force:",brute(V,adj,S))
     print("Optimal (PQ):",optimal(V,adj,S))