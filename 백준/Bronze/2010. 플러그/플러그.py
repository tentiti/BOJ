import sys
input = sys.stdin.readline

res = 0
for i in range(int(input())):
    res += int(input())-1
res += 1

print(res)