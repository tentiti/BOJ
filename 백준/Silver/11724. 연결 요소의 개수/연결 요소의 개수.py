import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

nodes, lines = map(int, input().split())

graph = [[] for _ in range(nodes + 1)]
visited = [-1 for _ in range(nodes + 1)]

def dfs(startPoint):
    visited[startPoint] = 1
    if graph[startPoint]:
        for destination in graph[startPoint]:
            if visited[destination] == -1:
                # print(startPoint, destination)
                dfs(destination)

for i in range(lines):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# print(graph)
    
dfs(1)

counter = 1

for i in range(1, nodes + 1):
    if visited[i] == -1:
        counter += 1
        dfs(i)

print(counter)