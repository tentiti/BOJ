n, m = input().split()
p = [0 for i in range(int(n))]
r = 0
for r in range(int(m)):
  i, j, k = input().split()
  i = int(i)
  j = int(j)
  k = int(k)
  while i-1<j:
    p[i-1] = k
    i+=1
print(*p, sep=' ')