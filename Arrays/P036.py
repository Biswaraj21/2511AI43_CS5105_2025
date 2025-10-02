def optimal(nums):
    n=len(nums)
    s1=n*(n+1)//2
    q1=n*(n+1)*(2*n+1)//6
    s=sum(nums)
    q=sum(x*x for x in nums)
    d1=s-s1
    d2=q-q1
    d=d2//d1
    A=(d1+d)//2
    B=A-d1
    return [A,B]

nums = [1, 2, 2, 4]
print(optimal(nums))