def brute(nums):
    n=len(nums)
    for i in range(n):
        c=0
        for j in range(n):
            if nums[i]==nums[j]:
                c+=1
        if c!=2:
            return nums[i]
    return -1

def optimal(nums):
    n=len(nums)
    res=nums[0]
    for i in range(1,n):
        res^=nums[i]
    return res

if  __name__=='__main__':
    nums=input('Enter elements: ').split()
    nums=list(map(int,nums))
    print('Brute: ',brute(nums))
    print('optimal: ',optimal(nums))