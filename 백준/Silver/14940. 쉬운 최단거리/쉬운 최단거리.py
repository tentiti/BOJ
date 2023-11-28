import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

height, width = map(int, input().split())
mapArr = []
visited = [[-1 for i in range(width)] for j in range(height)]
start_y, start_x = -1, -1
mapQueue = deque()

def bfs():
    global mapQueue
    while mapQueue:
        y, x = mapQueue.popleft()
        # visited[y][x] = 1
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0<=ny<height and 0<=nx<width):
                if mapArr[ny][nx] == 0:
                    continue
                elif visited[ny][nx] == -1:
                    visited[ny][nx] = 1
                    mapArr[ny][nx] = mapArr[y][x] + 1
                    mapQueue.append((ny, nx))

for i in range(height):
    mapArr.append(list(map(int, input().split())))
    for j in range(width):
        if mapArr[i][j] == 2:
            start_y = i
            start_x = j

mapQueue.append((start_y, start_x))
mapArr[start_y][start_x] = 0
# visited[start_y][start_x] = 1
bfs()
# print(mapArr)
for i in range(height):
    for j in range(width):
        if visited[i][j] == -1 and mapArr[i][j] != 0:
            mapArr[i][j] = -1
    print(*mapArr[i], sep=' ')
