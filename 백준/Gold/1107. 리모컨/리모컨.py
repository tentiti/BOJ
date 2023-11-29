target = int(input())
brokeKeys = int(input())

if brokeKeys:    
    broken = tuple(input().split())
else:
    broken = []

minDist = abs(100-target)
for i in range(1000001):
    m = str(i)
    for l in m:
        if l in broken:
            break
    else:
        minDist = min(minDist, abs(i-target)+len(m))
print(minDist)