def brute(m,n):
    def dfs(i,j):
        if i>=m or j>=n:
            return 0
        if i==m-1 and j==n-1:
            return 1
        tot=dfs(i+1,j)+dfs(i,j+1)
        return tot
    return dfs(0,0)

def optimal(m,n):
    prev=[1]*n
    for i in range(1,m):
        curr=[0]*n
        for j in range(n):
            left=curr[j-1] if j>0 else 0
            curr[j]=left+prev[j]
        prev=curr
    return prev[-1]

m,n=map(int,input("Enter m and n: ").split())
print("Brute: ",brute(m,n))
print("Optimal: ",optimal(m,n))