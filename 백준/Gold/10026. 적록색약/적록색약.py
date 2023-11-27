import sys
sys.setrecursionlimit(10**8)

#적록색약이 본 구역
rgBlind = 0

#적록색약이 아닌 사람이 본 구역
rgNotBlind = 0

blindList = []
notBlindList = []

n = int(input())
arr = [['a' for i in range(n)] for i in range(n)]
blindArr = [[1 for i in range(n)] for i in range(n)]
notBlindArr = [[1 for i in range(n)] for i in range(n)]

def dfs(i, j, blind):
    global blindList, notBlindList, blindArr, notBlindArr
    if blind and blindArr[i][j] == 1: #새로 보는 칸이
        blindArr[i][j] = -1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx >= n or ny >= n or nx<0 or ny<0:
                continue
            if (arr[nx][ny] in ['R', 'G'] and arr[i][j] in ['R', 'G']) or (arr[nx][ny] == 'B' and arr[i][j] =='B'):
                dfs(nx, ny, True)
            
    elif not blind and notBlindArr[i][j] == 1: #R과 G를 다르게 판단
        notBlindArr[i][j] = -1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx >= n or ny >= n or nx<0 or ny<0:
                continue
            if arr[nx][ny] == arr[i][j]:
                dfs(nx, ny, False)
             
for i in range(n):
    msg = input()
    for j in range(n):
        arr[i][j] = msg[j]
        
for i in range(n):
    for j in range(n):
        if notBlindArr[i][j] == 1:
            dfs(i, j, False)
            rgNotBlind += 1

for i in range(n):
    for j in range(n):
        if blindArr[i][j] == 1:
            dfs(i, j, True)
            rgBlind += 1





print(rgNotBlind, rgBlind)
# print(arr)