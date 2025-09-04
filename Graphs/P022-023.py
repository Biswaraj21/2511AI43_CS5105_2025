from itertools import permutations
def is_valid_order(order, edges, pos):
    for u, v in edges:
        if pos[u] > pos[v]: 
            return False
    return True

def Brute(V, edges):
    vertices = list(range(V))
    for perm in permutations(vertices):
        pos = {perm[i]: i for i in range(V)}

        if is_valid_order(perm, edges, pos):
            return perm 
    return None 

from collections import deque
def optimal(V,edge):
    indegree=[0]*V
    adj=[[] for _ in range(V)]
    for u,v in edge:
        adj[u].append(v)
        indegree[v]+=1
    q=deque()
    for i in range(V):
        if indegree[i]==0:
            q.append(i)
    res=[]
    while q:
        node=q.popleft()
        res.append(node)
        for nei in adj[node]:
            indegree[nei]-=1
            if indegree[nei]==0:
                q.append(nei)
    return (res)


V = 4
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
print("Brute :", Brute(V, edges))
print("Optimal: ",optimal(V,edges))