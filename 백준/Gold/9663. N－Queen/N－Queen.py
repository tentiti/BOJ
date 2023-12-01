# import sys
# sys.setrecursionlimit(10**6)

n = int(input())

#모든 퀸들이 가로, 세로로 중복되어서 놓여져선 안된다.
#모든 퀸들이 가로, 세로 기준으로 자신의 포지션의 차이만큼 떨어져 있어선 안된다. (대각선 상에 있으면 안된다.)
counter = 0
queenPos = [0]*n

#0번째 행 퀸의 위치를 임의의 장소로 결정
def nQueens(x):
    global counter
    if x == n:
        counter += 1
    else:
        for i in range(n):
            queenPos[x] = i
            if canPlace(x):
                nQueens(x+1)

def canPlace(x):
    for i in range(x):
        if queenPos[x] == queenPos[i] or abs(queenPos[x]-queenPos[i]) == abs(x-i):
            return False
    return True

nQueens(0)

print(counter)