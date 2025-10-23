def brute(n):
    if n<2:
        return 1
    return brute(n-1)+brute(n-2)

def optimal(n):
    if n<2:
        return 1
    dp=[0]*(n+1)
    dp[0]=dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

n=int(input("Enter steps: "))
print("Brute: ",brute(n))
print("Optimal: ",optimal(n))