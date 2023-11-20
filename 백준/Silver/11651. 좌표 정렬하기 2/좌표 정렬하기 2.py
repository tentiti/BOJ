import sys
coord = []

n = int(input())
for i in range(n):
    coord.append(list(map(int, sys.stdin.readline().split())))
coord.sort(key=lambda x: (x[1], x[0]))

for _ in coord:
    print(*_, sep=" ")