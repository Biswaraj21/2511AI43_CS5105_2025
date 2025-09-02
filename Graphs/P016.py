def brute(grid):
    row,col=len(grid),len(grid[0])
    visited=[[False]*col for _ in range(row)]
    def dfs(r,c,cells):
        visited[r][c]=True
        if r==0 or c==0 or r==row-1 or c==col-1:
            return True
        cells.append((r,c))
        touch_border=False
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr,nc=dr+r,dc+c
            if 0<=nr<row and 0<=nc<col and not visited[nr][nc] and grid[nr][nc]=='O':
                touch_border=touch_border or dfs(nr,nc,cells)
        return touch_border
    for i in range(row):
        for j in range(col):
            if grid[i][j]=='O' and visited[i][j]==False:
                cells=[]
                if not dfs(i,j,cells):
                    for r,c in cells:
                        grid[r][c]='X'
    return grid

def optimal(grid):
    row,col=len(grid),len(grid[0])
    visited=[[False]*col for _ in range(row)]
    def dfs_safe(r,c):
        grid[r][c]='S'
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr,nc=dr+r,dr+c
            if 0<=nr<row and 0<=c<col and grid[nr][nc]=='O':
                dfs_safe(nr,nc)
    for i in range(row):
        if grid[i][0]=='O':
            dfs_safe(i,0)
        if grid[i][col-1]=='O':
            dfs_safe(i,col-1)
    for i in range(col):
        if grid[0][i]=='O':
            dfs_safe(0,i)
        if grid[row-1][i]=='O':
            dfs_safe(row-1,i)
    def dfs(r,c):
        grid[r][c]='X'
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr,nc=dr+r,dr+c
            if 0<=nr<row and 0<=c<col and grid[nr][nc]=='O':
                dfs(nr,nc)
    for i in range(row):
        for j in range(col):
            if grid[i][j]=='O':
                dfs(i,j)
    def dfs_revert(r,c):
        grid[r][c]='O'
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr,nc=dr+r,dr+c
            if 0<=nr<row and 0<=c<col and grid[nr][nc]=='S':
                dfs_revert(nr,nc)
    for i in range(row):
        if grid[i][0]=='S':
            dfs_revert(i,0)
        if grid[i][col-1]=='S':
            dfs_revert(i,col-1)
    for i in range(col):
        if grid[0][i]=='S':
            dfs_revert(0,i)
        if grid[row-1][i]=='S':
            dfs_revert(row-1,i)
    return grid


matrix = [
    ['X','X','X','X'],
    ['X','O','O','X'],
    ['X','X','O','X'],
    ['X','O','X','X']
]

result1 = brute(matrix)
print("Brute: \n")
for row in result1:
    print(row)
result2 = optimal(matrix)
print("\nOptimal: \n")
for row in result2:
    print(row)