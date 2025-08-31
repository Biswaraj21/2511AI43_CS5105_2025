def brute(grid,src,dest):
    row,col=len(grid),len(grid[0])
    visited=[[False]*col for _ in range(row)]
    min_dist=[float('inf')]
    def dfs(r,c,dist):
        if r<0 or c<0 or r>=row or c>=col or grid[r][c]==0 or visited[r][c]:
            return
        if (r,c)==dest:
            min_dist[0]=min(min_dist[0],dist)
            return
        visited[r][c]=True
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            dfs(r+dr,c+dc,dist+1)
        visited[r][c]=False
    if grid[src[0]][src[1]]==0 or grid[dest[0]][dest[1]]==0:
        return -1
    dfs(src[0],src[1],0)
    return -1 if min_dist[0]==float("inf") else min_dist[0]

from collections import deque
def optimal(grid,src,dest):
    row,col=len(grid),len(grid[0])
    visited=[[False]*col for _ in range(row)]
    q=deque([(src[0],src[1],0)])
    if grid[src[0]][src[1]]==0 or grid[dest[0]][dest[1]]==0:
        return -1
    visited[src[0]][src[1]]=True
    while q:
        r,c,d=q.popleft()
        if (r,c)==dest:
            return d
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<row and 0<=nc<col and not visited[nr][nc] and grid[nr][nc]==1:
                visited[nr][nc]=True
                q.append((nr,nc,d+1))
    return -1

if __name__ == "__main__":
    grid = [
        [1, 1, 0, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 0],
        [1, 1, 1, 1]
    ]
    src = (0, 0)
    dest = (3, 3)

    print("Brute Force:", brute(grid, src, dest))
    print("Optimal BFS:", optimal(grid, src, dest))