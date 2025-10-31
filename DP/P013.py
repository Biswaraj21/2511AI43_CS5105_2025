def brute(arr,k):
    n=len(arr)
    def helper(i,target):
        if target==0:
            return True
        if i==0:
            return arr[0]==target
        not_pick=helper(i-1,target)
        pick=False
        if arr[i]<=target:
            pick=helper(i-1,target-arr[i])
        return pick or not_pick
    return helper(n-1,k)

def optimal(arr,k):
    n=len(arr)
    prev=[False]*(k+1)
    prev[0]=True
    if arr[0]<=k:
        prev[arr[0]]=True
    for i in range(1,n):
        curr=[False]*(k+1)
        curr[0]=True
        for target in range(1,k+1):
            not_pick=prev[target]
            pick=False
            if arr[i]<=target:
                pick=prev[target-arr[i]]
            curr[target]=pick or not_pick
        prev=curr
    return prev[k]

arr=list(map(int,input("Enter elements: ").split()))
k=int(input("Enter target: "))
print("Brute: ",brute(arr,k))
print("Optimal: ",optimal(arr,k))