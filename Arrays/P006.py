def brute(nums):
    n=len(nums)
    temp=[0]*n
    k=0
    for i in range(n):
        if nums[i]!=0:
            temp[k]=nums[i]
            k+=1
    return temp

def optimal(nums):
    n=len(nums)
    i=j=0
    while(j<n):
        if nums[j]==0:
            j+=1
            continue
        if nums[i]==0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j+=1
    return nums

if __name__=='__main__':
    arr=input('Enter elements: ').split()
    nums=list(map(int,arr))
    print('Brute: ',brute(nums))
    print('Optimal: ',optimal(nums))