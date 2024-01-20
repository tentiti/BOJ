a, b = map(int, input().split())
c = list(map(int, input().split()))

for i in range(len(c)):
    print(c[i]-a*b, end=' ')