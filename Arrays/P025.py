def optimal(nums):
    n=len(nums)
    i=n-2
    while(i>0 and nums[i]>nums[i+1]):
        i-=1
    if i>=0:
        j=n-1
        while(nums[j]<=nums[i]):
            j-=1
        nums[i],nums[j]=nums[j],nums[i]
    nums[i+1:]=reversed(nums[i+1:])
    return nums

if __name__=='__main__':
    nums=input("Enter array: ").split()
    nums=list(map(int,nums))
    #print("Brute: ",brute(nums))
    print("Optimal: ",optimal(nums))