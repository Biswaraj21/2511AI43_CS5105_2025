# Let’s divide the array into two subsets:

# S1: numbers with a + sign

# S2: numbers with a − sign

# Then:
#     sum(S1)−sum(S2)=Target
# and since all numbers are used,
#     sum(S1)+sum(S2)=totalSum    

# Adding both equations:
#     2×sum(S1)=Target+totalSum
#     ⇒sum(S1)=(Target+totalSum)//2​

# ✅ So this problem reduces to counting the number of subsets with sum = (Target + totalSum)/2.

def brute(arr,k):
    n=len(arr)
    tot=sum(arr)
    target=(k+tot)//2
    if (k + tot) % 2 != 0 or tot < abs(k):
        return 0
    def helper(i,target):
        if target==0:
            return 1
        if i==0:
            return 1 if arr[i]==target else 0
        not_pick=helper(i-1,target)
        pick=0
        if arr[i]<=target:
            pick=helper(i-1,target-arr[i])
        return pick+not_pick
    return helper(n-1,target)
    
def optimal(arr,k):
    n=len(arr)
    tot=sum(arr)
    target=(k+tot)//2
    if (k + tot) % 2 != 0 or tot < abs(k):
        return 0
    prev=[0]*(target+1)
    prev[0]=1
    if arr[0]<=target:
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

arr=list(map(int,input("Enter elements: ").split()))
k=int(input("Enter target: "))
print("Brute: ",brute(arr,k))
print("Optimal: ",optimal(arr,k))