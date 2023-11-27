import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values = []

for i in range(n):
    temp = int(input())
    if temp <= k:
        values.append(temp)
    else:
        break
    
count = 0
while k > 0:
    for i in range(len(values)):
        if k >= values[len(values)-i-1]:
            count += k//values[len(values)-i-1]
            k %= values[len(values)-i-1]
            if k < values[len(values)-i-1]:
                values.pop(-1)
            break
print(count)