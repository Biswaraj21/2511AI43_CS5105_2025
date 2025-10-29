def brute(matrix):
    n,m=len(matrix),len(matrix[0])
    def dfs(i,j):
        if i>=n or j>=m:
            return float('inf')
        if i==n-1 and j==m-1:
            return matrix[i][j]
        down=matrix[i][j]+dfs(i+1,j)
        right=matrix[i][j]+dfs(i,j+1)
        return min(down,right)
    return dfs(0,0)

def optimal(matrix):
    n,m=len(matrix),len(matrix[0])
    prev=[float('inf')]*m
    for i in range(n):
        curr=[float('inf')]*m
        for j in range(m):
            if i==0 and j==0:
                curr[j]=matrix[i][j]
                continue
            up=matrix[i][j]+prev[j] if i>0 else float('inf')
            left=matrix[i][j]+curr[j-1] if j>0 else float('inf')
            curr[j]=min(up,left)
        prev=curr
    return prev[-1]

grid = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]
print("Brute: ",brute(grid))
print("Optimal: ",optimal(grid))