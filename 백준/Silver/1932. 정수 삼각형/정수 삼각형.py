triangleSize = int(input())
triangle = []

for i in range(triangleSize):
    triangle.append(list(map(int, input().split())))

ans = []
ans.append(triangle[0])

for i in range(1, triangleSize):
    temp = []
    for j in range(i+1):
        if 1 <= j <= i-1: #사이에 있는 것드리 자기 바로 위, 자기 위보다 한쪽 왼쪽 중 큰것 받아옴.
            temp.append(triangle[i][j] + max(ans[i-1][j], ans[i-1][j-1]))
        elif j == 0: #맨 왼쪽 -> 자기 위쪽것만 받아올 수 있음, 항상 [0]
            temp.append(triangle[i][0] + ans[i-1][0])
        else: #맨 오른쪽 -> 자기 위쪽것만 받아올 수 있음, 항상 [-1]
            temp.append(triangle[i][-1] + ans[i-1][-1])
    ans.append(temp)

# print(ans)
print(max(ans[-1]))
            