from itertools import permutations
def is_valid_order(order,words):
    pos = {ch:i for i,ch in enumerate(order)}
    for i in range(len(words)-1):
        w1,w2=words[i],words[i+1]
        for j in range(min(len(w1),len(w2))):
            if w1[j]!=w2[j]:
                if pos[w1[j]]>pos[w2[j]]:
                    return False
                break
        else:
            if len(w1) > len(w2):
                return False
    return True
def brute(words, k):
    chars = set("".join(words))
    for perm in permutations(chars, len(chars)):
        if is_valid_order(perm, words):
            return "".join(perm)
    return ""

from collections import defaultdict,deque
def optimal(dict,K):
    adj=defaultdict(set)
    indegree={chr(ord("a")+i):0 for i in range(K)}
    for i in range(len(dict)-1):
        w1,w2=dict[i],dict[i+1]
        for j in range(min(len(w1),len(w2))):
            if w1[j]!=w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    indegree[w2[j]]+=1
                break
        else:
            if len(w2)>len(w1):
                return ""
    q=deque([ch for ch in indegree if indegree[ch]==0])
    order=[]
    while q:
        ch=q.popleft()
        order.append(ch)
        for nei in adj[ch]:
            indegree[nei]-=1
            if indegree[nei]==0:
                q.append(nei)
    if len(order)<len(indegree):
        return ""
    return "".join(order)

N = 5
K = 4
dict = ["baa","abcd","abca","cab","cad"]
print("Brute: ",brute(dict,K))
print("Optimal: ",optimal(dict,K))