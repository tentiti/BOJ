import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

testCase = int(input())
tempScore = (10**9)   
maxScore = 0 

# def dfs(y, x):
#     global tempScore, visited, maxScore
#     # print(y, x, tempScore)
#     # visited[y][x] = 1
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     for i in range(2):
#         for j in range(size):
#             if not visited[i][j]:
#                 for k in range(4):
#                     ny = i + dy[k]
#                     nx = j + dx[k]
#                     if not 0<=ny<2 or not 0<=nx<size: continue
#                     visited[ny][nx] = 1 #cannot use
#                 tempScore += stickerArr[i][j]
#                 maxScore = max(maxScore, tempScore)
#                 visited[i][j] = 1
#                 dfs(i, j)

for i in range(testCase):
    size = int(input())
    stickerArr = []
    for j in range(2):
        stickers = list(map(int, input().split()))
        stickerArr.append(stickers)
    # print(stickerArr)
    # visited = [[0] * (size)] * 2
    # for l in range(2):
    #     for m in range(size):
    #         tempScore = 0    
    #         visited[l][m] = 1
    #         dfs(l, m)
    #         visited = [[0] * (size)] * 2
    # print(maxScore)
    # maxScore = 0
    if size>1:
        stickerArr[0][1] += stickerArr[1][0]
        stickerArr[1][1] += stickerArr[0][0]
    for k in range(2, size):
        stickerArr[0][k] += max(stickerArr[1][k-1], stickerArr[1][k-2])
        stickerArr[1][k] += max(stickerArr[0][k-1], stickerArr[0][k-2])
    print(max(stickerArr[0][-1], stickerArr[1][-1]))