def optimal(nums,target):
    n=len(nums)
    nums.sort()
    res=[]
    for i in range(n-3):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>0 and nums[j]==nums[j-1]:
                continue
            k=j+1
            l=n-1
            while(k<l):
                tot=nums[i]+nums[j]+nums[k]+nums[l]
                if tot==target:
                    res.append([nums[i],nums[j],nums[k],nums[l]])
                    k+=1
                    l-=1
                    while k<l and nums[k]==nums[k-1]:
                        k+=1
                    while l>k and nums[l]==nums[l+1]:
                        l-=1
                elif tot>target:
                    l-=1
                else:
                    k+=1
    return res

nums = [1,0,-1,0,-2,2]
target = 0
print(optimal(nums, target))
