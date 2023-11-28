import sys
input = sys.stdin.readline

from collections import deque

width, height, floor = map(int, input().split())

groundArr = []
queue = deque()
visited = [[[-1 for i in range(width)] for j in range(height)] for k in range(floor)]


def bfs():
    global queue
    while queue:
        (tz, ty, tx) = queue.popleft()
        dx = [0, 0, 1, -1, 0, 0]
        dy = [1, -1, 0, 0, 0, 0]
        dz = [0, 0, 0, 0, 1, -1]
        for i in range(6):
            ny = ty + dy[i]
            nx = tx + dx[i]
            nz = tz + dz[i]
            # print(ny, nx)
            if ny<0 or nx<0 or nx>=width or ny >= height or nz < 0 or nz >= floor:
                continue
            if groundArr[nz][ny][nx] == -1:
                continue
            if visited[nz][ny][nx] == -1 and groundArr[nz][ny][nx] == 0:  
                visited[nz][ny][nx] = 1
                groundArr[nz][ny][nx] = groundArr[tz][ty][tx] + 1
                queue.append((nz, ny, nx))
for i in range(floor):
    thisFloor = []
    for i in range(height):
        thisFloor.append(list(map(int, input().split())))
    groundArr.append(thisFloor)
    
for k in range(floor):   
    for i in range(height):
        for j in range(width):
            if groundArr[k][i][j] == 1:
                queue.append((k, i, j))
                visited[k][i][j] = 1

bfs()

ans = 0
for k in range(floor):   
    for i in range(height):
        for j in range(width):
            if groundArr[k][i][j] == 0:
                print(-1)
                exit(0)
            if groundArr[k][i][j] > ans:
                ans = groundArr[k][i][j]
print(ans-1)