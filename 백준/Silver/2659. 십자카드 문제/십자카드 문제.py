num = input().split()

# 십자수 찾기
minNum = min(int(''.join(num)), int(''.join((num[1:]+num[0:1]))),
             int(''.join((num[2:]+num[0:2]))), int(''.join((num[3:]+num[0:3]))))

# print(minNum)


def isSN(n):
    num = str(n)
    minNum = min(int(''.join(num)), int(''.join((num[1:]+num[0:1]))),
                 int(''.join((num[2:]+num[0:2]))), int(''.join((num[3:]+num[0:3]))))
    return n == (minNum)


res = 0
# print(minNum)

for i in range(1111, minNum+1):
    if '0' in str(i):
        continue
    if isSN(i):
        res += 1

print(res)
