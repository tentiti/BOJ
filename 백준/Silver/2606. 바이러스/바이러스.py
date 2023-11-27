comCount = int(input())
nodes = int(input())

graph = [[0 for i in range(comCount + 1)] for j in range(comCount+1)]
visited = [-1] *(comCount+1)
count = 0

for i in range(nodes):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(x, y):
    global count
    count += 1
    visited[x] = 1
    for i in range(1, comCount + 1):
        if graph[x][i] == 1 and visited[i] == -1:
            graph[x][i] = -1
            graph[i][x] = -1
            dfs(i, x)

dfs(1, 1)
print(count-1)
            
            