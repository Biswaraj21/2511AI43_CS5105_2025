def brute(i,height,k):
    if i==0:
        return 0
    min_energy=float('inf')
    for j in range(1,k+1):
        if i-j>=0:
            energy=brute(i-j,height,k)+abs(height[i]-height[i-j])
            min_energy=min(min_energy,energy)
    return min_energy

def optimal(height,k):
    n=len(height)
    dp=[0]*n
    dp[0]=0
    for i in range(1,n):
        min_energy=float('inf')
        for j in range(1,k+1):
            if j<=i:
                energy=dp[i-j]+abs(height[i]-height[i-j])
                min_energy=min(min_energy,energy)
        dp[i]=min_energy
    return dp[-1]

height=list(map(int,input("Enter height: ").split()))
k=int(input("Enter step: "))
print("Brute: ",brute(len(height)-1,height,k))
print("Optimal: ",optimal(height,k))