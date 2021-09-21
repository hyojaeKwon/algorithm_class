import sys
from collections import deque
Input = sys.stdin.readline

dx = [0 , 0, 1, -1]
dy = [1 , -1, 0, 0]

def searching(k):
    queue = deque()
    queue.append((0,0))
    cheese[0][0] = k + 1
    #현재 턴에서 없어지는 치즈 개수 세기
    cheeseCount = 0
    while queue:
        (y,x) = queue.popleft()

        #bfs
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #치즈 전체 가능 범위
            if nx >= 0 and nx < m and ny >= 0  and ny < n and cheese[ny][nx] <= k:

                #치즈가 있고(True), 방문하지 않은 곳
                if cheese[ny][nx] == 1:
                    #방문처리 와 치즈 녹음처리
                    cheese[ny][nx] = k+1
                    #치즈 개수 추가
                    cheeseCount += 1

                #치즈가 없고(False), 방문하지 않은 곳
                elif cheese[ny][nx] != 1:
                    #방문 처리
                    cheese[ny][nx] = k+1
                    #Bfs 계속 진행
                    queue.append((ny,nx))
    #현재 턴에서 사라진 치즈 개수 반환
    return cheeseCount


#가로 세로 입력
n, m = map(int,Input().split())
#치즈 입력
cheese = [list(map(int,Input().split())) for _ in range(n)]
lastCheeseCount = 0
time = 3
while True:

    nowCheeseCount = searching(time)
    if not nowCheeseCount:
        print(time-3)
        print(lastCheeseCount)
        break
    else:
        lastCheeseCount = nowCheeseCount
    time += 1
