def brute(grid):
    row,col=len(grid),len(grid[0])
    rz=[1]*row
    cz=[1]*col
    for i in range(row):
        for j in range(col):
            if grid[i][j]==0:
                rz[i]=0
                cz[j]=0
    for i in range(row):
        for j in range(col):
            if rz[i]==0 or cz[j]==0:
                grid[i][j]=0
    return grid

def optimal(grid):
    row,col=len(grid),len(grid[0])
    fr=any(grid[0][j]==0 for j in range(col))
    fc=any(grid[i][0]==0 for i in range(row))
    for i in range(1,row):
        for j in range(1,col):
            if grid[i][j]==0:
                grid[i][0]=0
                grid[0][j]=0
    for i in range(1,row):
        for j in range(1,col):
            if grid[i][0]==0 or grid[0][j]==0:
                grid[i][j]=0
    if fr:
        for j in range(col):
            grid[0][j]=0
    if fc:
        for i in range(row):
            grid[i][0]=0
    return grid

matrix = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
print('Brute: ',brute([row[:] for row in matrix]))
print('Optimal: ',optimal([row[:] for row in matrix]))