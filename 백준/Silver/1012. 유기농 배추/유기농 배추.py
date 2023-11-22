import sys
sys.setrecursionlimit(10**6)

testCase = int(sys.stdin.readline())

#dfs
def dfs(xpos, ypos):
    dx = [0,0,-1,1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = xpos + dx[i]
        ny = ypos + dy[i]
        if(0<=nx<width and 0<=ny<height) and baechuGround[ny][nx] == 1:
            baechuGround[ny][nx] = -1
            dfs(nx, ny)
    
for case in range(testCase):
    answer = 0
    width, height, baechu = map(int, sys.stdin.readline().split())
    baechuGround = [[0]*width for i in range(height)]
    for i in range(baechu):
        x, y = map(int, sys.stdin.readline().split())
        baechuGround[y][x] = 1
    
    # print(baechuGround)
    for i in range(width):
        for j in range(height):
            if baechuGround[j][i] ==1:
                dfs(i, j)
                answer += 1
            
    # print(baechuGround)
    # dfs(baechuGround, width, height, 1, 1)
    print(answer)
    # print(baechuGround)
    