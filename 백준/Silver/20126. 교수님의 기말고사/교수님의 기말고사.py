n, m, s = map(int, input().split())
tests = []

for i in range(n):
    start, length = map(int, input().split())
    tests.append([start, start+length])

tests.sort()

p = 0

for start, end in tests:
    if p + m <= start:
        print(p)
        break
    p = end

else:
    if p + m <= s:
        print(p)
    else:
        print(-1)
