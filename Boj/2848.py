import sys
from collections import deque

Input = sys.stdin.readline
wordNum = int(Input())

index = 0
word ={}
wordList =[]

cnt = 0
for i in range(wordNum):
    wordStr = Input()
    wordList.append(wordStr)

    for j in range(len(wordStr)-2):
        if not (wordStr[j] in word):
            word[wordStr[j]] = index
            index += 1
            cnt += 1
        if not (wordStr[j + 1] in word):
            word[wordStr[j + 1]] = index
            index += 1
            cnt += 1

graph = [[] for _ in range(cnt)]
inDegree = [0]*cnt
#글자들을 등록한다.
for i in wordList:
    for j in range(len(i)-2):
        inDegree[word[i[j+1]]] += 1
        graph[word[i[j]]].append(i[j + 1])

print(inDegree)
def topology_soty():
    result = []
    q = deque()

    for i in range(1,len(graph)):
        if not inDegree[i]:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(word[now])

        for i in graph[now]:
            inDegree[i] -= 1
            if not inDegree:
                q.append(i)

    print(result)

topology_soty()