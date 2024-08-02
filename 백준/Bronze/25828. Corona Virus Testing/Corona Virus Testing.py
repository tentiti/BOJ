g,p,t=map(int,input().split())
if t*p+g>g*p: print(1)
elif t*p+g<g*p: print(2)
else: print(0)