m,s,g=map(float,input().split())
a,b=map(float,input().split())
l,r=map(float,input().split())
print('friskus' if m/g+l/a<m/s+r/b else 'latmask')