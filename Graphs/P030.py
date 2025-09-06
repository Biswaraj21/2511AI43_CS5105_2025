import heapq
def dijkstras(V,adj,S):
    dist=[float('inf')]*V
    dist[S]=0
    q=[]
    heapq.heappush(q,(0,S))
    while q:
        d,u=heapq.heappop(q)
        if d>dist[u]:
            continue
        for v,w in adj[u]:
            if dist[v]>d+w:
                dist[v]=d+w
                heapq.heappush(q,(dist[v],v))
    return [d if d!=float('inf') else -1 for d in dist]

if __name__ == "__main__":
    V = 5
    adj = [
        [(1, 2), (2, 4)],        
        [(0, 2), (2, 1), (3, 7)],
        [(0, 4), (1, 1), (4, 3)],
        [(1, 7), (4, 2)],        
        [(2, 3), (3, 2)]         
    ]
    S = 0
    print(dijkstras(V, adj, S))