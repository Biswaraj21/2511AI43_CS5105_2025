def brute(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                return False
    return True

def optimal(arr):
    n=len(arr)
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
    return True

if __name__=='__main__':
    arr=input('Enter elements: ')
    arr=arr.split()
    print('Brute: ',brute(arr))
    print('Optimal: ',optimal(arr))