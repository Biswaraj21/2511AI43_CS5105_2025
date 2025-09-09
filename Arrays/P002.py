def brute(arr):
    n=len(arr)
    for i in range(n):
        c=0
        for j in range(n):
            if arr[j]>arr[i]:
                c=1
                break
        if c==0:
            max1=arr[i]
            break
    for i in range(n):
        if arr[i]==max1:
            continue
        c=0
        for j in range(n):
            if arr[j]==max1:
                continue
            if arr[j]>arr[i]:
                c=1
                break
        if c==0:
            max2=arr[i]
            break
    return max2

def optimal(arr):
    n=len(arr)
    if n<2:
        return -1
    if arr[0]>arr[1]:
        max1,max2=arr[0],arr[1]
    else:
        max1,max2=arr[1],arr[0]
    for i in range(2,n):
        if arr[i]>max1:
            max2=max1
            max1=arr[i]
        elif arr[i]>max2:
            max2=arr[i]
    return max2

if __name__=='__main__':
    arr=input("Enter array")
    arr=arr.split()
    print("Brute: ",brute(arr))
    print('Optimal: ',optimal(arr))