def brute(arr):
    n=len(arr)
    if sum(arr)%2!=0:
        return False
    def helper(i,target):
        if target==0:
            return True
        if i==0:
            return target==arr[0]
        not_pick=helper(i-1,target)
        pick=False
        if arr[i]<=target:
            pick=helper(i-1,target-arr[i])
        return pick or not_pick
    return helper(n-1,sum(arr)//2)

def optimal(arr):
    n=len(arr)
    tot=sum(arr)
    if tot%2!=0:
        return False
    k=tot//2
    prev=[False]*(k+1)
    prev[0]=True
    if arr[0]<k:
        prev[arr[0]]=True
    for i in range(1,n):
        curr=[0]*(k+1)
        curr[0]==True
        for target in range(1,k+1):
            not_pick=prev[target]
            pick=False
            if arr[i]<=target:
                pick=prev[target-arr[i]]
            curr[target]=pick or not_pick
        prev=curr
    return prev[k]

arr=list(map(int,input("Enter elements: ").split()))
print("Brute: ",brute(arr))
print("Optimal: ",optimal(arr))