import sys, heapq
absArr = []
n = int(input())

for i in range(n):
    temp = int(sys.stdin.readline())
    if temp == 0:
        if len(absArr) > 0:
            print(heapq.heappop(absArr)[1])
        else:
            print(0)
    else:
       heapq.heappush(absArr, (abs(temp), temp))