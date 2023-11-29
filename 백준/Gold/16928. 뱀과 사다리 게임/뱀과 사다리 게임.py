from collections import deque

ladderCount, snakeCount = map(int, input().split())

mapArr = [0]*101
visited = [0]*101

ladder = dict()
snake = dict()

for i in range(ladderCount):
    start, dest =  map(int, input().split())
    ladder[start] = dest
    
for i in range(snakeCount):
    start, dest =  map(int, input().split())
    snake[start] = dest

queue = deque()

queue.append(1)

while queue:
    loc = queue.popleft()
    if loc == 100:
        print(mapArr[100])
        break
    for  dice in range(1,7):
        newLoc = loc + dice
        if newLoc > 100: break
        if not visited[newLoc]:
            if newLoc in ladder.keys():
                newLoc = ladder[newLoc]
            elif newLoc in snake.keys():
                newLoc = snake[newLoc]
            if not visited[newLoc]:
                visited[newLoc] = True
                mapArr[newLoc] = mapArr[loc] + 1
                queue.append(newLoc)