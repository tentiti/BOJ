import heapq, sys
input = sys.stdin.readline
myHeap = []
rep = int(input())
for i in range(rep):
    command = int(input())
    if command == 0:
        if len(myHeap):
            print(-heapq.heappop(myHeap))
        else:
            print(0)
    else:
        heapq.heappush(myHeap, -command)