import sys
from collections import deque

words = ["xwt","xwf","aw","att","wftt"]
def LanguageOrder(words):
    index = 0
    word ={}
    wordList2 = []
    for i in words:
        wordList2.append(i)

    cnt = 0
    wordSequence = []

    isWord =[]
    isWordCnt = 0
    for i in range(len(wordList2)):
        for j in range(len(wordList2[i])):
            if not(wordList2[i][j]) in isWord:
                isWord.append(wordList2[i][j])
                isWordCnt+=1

    for i in range(len(wordList2)-1):
        for j in range(len(wordList2[i])):
            if wordList2[i][j] == wordList2[i+1][j]:
                continue
            else:
                if wordList2[i+1][j] == '\n' or wordList2[i][j] == '\n':
                    break
                if not (wordList2[i][j] in word):
                    word[wordList2[i][j]] = index
                    index += 1
                    cnt += 1
                if not (wordList2[i+1][j] in word):
                    word[wordList2[i+1][j]] = index
                    index += 1
                    cnt += 1
                if not ([wordList2[i][j], wordList2[i + 1][j]] in wordSequence):
                    wordSequence.append([wordList2[i][j], wordList2[i + 1][j]])
                break




    graph = [[] for _ in range(cnt)]
    inDegree = [0]*cnt
    #글자들을 등록한다.
    for i in wordSequence:
        inDegree[word[i[1]]] += 1


    result = []
    q = deque()

    for i in range(len(inDegree)):
        if not inDegree[i]:
            q.append(i)

    while q:
        now = q.popleft()
        w = {v:k for k,v in word.items()}
        nw = w.get(now)
        result.append(nw)

        for i in wordSequence:
            if i[0] == nw:

                inDegree[word[i[1]]] -= 1
                if not inDegree[word[i[1]]]:
                    q.append(word[i[1]])

    isRight = True
    for i in inDegree:
        if i != 0:
            isRight = False
    if not isRight:
        return ""
    else:
        if len(result) < isWordCnt-1:
            for i in isWord:
                if i != '\n' and not (i in result):

                    result.append(i)
        ans = ''.join(result)
        return ans
print(LanguageOrder(words))