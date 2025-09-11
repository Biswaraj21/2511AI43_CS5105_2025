def optimal(nums1,nums2):
    n1,n2=len(nums1),len(nums2)
    i=j=0
    res=[]
    while(i<n1 and j<n2):
        if nums1[i]<nums2[j]:
            res.append(nums1[i])
            i+=1
        elif nums2[j]<nums1[i]:
            res.append(nums2[j])
            j+=1
        else:
            res.append(nums1[i])
            i+=1
            j+=1
    while(i<n1):
        res.append(nums1[i])
        i+=1
    while(j<n2):
        res.append(nums2[j])
        j+=1
    return res

if __name__=='__main__':
    nums1=input('Enter first nums: ').split()
    nums1=list(map(int,nums1))
    nums2=input('Enter second nums: ').split()
    nums2=list(map(int,nums2))
    print('Merges: ',optimal(nums1,nums2))