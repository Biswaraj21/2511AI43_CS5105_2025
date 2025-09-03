def brute(startWord,targetWord,wordList):
    wordSet=set(wordList)
    minStep=[float('inf')]
    minList=[]
    def diff_by_oneword(w1,w2):
        diff=0
        for i in range(len(w1)):
            if w1[i]!=w2[i]:
                diff+=1
            if diff>1:
                return False
        return diff==1
    def dfs(word,step,visited,path):
        if word==targetWord:
            if step<minStep[0]:
                minStep[0]=step
                minList.clear()
                minList.append(path[:])
            elif step==minStep[0]:
                minList.append(path[:])
            return
        for next in wordList:
            if diff_by_oneword(next,word) and next not in visited:
                visited.add(next)
                path.append(next)
                dfs(next,step+1,visited,path)
                visited.remove(next)
                path.pop()
    dfs(startWord,1,set([startWord]),[startWord])
    return minList

from collections import deque, defaultdict

def optimal(startWord, targetWord, wordList):
    wordSet = set(wordList)
    if targetWord not in wordSet:
        return []
    q = deque([startWord])
    parents = defaultdict(list)
    visited = set([startWord])
    found = False
    while q and not found:
        next_level = set()
        for _ in range(len(q)):
            word = q.popleft()
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i+1:]
                    if newWord in wordSet and newWord not in visited:
                        parents[newWord].append(word)
                        if newWord == targetWord:
                            found = True
                        next_level.add(newWord)
        q.extend(next_level)
        visited |= next_level
    res = []
    def backtrack(word, path):
        if word == startWord:
            res.append(path[::-1])
            return
        for p in parents[word]:
            backtrack(p, path + [p])
    if found:
        backtrack(targetWord, [targetWord])
    return res

startWord = "hit"
targetWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print("Brute: \n") 
res1 = brute(startWord, targetWord, wordList)
for row in res1:
    print('->'.join(row))
print("\nOptimal: \n") 
res2 = optimal(startWord, targetWord, wordList)
for row in res2:
    print('->'.join(row))