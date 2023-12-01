height, width = map(int, input().split())
import copy

#지도 설정
orgArr = []
for i in range(height):
    msg = list(map(int, input().split()))
    orgArr.append(msg)

#초기화된 배열
mapArr = copy.deepcopy(orgArr)
            
#spread virus function
def dfs(temp_y, temp_x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        ny = temp_y + dy[i]
        nx = temp_x + dx[i]
        if not (0<=ny<height and 0<=nx<width): continue #지도 밖이거나
        elif mapArr[ny][nx] != 0: continue #2거나 1이면 건너뛰규
        else: #0이라면, 
            mapArr[ny][nx] = 2 #바이러스 퍼뜨리고
            dfs(ny, nx) #얘도 퍼뜨리기

#최대 안전지대 저장 변수
maxSafe = 0

#3개의 겹치지 않는 점을 지정 -> 벽이거나 바이러스에 감염되었다면 그럴 수 없음.
for i in range(height*width): #i번째 줄 -> 전범위
    if mapArr[i//width][i%width]: continue
    for j in range(i+1, height*width):
        if mapArr[j//width][j%width]: continue
        for k in range(j+1, height*width):
            if mapArr[k//width][k%width]: continue
            
            # print(i, j, k, maxSafe)
            # for _ in mapArr:
            #     print(_)
            
            #dfs 배열 초기화
            # visited =[[0]*width]*height
            
            #셋 다 0이니 1로 바꿈
            mapArr[i//width][i%width] = 1
            mapArr[j//width][j%width] = 1
            mapArr[k//width][k%width] = 1
            
            #모든 바이러스 감염시키기.
            for l in range(height):
                for m in range(width):
                    if mapArr[l][m] == 2: #바이러스가 있다면, (굳이 중복은 X)
                        dfs(l, m) #퍼트리기
            # for _ in mapArr:
            #     print(_)
            
            #이제 다 퍼뜨렸으니, 안전구역 개수 세기
            tempSafe = 0
            for l in range(height):
                for m in range(width):
                    if mapArr[l][m] == 0: #0이라면
                        tempSafe += 1
            
            #더 큰 안전구역 수
            maxSafe = max(tempSafe, maxSafe)
            
            #배열 초기화
            mapArr = copy.deepcopy(orgArr)

print(maxSafe)

    