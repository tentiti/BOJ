n = int(input())
numList = list(map(int, input().split()))
for i in range(n):
    numList[i] %= 2
if sum(numList) >= n - sum(numList): 
    print('Sad')
else:
    print('Happy')