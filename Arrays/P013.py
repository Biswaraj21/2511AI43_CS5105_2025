def brute(nums):
    n=len(nums)
    res=[]
    for i in range(n):
        c=0
        for j in range(i+1,n):
            if nums[i]<nums[j]:
                c=1
        if c==0:
            res.append(nums[i])
    return res

def optimal(nums):
    n=len(nums)
    res=[]
    maxl=0
    for i in range(n-1,0,-1):
        if nums[i]>maxl:
            res.append(nums[i])
            maxl=nums[i]
    return res

if __name__=='__main__':
    nums=input('Enter numbers: ').split()
    nums=list(map(int,nums))
    print('Brute: ',brute(nums))
    print('optimal: ',optimal(nums))