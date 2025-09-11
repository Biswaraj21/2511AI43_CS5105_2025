def brute(nums,target):
    n=len(nums)
    c=0
    for i in range(n):
        s=0
        for j in range(i+1,n):
            s+=nums[j]
        if s==target:
            c+=1
    return c

def optimal(nums,target):
    n=len(nums)
    c=0
    prev_sum=set()
    s=0
    for n in nums:
        s+=n
        if s==target:
            c+=1
        elif s>target:
            if s-target in prev_sum:
                c+=1
        prev_sum.add(s)
    return c

if __name__=='__main__':
    nums=input('Enter numbers: ').split()
    nums=list(map(int,nums))
    target=int(input('Enter target: '))
    print('Brute: ',brute(nums,target))
    print('optimal: ',optimal(nums,target))