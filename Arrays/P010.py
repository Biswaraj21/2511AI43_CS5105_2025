def brute(arr):
    n=len(arr)
    count=0
    for i in range(n):
        count=0
        for j in range(n):
            if arr[i]==arr[j]:
                count+=1
        if count>=n//2:
            return arr[i]
        
def optimal(arr):
    n=len(arr)
    ele=count=0
    for i in range(n):
        if count==0:
            ele=arr[i]
        elif ele==arr[i]:
            count+=1
        else:
            count-=1
    return ele

if __name__=='__main__':
    arr=input('Enter array: ').split()
    arr=list(map(int,arr))
    print('Brute: ',brute(arr))
    print('Optimal: ',optimal(arr))