def brute(arr):
    s=set()
    n=len(arr)
    k=0
    for i in range(n):
        if arr[i] not in s:
            s.add(arr[i])
            k+=1
    sl=list(s)
    sl.sort()
    for i in range(k):
        arr[i]=sl[i]
    return arr

def optimal(arr):
    n=len(arr)
    i=0
    for j in range(1,n):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return arr

if __name__=='__main__':
    arr=input('Enter elements: ').split()
    print('Brute: ',brute(arr))
    print('Optimal: ',optimal(arr))