n, m, r = map(int, input().split())

items = list(map(int, input().split()))
route = [[] for i in range(n+1)]
plainRoute = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]    
maxItem, itemEarned = 0, 0

for i in range(r):
    a, b, l = map(int, input().split())
    route[a].append([b, l])
    route[b].append([a, l])
    plainRoute[a].append(b)
    plainRoute[b].append(a)

#dfs -> doesn't work
def dfs(v, distance):
    global itemEarned
    for j in route[v]:
        if distance+j[1] > m:
            continue
        # print(j)
        if visited[j[0]] == 0:
            visited[j[0]] = 1
            itemEarned += items[j[0]-1]
            dfs(j[0], distance+j[1])
        else:
            dfs(j[0], distance+j[1])   
            
for i in range(1, n+1):
    itemEarned = items[i-1]
    visited[i] = 1
    dfs(i, 0)
    # print(visited[1:])
    visited = [0 for i in range(n+1)]
    # print(maxItem, itemEarned)
    maxItem = max(maxItem, itemEarned)

#dijkstra
# for i in range(1, n+1): #i is starting point
#     #i에서 모든 node에 대해 dijkstra 실시
#     nodes = [j+1 for j in range(n+1)]
#     nodes.pop(nodes.index(i)) # -> 일단 나는 제거
#     distance = [10**9 for i in range(n+1)] #infinite distance table
#     distance[i] = 0 #self distance = 0

#     #이제 여기서 뭔가 재귀적 / 무한적으로 돌아가면 됨
#     thisNode = i
#     while nodes and route[thisNode]:    
#         temp_dist = 10**9
#         temp_loc = -1
#         for j in route[thisNode]: #이 (새로운) vertex에서 갈 수 있는 거리, 원래 거리 중에 작은거. 
#             #self dist를 0으로 설정하고, dist를 무한대로 설정했기에 이런 식으로 하면 됨.
#             distance[j[0]] = min(distance[i]+j[1], distance[j[0]])
#             if j[1]<temp_dist: #최소거리의 node 저장
#                 temp_dist=j[1]
#                 temp_loc = j[0]
#         if temp_loc in nodes:
#             nodes.pop(nodes.index(temp_loc))
#             thisNode = temp_loc
#         else:
#             break
        
#     #거리 계산 완료
#     for j in range(1, n+1):
#         if i != j and distance[j] <= r:
#             itemEarned += items[j-1]
    
#     maxItem = max(itemEarned, maxItem)
#     itemEarned = 0

print(maxItem)