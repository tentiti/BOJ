a=open(0).readlines()[1:]
r=200
for b in a:
    r=min(r, sum(list(map(int,b.split()))))
print(r)