def brute(arr):
    n=len(arr)
    for i in range(n+1):
        c=0
        for j in range(n):
            if arr[j]==i:
                c=1
        if c==0:
            return i
    return -1

def optimal(arr):
    n=len(arr)
    tot=n*(n+1)//2
    suma=0
    for i in range(n):
        suma+=arr[i]
    return tot-suma

if __name__=='__main__':
    arr=input("Enter array").split()
    nums=list(map(int,arr))
    print("Brute: ",brute(nums))
    print('Optimal: ',optimal(nums))