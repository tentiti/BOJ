import sys
input = sys.stdin.readline

from collections import deque

width, height = map(int, input().split())

groundArr = []
queue = deque()
visited = [[-1 for i in range(width)] for j in range(height)]


def bfs():
    global queue
    while queue:
        (ty, tx) = queue.popleft()
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            # print(ny, nx)
            if ny<0 or nx<0 or nx>=width or ny >= height:
                continue
            if groundArr[ny][nx] == -1:
                continue
            if visited[ny][nx] == -1 and groundArr[ny][nx] == 0:  
                visited[ny][nx] = 1
                groundArr[ny][nx] = groundArr[ty][tx] + 1
                queue.append((ny, nx))

for i in range(height):
    groundArr.append(list(map(int, input().split())))
    
start_y, start_x = -1, -1
for i in range(height):
    for j in range(width):
        if groundArr[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 1

bfs()
# print(groundArr)
ans = 0
for j in range(height):
    for i in range(width):
        if groundArr[j][i] == 0:
            print(-1)
            exit(0)
        if groundArr[j][i] > ans:
            ans = groundArr[j][i]
print(ans-1)