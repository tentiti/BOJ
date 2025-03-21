import heapq

def solution(operations):
    minQueue = []
    maxQueue = []
    visit = dict()  # 인덱스 대신 id로 동기화 관리
    idx = 0  # 고유한 인덱스
    
    for op in operations:
        command, value = op.split()
        value = int(value)
        
        if command == 'I':
            heapq.heappush(minQueue, (value, idx))
            heapq.heappush(maxQueue, (-value, idx))
            visit[idx] = True  # 삽입된 상태
            idx += 1
        
        elif command == 'D':
            if value == 1:  # 최댓값 삭제
                while maxQueue and not visit[maxQueue[0][1]]:
                    heapq.heappop(maxQueue)
                if maxQueue:
                    visit[maxQueue[0][1]] = False
                    heapq.heappop(maxQueue)
            
            elif value == -1:  # 최솟값 삭제
                while minQueue and not visit[minQueue[0][1]]:
                    heapq.heappop(minQueue)
                if minQueue:
                    visit[minQueue[0][1]] = False
                    heapq.heappop(minQueue)
    
    # 마지막으로 동기화 정리
    while minQueue and not visit[minQueue[0][1]]:
        heapq.heappop(minQueue)
    while maxQueue and not visit[maxQueue[0][1]]:
        heapq.heappop(maxQueue)
    
    if not minQueue or not maxQueue:
        return [0, 0]
    
    max_val = -maxQueue[0][0]
    min_val = minQueue[0][0]
    
    return [max_val, min_val]
