import sys
fiboTable = [[0,0] for i in range(41)]
fiboTable[0][0] = 1
fiboTable[1][1] = 1

for i in range(2, 41):
    fiboTable[i][0] = fiboTable[i-1][0]+fiboTable[i-2][0]
    fiboTable[i][1] = fiboTable[i-1][1]+fiboTable[i-2][1]

caseCnt = int(input())
for i in range(caseCnt):
    target = int(sys.stdin.readline())
    print(*fiboTable[target], sep=' ')