import sys
Input = sys.stdin.readline
sys.setrecursionlimit(10**6)

from collections import deque


#m이 높이, n이 가로 길이
m,n =  map(int,Input().split())
heightMap = [list(map(int,Input().split())) for _ in range(m)]


#dp Table 생성
dp = [[-1] * n for _ in range(m)]
# dp[0][0] =
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):

    if y == m-1 and x == n-1:
        return 1
    #방문한 노드 처리
    if dp[y][x] != -1:
        return dp[y][x]

    #방문하지 않은 노드 방문 처리
    dp[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < m and heightMap[ny][nx] < heightMap[y][x]:
            dp[y][x] += dfs(nx,ny)

    return dp[y][x]

print(dfs(0,0))


