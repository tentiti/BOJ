import sys
from collections import deque
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
mapArr = []

for i in range(n):
    mapArr.append(list(map(int, input())))

# print(mapArr)

minDist = n*m+1
visited = [[[0,0] for i in range(m)] for j in range(n)]
# def dfs(y, x, alreadyBroke, dist):  # dfs 
#     # print(y, x, alreadyBroke, dist)
#     global minDist
#     if y == n-1 and x == m-1:
#         # print('reached', y, x)
#         minDist = min(dist, minDist)
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if not(0<=ny<n and 0<=nx<m): continue
#         if visited[ny][nx]: continue
#         if mapArr[ny][nx] == 0:
#             visited[ny][nx] = 1
#             bfs(ny, nx, False, dist+1)
#         elif alreadyBroke:
#             continue
#         else:
#             visited[ny][nx] = 1
#             bfs(ny, nx, True, dist+1)

def bfs(yPos, xPos):
    queue = deque()
    queue.append([yPos, xPos, 0])
    visited[yPos][xPos][0] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        y, x, used = queue.popleft()
        
        #도착했다면, 내 값 내보내기
        if (y, x) == (n-1, m-1):
            return visited[y][x][used]
        
        #갈 수 있는 지점
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            #범위 제한
            if not(0<=ny<n and 0<=nx<m): continue
            
            #갈 수 있는 곳이고, 가본 적 없는 경로라면
            if mapArr[ny][nx] == 0 and visited[ny][nx][used] == 0:
                 visited[ny][nx][used] = visited[y][x][used] + 1
                 queue.append([ny, nx, used])
            
            #벽을 만났고, 아직 안부쉈다면    
            if mapArr[ny][nx] == 1 and not used:
                #이곳에 부숴서 가는 경로는 이 칸에서 부숴서 가면 됨.
                 visited[ny][nx][1] = visited[y][x][0] + 1
                 queue.append([ny, nx, 1])
    
    return -1
    
print(bfs(0,0))

# visited[0][0] = True
# dfs(0, 0, False, 0)
# print('-1' if minDist == m*n+1 else minDist-1)