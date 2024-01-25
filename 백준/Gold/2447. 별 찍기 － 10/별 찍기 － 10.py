n = int(input())

# 9 => 5 빼고는 출력
# 27 => 15 빼고는 출력

arr = [[' ' for i in range(n)] for i in range(n)]

def starPrinter(size, yPos, xPos):
    if size == 3:
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [1, 0, -1, 1, -1, 1, 0, -1]
        for i in range(8):
            arr[yPos+dy[i]][xPos+dx[i]] = '*'
    else:
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [1, 0, -1, 1, -1, 1, 0, -1]
        for i in range(8):
            starPrinter(size//3, yPos+size//3*dy[i], xPos+size//3*dx[i])
        
#starPrint
starPrinter(n, n//2, n//2)

for i in arr:
    print(*i, sep='')