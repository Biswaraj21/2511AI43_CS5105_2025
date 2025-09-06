def brute(intervals):
    n=len(intervals)
    merged=[False]*n
    res=[]
    for i in range(n):
        curr_start,curr_end=intervals[i][0],intervals[i][1]
        if merged[i]:
            continue
        for j in range(i+1,n):
            s,e=intervals[j][0],intervals[j][1]
            if not (s>curr_end or e<curr_start):
                curr_start=min(curr_start,s)
                curr_end=max(curr_end,e)
                merged[j]=True
        res.append((curr_start,curr_end))
    return res

def optimal(intervals):
    res=[]
    intervals.sort(key=lambda x:x[0])
    res.append(intervals[0])
    for start,end in intervals[1:]:
        if start<res[-1][1]:
            res[-1][1]=max(end,res[-1][1])
        else:
            res.append([start,end])
    return res


if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]

    print("Brute :",brute(intervals))
    print("Optimal :",optimal(intervals))