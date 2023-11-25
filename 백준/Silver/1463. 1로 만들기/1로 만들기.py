import sys
sys.setrecursionlimit(10**6)

counter = [-1 for i in range(10**6+2)]
counter[1] = 0
counter[2] = 1
counter[3] = 1

x = int(input())
# print(dotherightthing(x, 0))
for i in range(4, x+1):
    if i%3 == 0 and i%2 == 0:
        counter[i] = min(counter[i//3]+1, counter[i//2]+1)
    elif i%3 ==0 and i%2 != 0:
        counter[i] = min(counter[i//3]+1, counter[i-1]+1)
    elif i%3 != 0 and i % 2 == 0:
        counter[i] = min(counter[i-1]+1, counter[i//2]+1)
    else:
        counter[i] = counter[i-1] + 1
print(counter[x])

