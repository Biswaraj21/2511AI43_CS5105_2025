from collections import deque

def brute(grid):
    row,col=len(grid),len(grid[0])
    mins=0
    while(True):
        changed=False
        copy=[row[:] for row in grid]
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                        nr,nc=r+dr,c+dc
                        if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                            copy[nr][nc]=2
                            changed=True
        if changed==False:
            break
        mins+=1
        grid=copy
    for r in grid:
        if 1 in r:
            return -1
    return mins

def optimal(grid):
    row,col=len(grid),len(grid[0])
    q=deque()
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    fresh=0
    for r in range(row):
        for c in range(col):
            if grid[r][c]==2:
                q.append((r,c,0))
            if grid[r][c]==1:
                fresh+=1
    timemax=0
    while q:
        r,c,t=q.popleft()
        timemax=max(t,timemax)
        for dr,dc in directions:
            nr,nc=r+dr,c+dc
            if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                grid[nr][nc]=2
                q.append((nr,nc,t+1))
                fresh-=1
    return -1 if fresh>0 else timemax

if __name__=="__main__":
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print("Brute: ",brute(grid))
    print("Optimal: ",optimal(grid))