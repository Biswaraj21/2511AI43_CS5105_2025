def brute(nums):
    n=len(nums)
    pos,neg=[],[]
    for x in nums:
        if x>0:
            pos.append(x)
        else:
            neg.append(x)
    p=no=0
    for i in range(n):
        if i%2!=0:
            nums[i]=neg[no]
            no+=1
        else:
            nums[i]=pos[p]
            p+=1
    return nums

def optimal(nums):
    n=len(nums)
    res=[0]*n
    p,neg=0,1
    for n in nums:
        if n>0:
            res[p]=n
            p+=2
        else:
            res[neg]=n
            neg+=2
    return res

if __name__=='__main__':
    nums=input("Enter array: ").split()
    nums=list(map(int,nums))
    print("Brute: ",brute(nums))
    print("Optimal: ",optimal(nums))