orbCount = int(input())

minX, minY, maxX, maxY = 10001, 10001, -10001, -10001

for i in range(orbCount):
    x, y = map(int, input().split())
    minX = min(x, minX)
    minY = min(y, minY)
    maxX = max(x, maxX)
    maxY = max(y, maxY)
    
print((maxX-minX)*(maxY-minY))