def brute(nums,target):
    n=len(nums)
    max_len=0
    length=0
    for i in range(n):
        s=0
        length=0
        for j in range(i,n):
            s+=nums[j]
            length+=1
            if s==target:
                max_len=max(length,max_len)
    return max_len

def optimal(nums,target):
    n=len(nums)
    max_len=0
    prev_sum={}
    s=0
    for i in range(n):
        s+=nums[i]
        if s==target:
            max_len=max(max_len,i+1)
        if s-target in prev_sum:
            max_len=max(max_len,i-prev_sum[s-target])
        if s not in prev_sum:
            prev_sum[s]=i
    return max_len

if __name__=='__main__':
    nums=input('Enter numbers: ').split()
    nums=list(map(int,nums))
    target=int(input('Enter target: '))
    print('Brute: ',brute(nums,target))
    print('optimal: ',optimal(nums,target))