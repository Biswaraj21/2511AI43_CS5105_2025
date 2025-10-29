def brute(matrix):
    n=len(matrix)
    def dfs(i,j):
        if i==n-1:
            return matrix[i][j]
        down=matrix[i][j]+dfs(i+1,j)
        diagonal=matrix[i][j]+dfs(i+1,j+1)
        return min(down,diagonal)
    return dfs(0,0)
    
def optimal(matrix):
    n=len(matrix)
    prev=matrix[-1][:]
    for i in range(n-2,-1,-1):
        curr=[0]*(i+1)
        for j in range(i+1):
            down=prev[j]
            diag=prev[j+1]
            curr[j]=matrix[i][j]+min(down,diag)
        prev=curr
    return prev[0]

triangle = [
  [1],
  [2, 3],
  [3, 6, 7],
  [8, 9, 6, 10]
]
print("Brute: ",brute(triangle))
print("Optimal: ",optimal(triangle))