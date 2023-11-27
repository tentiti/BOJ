n, m = map(int, input().split())

mapArr = []

def bfs(x, y):
    queue = []
    queue.append((x, y))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
            
    while queue:
        temp = queue.pop(0)
        tempX = temp[0]
        tempY = temp[1]
        for i in range(4):
            nx = tempX + dx[i]
            ny = tempY + dy[i]
            if nx<0 or ny <0 or nx >=m or ny >= n or mapArr[ny][nx]==0:
                continue
            elif mapArr[ny][nx] == 1:
                mapArr[ny][nx] = int(mapArr[tempY][tempX]) + 1
                queue.append((nx, ny))
    
    return mapArr[n-1][m-1]

for i in range(n):
    mapArr.append(list(map(int, input())))

print(bfs(0,0))

