def brute(nums):
    n=len(nums)
    longest=seq=0
    for i in range(n-1):
        seq=0
        x=nums[i]
        while x in nums:
            seq+=1
            x+=1
        longest=max(longest,seq)
    return longest

def optimal(nums):
    n=len(nums)
    longest=seq=0
    for i in range(n-1):
        if nums[i]-1 not in nums:
            x=nums[i]
            seq=0
            while x in nums:
                seq+=1
                x+=1
            longest=max(longest,seq)
    return longest

if __name__=='__main__':
    nums=input('Enter numbers: ').split()
    nums=list(map(int,nums))
    print('Brute: ',brute(nums))
    print('Optimal: ',optimal(nums))