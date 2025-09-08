def brute(grid):
    row,col=len(grid),len(grid[0])
    visited=[[False]*col for _ in range(row)]
    dir=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    def dfs(r,c):
        visited[r][c]=True
        for dr,dc in dir:
            nr,nc=dr+r,dc+c
            if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1 and not visited[nr][nc]:
                dfs(nr,nc)
    c=0
    for i in range(row):
        for j in range(col):
            if grid[i][j]==1 and not visited[i][j]:
                dfs(i,j)
                c+=1
    return c

class DSU:
    def __init__(self,V):
        self.parent=[i for i in range(V)]
        self.rank=[1]*V
    def find(self,u):
        if self.parent[u]==u:
            return u
        self.parent[u]=self.find(self.parent[u])
        return self.parent[u]
    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)
        if self.rank[pu]>self.rank[pv]:
            self.parent[pv]=pu
        elif self.rank[pv]>self.rank[pu]:
            self.parent[pu]=pv
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1

def optimal(grid):
    row,col=len(grid),len(grid[0])
    dsu=DSU(row*col)
    dir=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    for i in range(row):
        for j in range(col):
            if grid[i][j]==1:
                for dr,dc in dir:
                    nr,nc=dr+i,dc+j
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                        dsu.union(i*col+j,nr*col+nc)
    res=set()
    for i in range(row):
        for j in range(col):
            if grid[i][j]==1:
                res.add(dsu.find(i*col+j))
    return len(res)

if __name__=="__main__":
    grid=[[0,1,1,0],
          [0,1,1,0],
          [0,0,1,0],
          [0,0,0,0],
          [1,1,0,1]]
    print("Brute: ",brute(grid))
    print("Optimal: ",optimal(grid))