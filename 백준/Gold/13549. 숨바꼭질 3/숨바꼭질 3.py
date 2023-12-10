from collections import deque

subinVisited =  [-1 for i in range(100001)]

subin, brother = map(int, input().split())

queue = deque()
queue.append(subin)
subinVisited[subin] = 0

while queue:
    charLoc = queue.popleft()
    if charLoc == brother:
        print(subinVisited[brother])
        break
    if 0<=charLoc*2<=100000 and subinVisited[charLoc*2] == -1:
        subinVisited[charLoc*2] = subinVisited[charLoc]
        queue.appendleft(charLoc*2)
    if 0<=charLoc-1<=100000 and subinVisited[charLoc-1] == -1:
        subinVisited[charLoc-1] = subinVisited[charLoc]+1
        queue.append(charLoc-1)
    if 0<=charLoc+1<=100000 and subinVisited[charLoc+1] == -1:
        subinVisited[charLoc+1] = subinVisited[charLoc]+1
        queue.append(charLoc+1)