def brute(s1,s2):
    n,m=len(s1),len(s2)
    def helper(i,j):
        if i==n and j==m:
            return True
        if i==n and j!=m:
            return False
        if j==m:
            return all(ch=='*' for ch in s1[i:])
        if s1[i]==s2[j] or s1[i]=='?':
            return helper(i+1,j+1)
        elif s1[i]=='*':
            return helper(i+1,j) or helper(i,j+1)
        else:
            return False
    return helper(0,0)

def optimal(s1,s2):
    n,m=len(s1),len(s2)
    dp=[[False]*(m+1) for _ in range(n+1)]
    dp[0][0]=True
    for i in range(1,n+1):
        dp[i][0]=dp[i-1][0] and s1[i-1]=='*'
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1] or s1[i-1]=='?':
                dp[i][j]=dp[i-1][j-1]
            elif s1[i-1]=='*':
                dp[i][j]=dp[i-1][j] or dp[i][j-1]
            else:
                dp[i][j]=False
    return dp[n][m]

s1=input("Enter s1:")
s2=input("Enter s2: ")
print("Brute: ",brute(s1,s2))
print("Optimal: ",optimal(s1,s2))
