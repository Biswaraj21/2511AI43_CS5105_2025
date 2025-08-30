from collections import deque

def brute(grid):
    row,col=len(grid),len(grid[0])
    dist=[[0]*col for _ in range(row)]
    for r in range(row):
        for c in range(col):
            if grid[r][c]==1:
                dist[r][c]=0
            else:
                minDist=float('inf')
                for i in range(row):
                    for j in range(col):
                        if grid[i][j]==1:
                            minDist=min(minDist,abs(i-r)+abs(j-c))
                dist[r][c]=minDist if minDist!=float('inf') else -1
    return dist

def optimal(grid):
    row,col=len(grid),len(grid[0])
    dist=[[-1]*col for _ in range(row)]
    q=deque()
    for r in range(row):
        for c in range(col):
            if grid[r][c]==1:
                dist[r][c]=1
                q.append((r,c,0))
    while q:
        r,c,d=q.popleft()
        for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<row and 0<=nc<col and dist[nr][nc]==-1:
                dist[nr][nc]=d+1
                q.append((nr,nc,d+1))
    return dist

if __name__=="__main__":
    grid=[
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 0]
]
    ans1=brute(grid)
    ans2=optimal(grid)
    print("For brute:\n ")
    for row in ans1:
        print(row)
    print("\nFor optimal:\n")
    for row in ans2:
        print(row)