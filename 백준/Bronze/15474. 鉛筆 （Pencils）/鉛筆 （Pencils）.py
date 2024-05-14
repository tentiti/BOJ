from math import ceil as m
n,a,b,c,d=map(int,input().split())
print(min(m(n/a)*b, m(n/c)*d))