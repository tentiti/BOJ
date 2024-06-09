a=int(input())
b,c,d=map(int,input().split())
b,c,d=min(a,b),min(a,c),min(a,d)
print(b+c+d)