import sys
sys.setrecursionlimit(10**6)

mapSize = int(input())
aptMap = []

for i in range(mapSize):
    aptMap.append(list(map(int, input())))

danjis = []
visited = [[0 for i in range(mapSize)] for j in range(mapSize)]

def dfs(i, j, danjiCount):
    aptMap[i][j] = danjiCount
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for k in range(4):
        ny = i + dy[k]
        nx = j + dx[k]
        if not (0<=nx<mapSize and 0<=ny<mapSize): continue
        if aptMap[ny][nx] == 0: continue
        if not visited[ny][nx]:
            visited[ny][nx] = 1
            danjis[danjiCount-1] += 1
            dfs(ny, nx, danjiCount)
        
danjiCount = 0
danji = []
for i in range(mapSize):
    for j in range(mapSize):
        if aptMap[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                danjiCount += 1
                danjis.append(1)
                dfs(i, j, danjiCount)
                
# for i in aptMap:
#     print(i)
# print(danjis)
print(danjiCount)
danjis.sort()
for _ in danjis:
    print(_)

        