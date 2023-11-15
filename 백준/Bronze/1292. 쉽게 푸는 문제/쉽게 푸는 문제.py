a, b = map(int, input().split())

arr = [0 for i in range(1002)]
#구현 -> 어차피 돌려야함,,,
cnt = 0
for i in range(1, 51):
    if cnt == 1001: break
    for j in range(i):
        if cnt == 1001: break
        arr[cnt] = i
        cnt += 1
me = 0

for i in range(a, b+1):
    me += arr[i-1]
    
print(me)