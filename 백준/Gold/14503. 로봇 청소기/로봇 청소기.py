n, m = map(int, input().split())
yPos, xPos, direction = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
# print(len(arr))
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]] #y축먼저 씀
ans = 0
count = 0 

while True:
    count += 1
    # print(count, ans, yPos, xPos, direction)
    
    #1. 현재 칸이 청소되지 않은 경우, 청소한다
    if arr[yPos][xPos] == 0:
        # print('cleaned', yPos, xPos)
        ans += 1
        arr[yPos][xPos] = -1 #청소완료 표시
    
    # 주변에 청소되지 않은 빈 칸이 있나 확인
    flag = False
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    for i in range(4):
        if not (0< yPos + dy[i] < n and 0< xPos + dx[i] < m): continue #행렬 벗어나지 않게 (0,0)
        if arr[yPos + dy[i]][xPos + dx[i]] == 0: #만약에 0이라면?
            flag = True #탐색 끝
            break
        
    #하나라도 있는 경우
    if flag:
        # print('rotated from {} to {}'.format(direction, (direction-1)%4))
        direction = (direction-1)%4 #반시계 방향 회전
        #앞쪽칸이 청소되지 않았다면, 전진한다
        if (0<=yPos+dir[direction][0] <n and 0<= xPos+dir[direction][1] <m): #벗어나지 않는다면,
            if True:
                if arr[yPos+dir[direction][0]][xPos+dir[direction][1]] == 0: #청소하지 않았다면, 전진
                    # print('frontward from {}{} to {}{}'. format(yPos, xPos, yPos+dir[direction][0], xPos+dir[direction][1]))
                    yPos += dir[direction][0]
                    xPos += dir[direction][1]
                
    #2. 하나도 없는 경우
    else:
        # if (0<=yPos-dir[direction][0] <m-1 and 0<= xPos-dir[direction][1] <n-1): #벗어나지 않았다면,
        if True:
            if arr[yPos - dir[direction][0]][xPos - dir[direction][1]] == 1: #벽을 마주친다면
                break #작동을 멈춘다
            else: #후진할 수 있다면 후진한다.
                # print('backward from {}{} to {}{}'. format(yPos, xPos, yPos-dir[direction][0], xPos-dir[direction][1]))
                yPos -= dir[direction][0]
                xPos -= dir[direction][1]
                #자연스레 1번으로 돌아간다.

print(ans)