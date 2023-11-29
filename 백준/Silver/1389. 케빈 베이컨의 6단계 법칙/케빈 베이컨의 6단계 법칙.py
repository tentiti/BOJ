userCount, friendCount = map(int, input().split())

friendArr = [[0 for i in range(userCount + 1)] for j in range(userCount + 1)]

for i in range(friendCount):
    a, b = map(int, input().split())
    friendArr[a][b] = 1
    friendArr[b][a] = 1
# for _ in friendArr:
#     print(_)
    
for i in range(1, userCount+1):
    for j in range(1, userCount+1):
        for k in range(1, userCount+1):
            #직접 갈 수 없는데, 거쳐서 갈 수 있거나, 가는 방법이 있는데(둘 다 고려) 더 빨리 갈 수 있다면
            if (friendArr[j][k] == 0 and friendArr[j][i] and friendArr[i][k])\
                or (friendArr[j][k] and friendArr[j][i] and friendArr[i][k] and friendArr[j][k] > friendArr[j][i] + friendArr[i][k]):
                #돌아가는 경로를 선택
                friendArr[j][k] = friendArr[j][i] + friendArr[i][k]

# print('result')
# for _ in friendArr:
#     print(_)

baconNum = [0 for i in range(userCount+1)]
baconNum[0] = 0 #무수히 큰 수)
baconUser = 0
for i in range(1, userCount+1):
    baconNum[i] = sum(friendArr[i])
    if not baconUser or baconNum[i]< baconNum[baconUser]:
        baconUser = i

print(baconUser)
    