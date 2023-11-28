# some dp stuff..
import sys
n = int(sys.stdin.readline())

dpArr = [0 for i in range(50001)]
dpArr[0] = 0
for i in range(1, n+1):
    dpArr[i] = dpArr[i-1]+1
    for j in range(int(i**0.5), 0, -1):
        dpArr[i] = min(dpArr[i], dpArr[i-j**2]+1)

print(dpArr[n])