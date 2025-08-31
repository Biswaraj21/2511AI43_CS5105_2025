def isSafe(node,c,color,adj):
    for nei in adj[node]:
        if color[nei]==c:
            return False
    return True

def brute(node,color,adj,V):
    if node==V:
        return True
    for c in [0,1]:
        if isSafe(node,c,color,adj):
            color[node]=c
            if brute(node+1,color,adj,V):
                return True
            color[node]=-1
    return False

def dfs(node,c,color,adj):
    color[node]=c
    for nei in adj[node]:
        if color[nei]==-1:
            if not dfs(nei,1-c,color,adj):
                return False
        elif color[nei]==c:
            return False
    return True

def optimal(adj,V):
    color=[-1]*V
    for i in range(V):
        if color[i]==-1:
            if not dfs(i,0,color,adj):
                return False
    return True

if __name__=="__main__":
    V = 4
    adj = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }
    color=[-1]*V
    print("Brute: ",brute(0,color,adj,V))
    print("Optimal: ",optimal(adj,V))