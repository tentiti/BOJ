import sys, heapq
input = sys.stdin.readline

v, e = map(int, input().split())
x = int(input())

adjList = [[] for i in range(v+1)]

for i in range(e):
    a, b, c = map(int, input().split())
    adjList[a].append([b, c])
    #서로 다른 두 정점에 여러개의 간선을 계산해야함
    

#start에서의 거리 구하기 -> 힙으로 구현
def dijkstra(start):
    q = []
    distance = [10**9 for i in range(v+1)]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for b, c in adjList[now]:
            cost = dist + c
            if distance[b] > cost:
                distance[b] = cost
                heapq.heappush(q, (cost, b))
    
    return distance

answerArr = dijkstra(x)

for _ in answerArr[1:]:
    if _ == 10**9:
        print("INF")
    else:
        print(_)