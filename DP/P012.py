def brute(grid):
    n,m=len(grid),len(grid[0])
    def dfs(i,j1,j2):
        if j1>=m or j1<0 or j2>=m or j2<0:
            return float('-inf')
        if i==n-1:
            if j1==j2:
                return grid[i][j1]
            else:
                return grid[i][j1]+grid[i][j2]
        res=0
        if j1==j2:
            res=grid[i][j1]
        else:
            res=grid[i][j1]+grid[i][j2]
        maxi=float('-inf')
        for dj1 in [-1,0,1]:
            for dj2 in [-1,0,1]:
                maxi=max(maxi,dfs(i+1,j1+dj1,j2+dj2))
        return res+maxi
    return dfs(0,0,m-1)

def optimal(grid):
    n,m=len(grid),len(grid[0])
    prev=[[0]*m for _ in range(m)]
    for j1 in range(m):
        for j2 in range(m):
            if j1==j2:
                prev[j1][j2]=grid[n-1][j1]
            else:
                prev[j1][j2]=grid[n-1][j1]+grid[n-1][j2]
    for i in range(n-2,-1,-1):
        curr=[[0]*m for _ in range(m)]
        for j1 in range(m):
            for j2 in range(m):
                maxi=float('-inf')
                for dj1 in [-1,0,1]:
                    for dj2 in [-1,0,1]:
                        val=0
                        if j1==j2:
                            val=grid[i][j1]
                        else:
                            val=grid[i][j1]+grid[i][j2]
                        if 0<=j1+dj1<m and 0<=j2+dj2<m:
                            val+=prev[j1+dj1][j2+dj2]
                        else:
                            val+=float('-inf')
                        maxi=max(maxi,val)
                curr[j1][j2]=maxi
        prev=curr
    return prev[0][m-1]


mat = [
  [2, 3, 1, 2],
  [3, 4, 2, 2],
  [5, 6, 3, 5]
]
print("Brute: ",brute(mat))
print("Optimal: ",optimal(mat))