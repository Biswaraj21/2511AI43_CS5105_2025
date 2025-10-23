def brute(i,height):
    if i==0:
        return 0
    jump1=brute(i-1,height)+abs(height[i]-height[i-1])
    jump2=float('inf')
    if i>1:
        jump2=brute(i-2,height)+abs(height[i]-height[i-2])
    return min(jump1,jump2)

def optimal(height):
    n = len(height)
    dp = [0] * n
    dp[0] = 0
    for i in range(1, n):
        jump1 = dp[i - 1] + abs(height[i] - height[i - 1])
        jump2 = float('inf')
        if i > 1:
            jump2 = dp[i - 2] + abs(height[i] - height[i - 2])
        dp[i] = min(jump1, jump2)

    return dp[-1]


height=list(map(int,input("Enter height: ").split()))
dp=[-1]*len(height)
print("Brute: ",brute(len(height)-1,height))
print("Optimal: ",optimal(height))