import sys
sys.setrecursionlimit(10**6)

n ,m= map(int, input().split())
map = []
visited = [[-1] * m for i in range(n)]

me_x = -1
me_y = -1
me_met = 0

def dfs(x, y):
    global me_met
    # print(x, y)
    if map[y][x] == "P":
        me_met += 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=m or ny>=n or map[ny][nx] == "X":
            continue
        if visited[ny][nx] == 1:
            continue
        else:
            visited[ny][nx] = 1
            dfs(nx, ny)

for i in range(n):
    temp = sys.stdin.readline()
    map.append(temp)
    # print(temp)
    for j in range(m):
        # map[i][j] = temp[j]
        if temp[j] == 'I':
            me_x = j
            me_y = i

# print(map)
# print(len(map))
dfs(me_x, me_y)

if me_met:
    print(me_met)
else:
    print('TT')