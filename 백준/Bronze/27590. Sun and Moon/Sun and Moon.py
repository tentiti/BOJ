a,b=map(int,input().split())
c,d=map(int,input().split())

s = b -a
m = d-c

while s != m:
    if s < m:
        s += b
    else:
        m += d
print(s)