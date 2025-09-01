def brute(n,road):
    adj=[[] for _ in range(n)]
    for u,v,w in road:
        adj[u].append((v,w))
        adj[v].append((u,w))
    min_time=[float("inf")]
    count=[0]
    def dfs(node,target,visited,time):
        if node==target:
            if time<min_time[0]:
                min_time[0]=time
                count[0]=1
            elif time==min_time[0]:
                count[0]+=1
        if time>min_time[0]:
            return
        visited[node]=True
        for v,t in adj[node]:
            if not visited[v]:
                dfs(v,target,visited,time+t)
        visited[node]=False
    visited=[False]*n
    dfs(0,n-1,visited,0)
    return count[0]


MOD=10**9+7
import heapq
def optimal(n,road):
    adj=[[] for _ in range(n)]
    for u,v,w in road:
        adj[u].append((v,w))
        adj[v].append((u,w))
    dist=[float('inf')]*n
    ways=[0]*n
    dist[0]=0
    ways[0]=1
    pq=[(0,0)]
    while pq:
        d,u=heapq.heappop(pq)
        if d>dist[u]:
            continue
        for v,w in adj[u]:
            if dist[v]>dist[u]+w:
                dist[v]=dist[u]+w
                ways[v]=ways[u]
                heapq.heappush(pq,(dist[v],v))
            elif dist[v]==dist[u]+w:
                ways[v]=(ways[u]+ways[v])%MOD
    return ways[n-1]%MOD

n = 7
roads = [
    [0,6,7],
    [0,1,2],
    [1,2,3],
    [1,3,3],
    [6,3,3],
    [3,5,1],
    [6,5,1],
    [2,5,1],
    [0,4,5],
    [4,6,2]
]
print("Brute: ",brute(n,roads))
print("Opitimal: ",optimal(n,roads))