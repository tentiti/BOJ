n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())
s = set(s)
temp = 0
for i in range(m):
    if input() in s: temp += 1
print(temp)