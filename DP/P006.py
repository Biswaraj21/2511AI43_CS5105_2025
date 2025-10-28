def brute_ninja(day,last,point):
    if day==0:
        maxi=0
        for i in range(3):
            if i!=last:
                maxi=max(maxi,point[0][i])
        return maxi
    maxi=0
    for i in range(3):
        if i!=last:
            maxi=max(maxi,point[day][i]+brute_ninja(day-1,i,point))
    return maxi

def brute(point):
    n=len(point)
    return brute_ninja(n-1,3,point)

def optimal(point):
    n=len(point)
    prev=[0]*4
    for last in range(4):
        prev[last]=max(point[0][i] for i in range(3) if i!=last)
    for i in range(1,n):
        curr=[0]*4
        for last in range(4):
            curr[last]=max(prev[task]+point[i][task] for task in range(3) if task!=last)
        prev=curr[:]
    return prev[-1]

points = [
    [1, 2, 5],
    [3, 1, 1],
    [3, 3, 3]
]
print("Bruute: ",brute(points))
print("Optimal: ", optimal(points))