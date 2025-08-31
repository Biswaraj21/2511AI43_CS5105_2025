def brute(grid):
    row,col=len(grid),len(grid[0])
    visited=[[False]*col for _ in range(row)]
    visited[0][0]=True
    min_effort=[float('inf')]
    def dfs(r,c,current_effort):
        if r==row-1 and c==col-1:
            min_effort[0]=min(min_effort[0],current_effort)
            return
        visited[r][c]=True
        for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr,nc=dr+r,dc+c
            if 0<=nr<row and 0<=nc<col and not visited[nr][nc]:
                dfs(nr,nc,max(current_effort,abs(grid[r][c]-grid[nr][nc])))
        visited[r][c]=False
    dfs(0,0,0)
    return -1 if min_effort[0]==float("inf") else min_effort[0]

import heapq

def optimal(grid):
    row,col=len(grid),len(grid[0])
    effort=[[float('inf')]*col for _ in range(row)]
    effort[0][0]==0
    pq=[(0,0,0)]
    while pq:
        curr_effort,r,c=heapq.heappop(pq)
        if r==row-1 and c==col-1:
            return curr_effort
        for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr,nc=dr+r,dc+c
            if 0<=nr<row and 0<=nc<col:
                new_effort=max(curr_effort,abs(grid[r][c]-grid[nr][nc]))
                if curr_effort<effort[nr][nc]:
                    effort[nr][nc]=new_effort
                    heapq.heappush(pq,(effort[nr][nc],nr,nc))
    return -1
    
heights = [
    [1,2,2],
    [3,8,2],
    [5,3,5]
]

print("Brute Force:", brute(heights))   
print("Optimal Dijkstra:", optimal(heights))
