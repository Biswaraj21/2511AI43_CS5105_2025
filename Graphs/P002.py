from collections import deque

def brute(V,adj):
    visited=[False]*(V+1)
    count=0
    for i in range(1,V+1):
        if visited[i]==False:
            q=deque([i])
            visited[i]=True
            while q:
                level_size=len(q)
                for _ in range(level_size):
                    node=q.popleft()
                    for child in adj[node]:
                        if visited[child]==False:
                            visited[child]=True
                            q.append(child)
            count+=1
    return count

def optimal(V,adj):
    visited=[False]*(V+1)
    count=0
    for i in range(1,V+1):
        if visited[i]==False:
            q=deque([i])
            visited[i]=True
            while q:
                node=q.popleft()
                for child in adj[node]:
                    if visited[child]==False:
                        visited[child]=True
                        q.append(child)
            count+=1
    return count

if __name__=="__main__":
    V=8
    adj={1:[2],
         2:[1,3],
         3:[2],
         4:[5],
         5:[4,6],
         6:[5],
         7:[8],
         8:[7]}
    print("Brute force:",brute(V,adj))
    print("Optimal: ",optimal(V,adj))