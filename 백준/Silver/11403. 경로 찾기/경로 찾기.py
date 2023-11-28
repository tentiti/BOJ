import sys
sys.setrecursionlimit(10**7)

size = int(input())
mapArr = []
for i in range(size):
    mapArr.append(list(map(int, input().split())))
visited = [[0]*size for _ in range(size)]
n = size
for i in range(n):
    for j in range(n):
        for k in range(n):
            if mapArr[j][i] == 1 and mapArr[i][k] == 1:
                mapArr[j][k] = 1

for _ in mapArr:
    print(*_)
