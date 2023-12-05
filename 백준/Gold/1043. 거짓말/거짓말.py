from collections import deque

n, m = map(int, input().split())
truth = input()
if truth == '0':
    print(m)
    exit(0)
else:
    truthKnown = int(list(truth.split())[0])
    truthKnower = list(map(int, truth.split()))[1:]
# print(truthKnower, truthKnown)
parties = []
for i in range(m):
    parties.append(list(map(int, input().split()))[1:])
# print(parties)

#진실을 아는 사람과 한번이라도 만나는 사람이 있는 파티에서는 거짓말을 할 수 없음.
#사람들끼리의 그래프로 이걸 변환하면 됨!
graph = [[] for i in range(n+1)]

#graph
for party in parties:
    for i in range(len(party)):
        for j in range(i, len(party)):
            a = party[i]
            b = party[j]
            if a not in graph[b]:
                graph[a].append(b)
                graph[b].append(a)

stupidPeople = [0 for i in range(n+1)]
visited = [0 for i in range(n+1)]
for smart in truthKnower:
    queue = deque()
    queue.append(smart)
    
    while queue:
        temp = queue.popleft()
        stupidPeople[temp] = 1
        visited[temp] = 1
        for dest in graph[temp]:
            if visited[dest] == 0:
                stupidPeople[dest]= 1
                visited[dest]= 1
                queue.append(dest)
    
    visited = [0 for i in range(n+1)]

count = 0
# print(stupidPeople[1:])
for party in parties:
    canLie = True
    for attendee in party:
        # print(attendee)
        if stupidPeople[attendee]:
            canLie = False
            break
    if canLie: 
        # print(party)
        count += 1

print(count)
