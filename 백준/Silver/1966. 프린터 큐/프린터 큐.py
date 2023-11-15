from collections import deque
import sys
for rep in range(int(input())): #테스트케이스의 수
    
    n, m = map(int, input().split()) #n, m
    waitQueue = deque(list(map(int, sys.stdin.readline().split())))#중요도
    count = 0
    while waitQueue:
        best = max(waitQueue)
        front = waitQueue.popleft()
        m -= 1
        
        if best == front:
            count += 1
            if m<0:
                print(count)
                break
        
        else:
            waitQueue.append(front)
            if m<0:
                m = len(waitQueue) - 1
            
    
    # for i in range(n): #중요도
    #     waitQueue[i] = [int(waitQueue[i]), i]
    
    # #정렬을 하는데요...
    # needSort = True
    # while needSort:
    #     needSort = False
    #     for i in range(n):
    #         for j in range(i, n):
    #             #뒤에 중요도가 더 높은게 하나라도 있으면
    #             if waitQueue[i][0] < waitQueue[j][0]:
    #                 needSort = True
    #                 #나를 제일 뒤로 넣음
    #                 temp = waitQueue[i]
    #                 waitQueue.pop(i)
    #                 waitQueue.append(temp)
                    
    #             #아니면 걍 그 자리에서 인쇄 (할 거 없음)
    
    # # print("after", waitQueue)
    # #그 다음에        
    # for i in range(n):
    #     #원래 위치가 내가 궁금하던 그거면
    #     if waitQueue[i][1] == m:
    #         print(i+1) #순서로 뽑기
    #         break #띁