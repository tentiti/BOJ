a, b = map(int, input().split())

count = 0
ans = -1

for i in range(1, a+1):
    if a%i == 0:
        count += 1
        ans = i
    if count == b:
        break

if count < b :
    ans = 0
    
print(ans)