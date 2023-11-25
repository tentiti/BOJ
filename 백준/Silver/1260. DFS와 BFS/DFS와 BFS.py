import sys
sys.setrecursionlimit(10**6)
n, m, v = map(int, input().split())

arr=[[0 for i in range(n+1)] for i in range(n+1)]
dfsSeen = [False for i in range(n+1)] 
bfsSeen = [False for i in range(n+1)] 

def dfs(n, startP):
    dfsSeen[startP] = True
    print(startP,end=' ')
    for i in range(1, n+1):
        if arr[startP][i] == 1 and not dfsSeen[i]:
            dfs(n, i)

def bfs(n, v):
    if not bfsSeen[v]:
        print(v, end=' ')
    bfsSeen[v] = True
    for i in range(1, n+1):
        if arr[v][i] == 1 and not bfsSeen[i]:
            bfsList.append(i)
    while len(bfsList) != 0:
        bfs(n, bfsList.pop(0))

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

# dfsSeen[v] = True
# bfsSeen[v] = True

dfs(n, v)
print()
bfsList = []
bfs(n, v)