a,b,c,d=map(float,input().split())
e,f,g,h=map(int,[a,b,c,d])
print(+((a/b*c/d)==(e/f*g/h) and (e/f*g/h)%2==0))