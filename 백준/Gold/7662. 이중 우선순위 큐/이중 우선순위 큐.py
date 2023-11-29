import sys
input = sys.stdin.readline

# from collections 
import heapq

testCase = int(input())

for i in range(testCase):
    maxQueue = []
    minQueue = []
    commandCount = int(input())
    visit = [False] * commandCount
    for j in range(commandCount):
        command = input().split()
        if command[0] == 'I':
            heapq.heappush(maxQueue, (-int(command[1]), j))
            heapq.heappush(minQueue, (int(command[1]), j))
            visit[j] = True #이때 넣은건 아직 삭제 안된거임
        else:
            if command[1] == '-1': #지우라는 명령이 들어왔으면 -> 이렇게 지우면 각각 제일 앞에 최소, 최댓값 들어옴
                while minQueue and visit[minQueue[0][1]] == False: #앞에서 지웠던 것들 다 지워버리고 난 다음에
                    heapq.heappop(minQueue)
                if minQueue: #남은게 있으면
                    visit[minQueue[0][1]] = False #최슛값 삭제 동기화
                    heapq.heappop(minQueue) 
            else:
                while maxQueue and visit[maxQueue[0][1]] == False: #앞에서 지웠던 것들 다 지워버리고
                    heapq.heappop(maxQueue)
                if maxQueue:
                    visit[maxQueue[0][1]] = False #최댓값 삭제 동기화
                    heapq.heappop(maxQueue)
                        
    #명령어 끝나고 출력할 시간
    while minQueue and visit[minQueue[0][1]] == 0: #앞에서 지웠던 것들 다 지워버리고
        heapq.heappop(minQueue)
    while maxQueue and visit[maxQueue[0][1]] == 0: #앞에서 지웠던 것들 다 지워버리고
        heapq.heappop(maxQueue)
        
    if not maxQueue and not minQueue:
        print('EMPTY')
    else:
        print(-maxQueue[0][0], minQueue[0][0])