def brute(arr,k):
    n=len(arr)
    def helper(i,target):
        if target==0:
            return 1
        if i==0:
            return 1 if arr[0]==k else 0
        not_pick=helper(i-1,target)
        pick=0
        if arr[i]<=target:
            pick=helper(i-1,target-arr[i])
        return pick+not_pick
    return helper(n-1,k)

def optimal(arr,k):
    n=len(arr)
    prev=[0]*(k+1)
    prev[0]=1
    if arr[0]<k:
        prev[arr[0]]=1
    for i in range(1,n):
        curr=[0]*(k+1)
        curr[0]=1
        for j in range(k+1):
            not_pick=prev[j]
            pick=0
            if j<=arr[i]:
                pick=prev[j-arr[i]]
            curr[j]=pick+not_pick
        prev=curr
    return prev[k]

arr=list(map(int,input("Enter elements: ").split()))
k=int(input("Enter target: "))
print("Brute: ",brute(arr,k))
print("Optimal: ",optimal(arr,k))