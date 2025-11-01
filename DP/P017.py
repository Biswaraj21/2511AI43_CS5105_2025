# Let:
#     S1 + S2 = totalSum
# and
#     S1 − S2 = d

# Add both equations:

#     2S1 = d + totalSum
#     S1 = (d+totalSum)//2
# ✅ So we just need to count the number of subsets with sum = (d + totalSum)//2

def brute(arr,k):
    n=len(arr)
    tot=sum(arr)
    if (k+tot) % 2!=0:
        return 0
    target=(k+tot)//2
    def helper(i,target):
        if target==0:
            return 1
        if i==0:
            return 1 if target==arr[i] else 0
        not_pick=helper(i-1,target)
        pick=0
        if arr[i]<=target:
            pick=helper(i-1,target-arr[i])
        return pick+not_pick
    return helper(n-1,target)

def optimal(arr,k):
    n=len(arr)
    tot=sum(arr)
    if (k+tot) % 2!=0:
        return 0
    target=(k+tot)//2
    prev=[0]*(target+1)
    prev[0]=1
    if arr[0]<target:
        prev[arr[0]]=1
    for i in range(1,n):
        curr=[0]*(target+1)
        curr[0]=1
        for j in range(target+1):
            not_pick=prev[j]
            pick=0
            if arr[i]<=j:
                pick=prev[j-arr[i]]
            curr[j]=pick+not_pick
        prev=curr
    return prev[target]

arr=list(map(int,input("Enter arr: ").split()))
k=int(input("Enter difference: "))
print("Brute: ",brute(arr,k))
print("Optimal: ",optimal(arr,k))