from collections import deque

def BruteForce(V,adj,start):
    res=[]
    q=deque([start])
    visited=[False]*(V+1)
    visited[start]=True
    while q:
        levelsize=len(q)
        for _ in range(levelsize):
            node=q.popleft()
            res.append(node)
            for child in adj[node]:
                if visited[child]==False:
                    visited[child]=True
                    q.append(child)
    return res    

def OptimalApproach(V,adj,start):
    res=[]
    q=deque([start])
    visited=[False]*(V+1)
    visited[start]=True
    while q:
        node=q.popleft()
        res.append(node)
        for child in adj[node]:
            if visited[child]==False:
                q.append(child)
                visited[child]=True
    return res

if __name__=='__main__':
    adj={1:[2,5],
         2:[1,5,3],
         3:[2,4,5],
         4:[3,5],
         5:[1,2,4]}
    V=5
    print("By Brute Force: ",BruteForce(V,adj,1))
    print("Optimal Approach: ",OptimalApproach(V,adj,1))