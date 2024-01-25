import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

a, b = map(int, input().split())
cost = [10**9 for i in range(n+1)]
cost[a] = 0
heap = []
heapq.heappush(heap, [a, 0])

while heap:
    cur_v, cur_cost = heapq.heappop(heap)
    if cost[cur_v] < cur_cost:
        continue
    for next_v, next_cost in graph[cur_v]:
        costSum = cur_cost + next_cost
        if costSum >= cost[next_v]:
            continue
        cost[next_v] = costSum
        heapq.heappush(heap, [next_v, costSum])

print(cost[b])