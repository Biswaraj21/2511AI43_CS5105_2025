c=0
def mergesort(nums,l,h):
    if (l<h):
        mid=(l+h)//2
        mergesort(nums,l,mid)
        mergesort(nums,mid+1,h)
        merge(nums,l,mid,h)

def merge(nums,l,mid,h):
    global c
    n1,n2=mid-l+1,h-mid
    arr1=[]
    arr2=[]
    for i in range(l,mid+1):
        arr1.append(nums[i])
    for i in range(mid+1,h+1):
        arr2.append(nums[i])
    i, j = 0, 0
    while i < n1 and j < n2:
        if arr1[i] > 2 * arr2[j]:
            c += (n1 - i)
            j += 1
        else:
            i += 1
    i,j=0,0
    k=l
    while(i<n1 and j<n2):
        if arr1[i]<=arr2[j]:
            nums[k]=arr1[i]
            i+=1
        else:
            nums[k]=arr2[j]
            j+=1
        k+=1
    while(i<n1):
        nums[k]=arr1[i]
        i+=1
        k+=1
    while(j<n2):
        nums[k]=arr2[j]
        j+=1
        k+=1

nums = [6,4,1,2,7]
mergesort(nums,0,4)
#print("Brute:", brute(nums))   # 3 inversions -> (2,1), (4,1), (4,3)
print("Optimal: ", c)