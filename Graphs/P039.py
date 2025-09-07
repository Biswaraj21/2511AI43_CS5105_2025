def brute(n,m,k,arr):
    matrix=[[0]*m for _ in range(n)]
    def dfs(r,c,visited):
        visited[r][c]=True
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr,nc=dr+r,dc+c
            if 0<=nr<n and 0<=nc<m and matrix[nr][nc]==1 and not visited[nr][nc]:
                dfs(nr,nc,visited)
    res=[]
    for r,c in arr:
        count=0
        visited=[[False]*m for _ in range(n)]
        matrix[r][c]=1
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and matrix[i][j]==1:
                    dfs(i,j,visited)
                    count+=1
        res.append(count)
    return res

class DSU:
    def __init__(self,V):
        self.parent=[i for i in range(V)]
        self.rank=[1]*V
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        px,py=self.find(x),self.find(y)
        if self.rank[px]>self.rank[py]:
            self.parent[py]=px
        elif self.rank[py]>self.parent[px]:
            self.parent[px]=py
        else:
            self.parent[py]=px
            self.rank[px]+=1

def optimal(n,m,k,arr):
    dsu=DSU(n*m)
    res=[]
    matrix=[[0]*m for i in range(n)]
    count=0
    for r,c in arr:
        matrix[r][c]=1
        count+=1
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr,nc=dr+r,dc+c
            if 0<=nr<n and 0<=nc<m and matrix[nr][nc]==1 and dsu.find(r*n+c)!=dsu.find(nr*n+nc):
                dsu.union(r*n+c,nr*n+nc)
                count-=1
        res.append(count)
    return res

n, m, k = 3, 3, 5
ops = [(0,0),(0,1),(1,2),(2,1),(1,1)]
print('Brute: ',brute(n,m,k,ops))
print('Optimal: ',optimal(n,m,k,ops))