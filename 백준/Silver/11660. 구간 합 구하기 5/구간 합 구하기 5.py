import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

#단순하게 구간합을 구하는 식으로 제작하면, 0,0과 n,n에 근접한 지점을 계속 구하면 시간초과
#메모리 희생하고 전체적으로 계산해서 각 계산은 덧셈 몇 번 정도로 끝나게 접근
supArr = [[0 for i in range(n+1)] for i in range(n+1)]

#가로로 한번 누적합으로 변경
for i in range(1, n+1):
    for j in range(1, n+1):
        supArr[i][j] = supArr[i][j-1] + supArr[i-1][j] - supArr[i-1][j-1] + arr[i-1][j-1]
#전체적으로 하나씩 올라가 있기 때문에 마지막에 1씩 빼주는 것

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # x1, y1, x2, y2 = x1 -1,  y1-1, x2-1,y2-1
    print(supArr[x2][y2]-supArr[x2][y1-1]-supArr[x1-1][y2]+supArr[x1-1][y1-1])

    