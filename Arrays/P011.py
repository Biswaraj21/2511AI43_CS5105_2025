def brute(arr):
    n=len(arr)
    max_sum=0
    for i in range(n-1):
        curr_sum=0
        for j in range(i,n):
            curr_sum+=arr[j]
            max_sum=max(max_sum,curr_sum)
    return max_sum

def optimal(arr):
    n=len(arr)
    max_sum=curr_sum=0
    for i in range(n):
        if curr_sum<0:
            curr_sum=0
        curr_sum+=arr[i]
        max_sum=max(max_sum,curr_sum)
    return max_sum

if __name__=='__main__':
    arr=input('Enter array: ').split()
    arr=list(map(int,arr))
    print('Brute: ',brute(arr))
    print('Optimal: ',optimal(arr))