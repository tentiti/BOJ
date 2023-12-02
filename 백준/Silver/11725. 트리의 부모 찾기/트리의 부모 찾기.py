import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

nodeCount = int(input())
graph = [[] for i in range(nodeCount + 1)]

for i in range(nodeCount-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

used = [0 for i in range(nodeCount+1)]

def dfs(v):
    for i in graph[v]: 
        if not used[i]:
            used[i] = v
            dfs(i)    

dfs(1)

for i in range(2, nodeCount+1):
    print(used[i])