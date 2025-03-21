import heapq

def solution(jobs):
    jobs.sort()
    heap, time, i, res = [], 0, 0, 0
    n = len(jobs)
    
    while i<n or heap:
        while i<n and jobs[i][0] <= time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i+=1
            
        if heap:
            dur, req = heapq.heappop(heap)
            time += dur
            res += time - req
        else:
            time = jobs[i][0]
    
    return res // n