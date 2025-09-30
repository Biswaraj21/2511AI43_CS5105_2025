def brute(nums):
    n=len(nums)
    res=set()
    for i in  range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==0:
                    res.add(tuple(sorted([nums[i],nums[j],nums[k]])))
    return [list(triplets) for triplets in res]

def optimal(nums):
    n=len(nums)
    nums.sort()
    res=[]
    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=n-1
        while (left<right):
            if nums[i]+nums[left]+nums[right]==0:
                res.append([nums[i],nums[left],nums[right]])
                left+=1
                right-=1
                while left<right and nums[left-1]==nums[left]:
                    left+=1
                while left<right and nums[right+1]==nums[right]:
                    right+=1
            elif nums[i]+nums[left]+nums[right]<0:
                left+=1
            else:
                right-=1
    return res

nums=input("Enter array: ").split()
nums=list(map(int,nums))
print("Brute: ",brute(nums))
print("Optimal: ",optimal(nums))