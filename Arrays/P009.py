def optimal(arr):
    count=max_count=0
    n=len(arr)
    for i in range(n):
        if arr[i]==1:
            count+=1
        else:
            max_count=max(max_count,count)
            count=0
    max_count=max(max_count,count)
    return max_count

if __name__=='__main__':
    arr=input("Enter array: ").split()
    arr=list(map(int,arr))
    print('Max= ',optimal(arr))