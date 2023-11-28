import sys
input = sys.stdin.readline

n, m = map(int, input().split())

myList = tuple(map(int, input().split()))
mySum = [0]

temp = 0
for i in myList:
    temp += i
    mySum.append(temp)

for i in range(m):
    a, b = map(int, input().split())
    print(mySum[b]-mySum[a-1])