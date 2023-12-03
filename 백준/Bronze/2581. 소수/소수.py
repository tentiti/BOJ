m = int(input())
n = int(input())

tempMin = 0
temp = []
for i in range(max(m,2), n+1):
    isPrime = True
    for j in range(2, i):
        if i%j == 0:
            isPrime = False
            break
    if isPrime:
        temp.append(i)

if temp:
    print(sum(temp))
    print(temp[0])
else:
    print(-1)
    