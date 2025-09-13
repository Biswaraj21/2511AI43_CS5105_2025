def brute(nums):
    n=len(nums)
    count0=count1=count2=0
    for n in nums:
        if n==0:
            count0+=1
        elif n==1:
            count1+=1
        else:
            count2+=1
    i=0
    for _ in range(count0):
        nums[i]=0
        i+=1
    for _ in range(count1):
        nums[i]=1
        i+=1
    for _ in range(count2):
        nums[i]=2
        i+=1    
    return nums

def optimal(nums):
    n=len(nums)
    low,mid,high=0,0,n-1
    while(mid<=high):
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums

if __name__=='__main__':
    nums=input('Enter array: ').split()
    nums=list(map(int,nums))
    print('Brute: ',brute(nums))
    print('Optimal: ',optimal(nums))