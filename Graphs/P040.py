def brute(grid):
    row,col=len(grid),len(grid[0])
    count=[0]
    def dfs(r,c,visited):
        visited[r][c]=True
        count[0]+=1
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr,nc=dr+r,dc+c
            if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1 and not visited[nr][nc]:
                dfs(nr,nc,visited)
    max_area=0
    for i in range(row):
        for j in range(col):
            if grid[i][j]==0:
                grid[i][j]=1
                count[0]=0
                visited=[[False]*col for _ in range(row)]
                dfs(i,j,visited)
                grid[i][j]=0
                max_area=max(max_area,count[0])
    count[0]=0
    visited=[[False]*col for _ in range(row)]
    dfs(i,j,visited)
    max_area=max(max_area,count[0])
    return max_area

class DSU:
    def __init__(self,V):
        self.parent=[i for i in range(V)]   
        self.size=[1]*V
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        px,py=self.find(x),self.find(y)
        if px==py:
            return
        if self.size[px]>=self.size[py]:
            self.parent[py]=px
            self.size[px]+=self.size[py]
        else:
            self.parent[px]=py
            self.size[py]+=self.size[px]

def optimal(grid):
    row,col=len(grid),len(grid[0])
    dsu=DSU(row*col)
    for i in range(row):
        for j in range(col):
            if grid[i][j]==1:
                for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                    nr,nc=dr+i,dc+j
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc] and dsu.find(i*col+j)!=dsu.find(nr*col+nc):
                        dsu.union(i*col+j,nr*row+nc)
    max_area=0
    for i in range(row):
        for j in range(col):
            if grid[i][j]==0:
                seen=set()
                area=1
                for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                    nr,nc=dr+i,dc+j
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                        if dsu.parent[nr*col+nc] not in seen:
                            area+=dsu.size[dsu.parent[nr*col+nc]]
                            seen.add(dsu.parent[nr*col+nc])
                max_area=max(max_area,area)
    if max_area==0:
        return row*col
    return max_area


grid = [
    [1, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 1]
]


print("Brute Force: ", brute(grid))
print("Optimal:", optimal(grid))