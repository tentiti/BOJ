from collections import deque
tc = int(input())

for i in range(tc):
    points, routes, wormhole = map(int, input().split())
    connections = []
    for j in range(routes):
        start, end, time = map(int, input().split())
        connections.append([start, end, time])
        connections.append([end, start, time])
    for j in range(wormhole):
        start, end, time = map(int, input().split())
        connections.append([start, end, -time])

    answerFound = False
    #계속 왕복할 때 가중치가 줄어드는 곳이 있다면, 시작점을 1로 잡아도 거기선 줄어들거임.
    distance = [10**5 for i in range(points+1)]
    distance[0] = 0
    distance[1] = 0
    
    for i in range(points):
        if answerFound: break
        for connection in connections:
            start = connection[0]
            end = connection[1]
            cost = connection[2]
            if distance[end] > cost+distance[start]:
                distance[end] =  cost+distance[start] #벨만포드 작동중,,,
                if i == points-1: #근데 만약 지점수-1번을 돌렸는데도 있다면,
                    print("YES") #음의 사이클이 존재하는거임, 왜냐면 아니라면 최단거리루트 찾아씅니까
                    answerFound = True
                    break
    if not answerFound: print("NO")
            