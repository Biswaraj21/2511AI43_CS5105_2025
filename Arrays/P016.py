def brute(nums):
    n=len(nums)
    max_prod=float('-inf')
    for i in range(n-1):
        prod=1
        for j in range(i,n):
            prod*=nums[i]
        max_prod=max(max_prod,prod)
    return max_prod

def optimal(nums):
    n=len(nums)
    min_prod=max_prod=result=nums[0]
    for i in range(1,n-1):
        if nums[i]<0:
            min_prod,max_prod=max_prod,min_prod
        min_prod=min(nums[i],min_prod*nums[i])
        max_prod=max(max_prod*nums[i],nums[i])
        result=max(result,max_prod)
    return result

if __name__=='__main__':
    nums=input('Enter nums: ').split()
    nums=list(map(int,nums))
    print('Brute: ',brute(nums))
    print('Optimal: ',optimal(nums))