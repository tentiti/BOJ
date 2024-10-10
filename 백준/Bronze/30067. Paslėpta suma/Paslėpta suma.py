a=list(map(int,open(0).readlines()))
b=sum(a)/2
for k in a:
    if k==b:
        print(k)
        break