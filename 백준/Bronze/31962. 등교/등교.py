a=open(0).readlines()
n,x=map(int,a[0].split())
ans = -1
for i in range(1, n+1):
    tn, tx = map(int,a[i].split())
    if tn+tx <= x and ans <= tn:
        ans = tn
print(ans)