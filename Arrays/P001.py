def brute(arr):
    n=len(arr)
    for i in range(n):
        c=0
        for j in range(n):
            if arr[j]>arr[i]:
                c=1
                break
        if c==0:
            return arr[i]
    return -1

def optimal(arr):
    n=len(arr)
    max_ele=arr[0]
    for i in range(1,n):
        if arr[i]>max_ele:
            max_ele=arr[i]
    return max_ele

if __name__=='__main__':
    arr=input('Enter elements')
    arr=arr.split()
    print('Brute: ',brute(arr))
    print('Optimal: ',optimal(arr))