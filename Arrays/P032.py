def optimal(nums):
    nums.sort(key=lambda x:x[0])
    merge=[]
    for interval in nums:
        if not merge or merge[-1][1]<interval[0]:
            merge.append(interval)
        else:
            merge[-1][0]=min(merge[-1][0],interval[0])
            merge[-1][1]=min(merge[-1][1],interval[1])
    return merge

intervals = [[1,3],[2,6],[8,10],[15,18]]
print("Optimal: ",optimal(intervals))