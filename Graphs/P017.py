def brute(grid):
    row,col=len(grid),len(grid[0])
    visited=[[False]*col for _ in range(row)]
    count=[0]
    def dfs(r,c):
        if r==0 or c==0 or r==row-1 or c==col-1:
            return True
        visited[r][c]=True
        count[0]+=1
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr,nc=r+dr,c+dc
            if not visited[nr][nc] and grid[nr][nc]=='1':
                return dfs(nr,nc)
        return False
    tot=0
    for i in range(row):
        for j in range(col):
            if grid[i][j]=='1' and not visited[i][j]:
                count[0]=0
                if not dfs(i,j):
                    tot+=count[0]
    return tot

from collections import deque
def optimal(grid):
    row,col=len(grid),len(grid[0])
    q=deque()
    visited=[[False]*col for _ in range(row)]
    for i in range(col):
        if grid[0][i]=='1':
            q.append((0,i))
            visited[0][i]=True
        if grid[row-1][i]=='1':
            q.append((row-1,i))
            visited[row-1][i]=True
    for i in range(1,row-1):
        if grid[i][0]=='1':
            q.append((i,0))
            visited[i][0]=True
        if grid[i][col-1]=='1':
            q.append((i,col-1))
            visited[i][col-1]=True
    while q:
        r,c,=q.popleft()
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<row and 0<=nc<col and grid[nr][nc]=='1' and not visited[nr][nc]:
                visited[nr][nc]=True
                q.append((nr,nc))
    count=0
    for i in range(row):
        for j in range(col):
            if grid[i][j]=='1' and not visited[i][j]:
                count+=1
    return count

if __name__=="__main__":
    grid=[['0','0','0','0'],
          ['1','0','1','0'],
          ['0','1','1','0'],
          ['0','0','0','0']]
    print("Brute: ",brute(grid))
    print("Optimal: ",optimal(grid))