def brute(sr,sc,image,newColor):
    original=image[sr][sc]
    row,col=len(image),len(image[0])
    if original==newColor:
        return image
    def dfs(r,c):
        image[r][c]=newColor
        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr,nc=dr+r,dc+c
            if 0<=nr<row and 0<=nc<col and image[nr][nc]==original:
                dfs(nr,nc)
    dfs(sr,sc)
    return image

import heapq
def optimal(sr,sc,image,newColor):
    original=image[sr][sc]
    row,col=len(image),len(image[0])
    if original==newColor:
        return image
    pq=[(sr,sc)]
    image[sr][sc]=newColor
    while pq:
        r,c=heapq.heappop(pq)
        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr,nc=dr+r,dc+c
            if 0<=nr<row and 0<=nc<col:
                if image[nr][nc]==original:
                    image[nr][nc]=newColor
                    heapq.heappush(pq,(nr,nc))
    return image

if __name__=="__main__":
    image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
    ]
    sr, sc = 1, 1 
    newColor = 2
    image1=brute(sr,sc,image,newColor)
    image2=optimal(sr,sc,image,newColor)
    print("Brute: \n")
    for row in image1:
        print(row)
    print("\nOptimal: \n")
    for row in image2:
        print(row)