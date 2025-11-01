def brute(arr):
    n=len(arr)
    def helper(i,s1,total):
        if i==0:
            return abs(total-2*s1)
        not_pick=helper(i-1,s1,total)
        pick=helper(i-1,s1+arr[i],total)
        return min(not_pick,pick)
    return helper(n-1,0,sum(arr))

def optimal(arr):
    n=len(arr)
    target=sum(arr)//2
    prev=[False]*(target+1)
    prev[0]=True
    if arr[0]<=target:
        prev[arr[0]]=True
    for i in range(1,n):
        for j in range(target,arr[i]-1,-1):
            if prev[j-arr[i]]:
                prev[j]=True
    mini=float('inf')
    #print(prev)
    for i in range(1,target+1):
        if prev[i]:
            mini=min(mini,sum(arr)-2*i)
    return mini

arr=list(map(int,input("Enter arr: ").split()))
print("Brute: ",brute(arr))
print("Optimal: ",optimal(arr))