import sys
from collections import deque
sys.setrecursionlimit(10**4)

nMap = []

r, c = map(int, input().split())

for i in range(r):
    nMap.append(list(input()))

# visitList = deque()
# visitList = []
# visitList.append(nMap[0][0])
visitList = [0 for i in range(26)]
visitList[ord(nMap[0][0])-65] = 1
# maxTraverse = 1
maxCounter = 0

def dfs(y, x, maxTraverse):
    global maxCounter
    maxCounter = max(maxCounter, maxTraverse)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not (0<=nx<c and 0<=ny<r): continue
        if visitList[ord(nMap[ny][nx])-65]: continue
        visitList[ord(nMap[ny][nx])-65] = 1
        dfs(ny, nx, maxTraverse+1)
        visitList[ord(nMap[ny][nx])-65] = 0

dfs(0, 0, 1)
print(maxCounter)