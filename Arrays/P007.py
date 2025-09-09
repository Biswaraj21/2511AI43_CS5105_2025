def linear(arr,target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return i
    return -1

if __name__=='__main__':
    arr=input('Enter elements: ').split()
    target=int(input("Enter target: "))
    nums=list(map(int,arr))
    print(linear(nums,target))