def brute(matrix):
    n,m=len(matrix),len(matrix[0])
    def dfs(i,j):
        if i>=n or j>=m:
            return float('-inf')
        if i==n-1:
            return matrix[i][j]
        bottom=matrix[i][j]+dfs(i+1,j)
        diag=matrix[i][j]+dfs(i+1,j+1)
        inv=matrix[i][j]+dfs(i+1,j-1) if j>0 else float('-inf')
        return max(bottom,diag,inv)
    maxi=float('-inf')
    for i in range(m):
        maxi=max(dfs(0,i),maxi)
    return maxi

def optimal(matrix):
    n,m=len(matrix),len(matrix[0])
    prev=matrix[0][:]
    for i in range(1,n):
        curr=[float('-inf')]*m
        for j in range(m):
            top=prev[j]+matrix[i][j]
            tr=prev[j-1]+matrix[i][j] if j>0 else float('-inf')
            tl=prev[j+1]+matrix[i][j] if j<m-1 else float('-inf')
            curr[j]=max(top,tr,tl)
        prev=curr
    return max(prev)

grid=[[1,2,10,4],
      [100,3,2,1],
      [1,1,20,2],
      [1,2,2,1]]
print("Brute: ",brute(grid))
print("Optimal: ",optimal(grid))