#max가 아니라 여기까지 가는데 소요되는 거리로 visited 사용

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(v):
    for i in tree[v]: #내가 갈 수 있는 것 중에
        if visited[i[0]]==-1: #안가본 곳은
            visited[i[0]] = i[1] + visited[v] #나한테서 이곳까지 가는데 드는 거리
            dfs(i[0])

nodeCount = int(input())
tree = [[] for i in range(nodeCount+1)]
for i in range(1, nodeCount+1):
    tempNode = list(map(int, input().split()))
    for j in range(1, len(tempNode)-1, 2):
        tree[tempNode[0]].append([tempNode[j], tempNode[j+1]])

#한번 갔다 온 뒤에는
root = 1
visited = [-1] * (nodeCount+1)
# print(visited)
visited[root] = 0
dfs(1)

# print(visited)

# #그 자리에서 한번 더 dfs 돌리면
start = visited.index(max(visited))

visited = [-1] * (nodeCount+1)
# visited[maxPos] = 1 
# visited[root] = 1
visited[start] = 0
dfs(start)
# print(visited)

# #답
print(max(visited))