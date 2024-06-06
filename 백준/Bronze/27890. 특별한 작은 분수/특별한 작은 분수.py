a,t=map(int,input().split())
for i in range(1,t+1):
    if a%2:
        a=(2*a)^6
    else:
        a=int(a//2)^6
print(a)