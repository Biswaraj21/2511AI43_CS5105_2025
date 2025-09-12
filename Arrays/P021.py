def brute(nums,target):
    n=len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
    return [-1,-1]

def optimal(nums,target):
    n=len(nums)
    seen={}
    for i in range(n):
        if target-nums[i] in seen:
            return [seen[target-nums[i]],i]
        seen[nums[i]]=i
    return [-1,-1]

if __name__=='__main__':
    nums=input('Enter array: ').split()
    nums=list(map(int,nums))
    target=int(input("Enter target: "))
    print('Brute: ',brute(nums,target))
    print('Optimal: ',optimal(nums,target))