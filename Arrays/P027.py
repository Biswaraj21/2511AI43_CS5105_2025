def brute(grid):
    n=len(grid)
    res=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[j][n-1-i]=grid[i][j]
    return res

def optimal(grid):
    n=len(grid)
    for i in range(n):
        for j in range(i+1,n):
            grid[i][j],grid[j][i]=grid[j][i],grid[i][j]
    for i in range(n):
        grid[i].reverse()
    return grid

mat2 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print('Brute: ',brute(mat2))
print("Optimal: ",optimal(mat2))