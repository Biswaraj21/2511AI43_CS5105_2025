import heapq
def prims(V,edges):
    adj=[[] for _ in range(V)]
    for u,v,w in edges:
        adj[u].append((v,w))
        adj[v].append((u,w))
    q=[[0,0,0]]
    wt=0
    visited=[False]*V
    mst=[]
    while q:
        w,s,e=heapq.heappop(q)
        if visited[e]:
            continue
        if w!=0:
            mst.append((s,e))
        wt+=w
        visited[e]=True
        for nei,d in adj[e]:
            if not visited[nei]:
                heapq.heappush(q,(d,e,nei))
    print('Weight: ',wt)
    print("MST: \n",mst)

V = 5
edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]
prims(V,edges)