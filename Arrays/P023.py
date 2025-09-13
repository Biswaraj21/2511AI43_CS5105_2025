def brute(nums):
    n=len(nums)
    max_sum=float('-inf')
    for i in range(n):
        suma=0
        for j in range(i,n):
            suma+=nums[j]
            max_sum=max(max_sum,suma)
    return max_sum

def optimal(nums):
    n=len(nums)
    cur_sum=max_sum=nums[0]
    for i in range(1,n):
        cur_sum=max(cur_sum+nums[i],nums[i])
        max_sum=max(max_sum,cur_sum)
    return max_sum

if __name__=='__main__':
    nums=input("Enter array: ").split()
    nums=list(map(int,nums))
    print("Brute: ",brute(nums))
    print("Optimal: ",optimal(nums))