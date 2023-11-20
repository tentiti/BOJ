import sys
n, m, b = map(int, sys.stdin.readline().split())

terrain = []
for i in range(n):
    terrain.extend(list(map(int, sys.stdin.readline().split())))

target = -1
timeCount = int(1e9)
for i in range(min(terrain), max(terrain)+1):
    #target is i
    #do task
    use = 0
    get = 0
    thisTime = 0
    for x in terrain:
        if x < i:
            use += (i - x) #쓴 거 
        if x > i:
            get += (x - i) #얻은 거
    #compare time
    #smaller or the same? change the target.(asc)
    if use > get + b: #만약 만들 수 없다면 패스
        continue
    else:
        if 2*get + use <= timeCount: #아니면 쓴 시간이 더 적거나 같다면(오름차순이고 가장 높은 것)
            target = i
            timeCount = 2*get + use    

print(timeCount, target)