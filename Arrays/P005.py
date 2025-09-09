def brute(nums):
    n=len(nums)
    temp=[0]*n
    for i in range(1,n):
        temp[i-1]=nums[i]
    temp[n-1]=nums[0]
    return temp


def optimal(nums):
    n=len(nums)
    temp=nums[0]
    for i in range(1,n):
        nums[i-1]=nums[i]
    nums[n-1]=temp
    return nums

if __name__=='__main__':
    arr=input('Enter elements: ').split()
    print('Brute: ',brute(arr))
    print('Optimal: ',optimal(arr))