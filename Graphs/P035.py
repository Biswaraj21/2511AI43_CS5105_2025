import heapq
def brute(n,edge,threshold):
    adj=[[] for i in range(n)]
    for u,v,w in edge:
        adj[u].append((v,w))
        adj[v].append((u,w))
        def dijkstra(node):
            dist=[float('inf')]*n
            dist[node]=0
            q=[(0,node)]
            while q:
                d,u= heapq.heappop(q)
                if dist[u]<d:
                    continue
                for v,w in adj[u]:
                    if dist[v]<d+w:
                        dist[v]=d+w
                        heapq.heappush(q,(dist[v],v))
            return dist
        min_count=float('inf')
        res=-1
        for i in range(n):
            dist=dijkstra(i)
            count=0
            for k in dist:
                if k<=threshold:
                    count+=1
            if count<=min_count:
                min_count=count
                res=i
        return res
    

def optimal(n,edge,threshold):
    grid=[[float('inf')]*n for _ in range(n)]
    for u,v,w in edge:
        grid[u][v]=grid[v][u]=w
    for i in range(n):
        grid[i][i]=0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if grid[i][j]>grid[i][k]+grid[k][j]:
                    grid[i][j]=grid[i][k]+grid[k][j]
    min_count=float('inf')
    res=-1
    for i in range(n):
        count=0
        for j in range(n):
            if grid[i][j]<=threshold and i!=j:
                count+=1
        if count<=min_count:
            min_count=count
            res=i
    return res

n = 4
edges = [[0,1,3],[1,2,1],[2,3,4],[0,3,7]]
threshold = 4

print(brute(n, edges, threshold))
print(optimal(n, edges, threshold))