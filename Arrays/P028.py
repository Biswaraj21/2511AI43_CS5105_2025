def brute_spiral(matrix):
    if not matrix: 
        return []
    m, n = len(matrix), len(matrix[0])
    visited = [[False] * n for _ in range(m)]
    result = []

    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    dir_idx = 0
    x, y = 0, 0
    for _ in range(m * n):
        result.append(matrix[x][y])
        visited[x][y] = True
        nx, ny = x + directions[dir_idx][0], y + directions[dir_idx][1]
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
            x, y = nx, ny
        else:
            dir_idx = (dir_idx + 1) % 4
            x, y = x + directions[dir_idx][0], y + directions[dir_idx][1]
    return result


def optimal(grid):
    row,col=len(grid),len(grid[0])
    left,right,top,bottom=0,col-1,0,row-1
    res=[]
    while(right>=left and top<=bottom):
        for i in range(left,right+1):
            res.append(grid[top][i])
        top+=1
        for i in range(top,bottom+1):
            res.append(grid[i][right])
        right-=1
        for i in range(right,left-1,-1):
            res.append(grid[bottom][i])
        bottom-=1
        for i in range(bottom,top-1,-1):
            res.append(grid[i][left])
        left+=1
    return res

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

print("Brute:   ", brute_spiral(matrix))
print("Optimal: ", optimal(matrix))