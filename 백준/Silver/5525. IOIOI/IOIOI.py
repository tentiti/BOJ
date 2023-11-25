n = int(input())
s = int(input())
m = input()
q = 'I'
count = 0
for i in range(n):
    q += 'OI'


for i in range(n, s-n):
    # print(m[i-n:i+n+1])
    if m[i-n:i+n+1] == q:
        count += 1

print(count)