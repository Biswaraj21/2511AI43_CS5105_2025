def brute(startWord,targetWord,wordList):
    wordSet=set(wordList)
    minStep=[float('inf')]
    def diff_by_oneword(w1,w2):
        diff=0
        for i in range(len(w1)):
            if w1[i]!=w2[i]:
                diff+=1
            if diff>1:
                return False
        return diff==1
    def dfs(word,step,visited):
        if word==targetWord:
            minStep[0]=min(minStep[0],step)
            return
        for next in wordList:
            if diff_by_oneword(next,word) and next not in visited:
                visited.add(next)
                dfs(next,step+1,visited)
                visited.remove(next)
    dfs(startWord,1,set([startWord]))
    return minStep[0] if minStep[0]!=float('inf') else 0

from collections import deque
def optimal(startword,targetword,wordList):
    wordSet=set(wordList)
    q=deque([(startword,1)])
    while q:
        word,step=q.popleft()
        if word==targetword:
            return step
        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                newWord=word[:i]+ch+word[i+1:]
                if newWord in wordSet:
                    q.append((newWord,step+1))
                    wordSet.remove(newWord)
    return 0

startWord = "hit"
targetWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print("Brute", brute(startWord, targetWord, wordList))
print("Optimal :", optimal(startWord, targetWord, wordList))