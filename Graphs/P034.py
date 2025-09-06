def floyd_warshall(matrix):
    n=len(matrix)
    INF=10**9
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==-1 and i!=j:
                matrix[i][j]=INF
        matrix[i][i]=0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][j]>matrix[i][k]+matrix[k][j]:
                    matrix[i][j]=matrix[i][k]+matrix[k][j]
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==INF and i!=j:
                matrix[i][j]=-1
    return matrix

mat = [
    [0, 3, -1, 7],
    [-1, 0, 2, -1],
    [-1, -1, 0, 1],
    [6, -1, -1, 0]
]

floyd_warshall(mat)
print(mat)