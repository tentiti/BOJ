rep = int(input())
papers = [[0 for i in range(100)] for j in range(100)]

for i in range(rep):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            papers[i][j] = 1
sum = 0
for i in range(100):
    for j in range(100):
        sum += papers[i][j]

print(sum)