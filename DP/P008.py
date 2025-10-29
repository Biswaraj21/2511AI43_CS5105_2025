def brute(matrix):
    n,m=len(matrix),len(matrix[0])
    def dfs(i,j):
        if i>=n or j>=m or matrix[i][j]==-1:
            return 0
        if i==n-1 and j==m-1:
            return 1
        tot=dfs(i+1,j)+dfs(i,j+1)
        return tot
    return dfs(0,0)

def optimal(matrix):
    n,m=len(matrix),len(matrix[0])
    prev=[0]*m
    for i in range(n):
        curr=[0]*m
        for j in range(m):
            if matrix[i][j]==-1:
                curr[j]=0
                continue
            if i==0 and j==0:
                curr[j]=1
                continue
            up=prev[j] if i>0 else 0
            left=curr[j-1] if j>0 else 0
            curr[j]=up+left
        prev=curr
    return prev[-1]

maze = [
 [0, 0, 0],
 [0, -1, 0],
 [0, 0, 0]
]
print("Brute: ",brute(maze))
print("Optimal: ",optimal(maze))
