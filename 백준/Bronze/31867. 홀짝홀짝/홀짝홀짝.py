def c(a,b):
    return a.count(b)
l=int(input())
a=input()
h=c(a,'1')+c(a,'3')+c(a,'5')+c(a,'7')+c(a,'9')
b=l-h
if h>b:
    r=1
elif h<b:
    r=0
else:
    r=-1
print(r)
