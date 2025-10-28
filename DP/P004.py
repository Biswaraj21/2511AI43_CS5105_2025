def brute(arr,i):
    if i==0:
        return arr[0]
    if i<0:
        return 0
    pick=arr[i]+brute(arr,i-2)
    not_pick=brute(arr,i-1)
    return max(pick,not_pick)

def optimal(arr):
    n=len(arr)
    if n==0:
        return 0
    if n==1:
        return arr[0]
    dp=[0]*n
    dp[0]=arr[0]
    dp[1]=max(arr[0],arr[1])
    for i in range(1,n):
        pick=arr[i]+dp[i-2]
        not_pick=dp[i-1]
        dp[i]=max(pick,not_pick)
    #print(dp)
    return dp[-1]

arr=list(map(int,input("Enter elements: ").split()))
print("Brute: ",brute(arr,len(arr)-1))
print("Optimal: ",optimal(arr))