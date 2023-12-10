import sys, heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())

adjDepList = [[] for i in range(n+1)]
adjArrList = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    adjDepList[b].append([a, c])
    adjArrList[a].append([b, c])


depVisited = [0 for i in range(n+1)]
minArrDist = [10**9 for i in range(n+1)]
arrVisited = [0 for i in range(n+1)]

#start에서의 거리 구하기 -> 힙으로 구현
def dijkstra(start):
    q = []
    distance = [10**9 for i in range(n+1)]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for b, c in adjDepList[now]:
            cost = dist + c
            if distance[b] > cost:
                distance[b] = cost
                heapq.heappush(q, (cost, b))
    
    return distance

answer = 0
xToEverywhere = dijkstra(x)
# print(xToEverywhere)
for i in range(1, n+1):
    iToEverywhere = dijkstra(i)
    # print(iToEverywhere)
    answer = max(answer, iToEverywhere[x]+xToEverywhere[i])

print(answer)