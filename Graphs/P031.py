def brute(n,flights,src,dst,k):
    city=[[] for i in range(n)]
    for u,v,w in flights:
        city[u].append((v,w))
    min_cost=[float('inf')]
    def dfs(node,cost,stop):
        if node==dst:
            min_cost[0]=min(min_cost[0],cost)
        if stop>k:
            return
        for nei,w in city[node]:
            dfs(nei,cost+w,stop+1)
    dfs(src,0,0)
    return min_cost[0] if min_cost[0]!=float('inf') else -1

import heapq
def optimal(n,flights,src,dest,k):
    city=[[] for i in range(n)]
    for u,v,w in flights:
        city[u].append((v,w))
    q=[(0,src,-1)]
    cost=[float('inf')]*n
    cost[src]=0
    while q:
        w,node,stop=heapq.heappop(q)
        if node==dest and stop<=k:
            return w
        for nei,d in city[node]:
            if cost[nei]>w+d and stop<k:
                cost[nei]=w+d
                heapq.heappush(q,(w+d,nei,stop+1))
    print(cost)
    return -1


if __name__ == "__main__":
    n = 4
    flights = [
        [0, 1, 100],
        [1, 2, 100],
        [2, 3, 100],
        [0, 2, 500]
    ]
    src, dst, k = 0, 3, 1
    
    print("Brute:", brute(n,flights,src,dst,k))
    print("Optimal:",optimal(n,flights,src,dst,k))
