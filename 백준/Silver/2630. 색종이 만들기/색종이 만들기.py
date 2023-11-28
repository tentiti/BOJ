import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

#종이 설정
paperSize = int(input())
paper = []
for i in range(paperSize):
    paper.append(list(map(int, input().split())))

paperCount = 0
paperBlue = 0
paperWhite = 0
def paperCut(startY, startX, endY, endX):
    global paperCount, paperBlue, paperWhite
    targetColor = paper[startY][startX]
    match = True
    for i in range(startY, endY):
        if not match:
            break
        for j in range(startX, endX):
            if paper[i][j] != targetColor:
                #만약 다 같지 않다면?
                match = False
                break
    if match:
        paperCount += 1
        if targetColor == 1:
            paperBlue += 1
        else:
            paperWhite += 1
    if not match:
        size = endY - startY 
        paperCut(startY, startX, startY+size//2, startX+size//2)
        paperCut(startY, startX+size//2, startY+size//2, startX+size//2+size//2)
        paperCut(startY+size//2, startX, startY+size//2+size//2, startX+size//2)
        paperCut(startY+size//2, startX+size//2, startY+size//2+size//2, startX+size//2+size//2)

paperCut(0, 0, paperSize, paperSize)
print(paperWhite)
print(paperBlue)