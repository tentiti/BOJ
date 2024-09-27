a,b=map(int,input().split())
k,x=map(int,input().split())

f=min(k+x,b)-max(k-x,a)+1
print(f if f>0 else 'IMPOSSIBLE')