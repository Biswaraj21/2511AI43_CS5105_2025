from collections import Counter
def brute(nums):
    n = len(nums)
    freq = Counter(nums)
    result = []
    for num, count in freq.items():
        if count > n // 3:
            result.append(num)
    return result


def optimal(nums):
    cand1,cand2=None,None
    count1=count2=0
    n=len(nums)
    for i in range(n):
        if cand1==nums[i]:
            count1+=1
        elif cand2==nums[i]:
            count2+=1
        elif count1==0:
            count1=1
            cand1=nums[i]
        elif count2==0:
            count2=1
            cand2=nums[i]
        else:
            count1-=1
            count2-=1
    count1=count2=0
    for i in range(n):
        if cand1==nums[i]:
            count1+=1
        elif cand2==nums[i]:
            count2+=1
    res=[]
    if count1>n//3 and cand1 is not None:
        res.append(cand1)
    if count2>n//3 and cand2 is not None:
        res.append(cand2)
    return res

nums=input("Enter array: ").split()
nums = list(map(int,nums))
print("Brute:  ", brute(nums))
print("Optimal:", optimal(nums))
