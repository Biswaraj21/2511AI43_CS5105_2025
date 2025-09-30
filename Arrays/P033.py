def merge(nums1,nums2):
    n1,n2=len(nums1),len(nums2)
    res=[]
    i=j=0
    while(i<n1 and j<n2):
        if nums1[i]>nums2[j]:
            res.append(nums2[j])
            j+=1
        else:
            res.append(nums1[i])
            i+=1
    while(i<n1):
        res.append(nums1[i])
        i+=1
    while(j<n2):
        res.append(nums2[j])
        j+=1
    return res

nums1 = [1,2,3]
m = 3
nums2 = [2,5,6]
n = 3
res=merge(nums1,nums2)
print(res)