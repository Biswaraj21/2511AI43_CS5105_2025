from itertools import permutations
def is_valid_order(order, edges, pos):
    for u, v in edges:
        if pos[v] > pos[u]: 
            return False
    return True

def Brute(N,P,array):
    vertices = list(range(N))
    for perm in permutations(vertices):
        pos = {perm[i]: i for i in range(N)}

        if is_valid_order(perm, array, pos):
            return True 
    return False

from collections import deque
def optimal(N,P,array):
    indegree=[0]*N
    adj=[[] for _ in range(N)]
    for u,v in array:
        adj[v].append(u)
        indegree[u]+=1
    q=deque()
    for i in range(N):
        if indegree[i]==0:
            q.append(i)
    res=[]
    count=0
    while q:
        node=q.popleft()
        count+=1
        res.append(node)
        for nei in adj[node]:
            indegree[nei]-=1
            if indegree[nei]==0:
                q.append(nei)
    return count==N

if __name__=='__main__':
    N = 4
    P = 3
    array=[(1,0),(2,1),(3,2)]
    print("Brute: ",Brute(N,P,array))
    print("Optimal: ",optimal(N,P,array))