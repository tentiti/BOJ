xArr = []
yArr = []
for i in range(3):
    a, b = map(int, input().split())
    xArr.append(a)
    yArr.append(b)

for j in xArr:
    if xArr.count(j) == 1:
        print(j, end=' ')
        break
for j in yArr:
    if yArr.count(j) == 1:
        print(j, end='')
        break