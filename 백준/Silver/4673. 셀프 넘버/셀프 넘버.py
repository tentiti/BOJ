selfTable = [0 for i in range(10001)]
for i in range(100001):
    temp = i+sum(list(map(int, str(i))))
    if temp <= 10000:
        selfTable[temp] = 1
for i in range(1, 10001):
    if selfTable[i] == 0:
        print(i)
    