def bellmanford(V,edge,S):
    dist=[float('inf')]*V
    dist[S]=0
    for _ in range(V-1):
        for u,v,w in edge:
            if dist[u]!=float('inf') and dist[v]>dist[u]+w:
                dist[v]=dist[u]+w
    for u,v,w in edge:
        if dist[u]!=float('inf') and dist[v]>dist[u]+w:
            return [-1]
    return [d if d!=float('inf') else -1 for d in dist]

if __name__ == "__main__":
    V = 5
    edges = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3)
    ]
    S = 0

    print("Shortest distances:", bellmanford(V, edges, S))