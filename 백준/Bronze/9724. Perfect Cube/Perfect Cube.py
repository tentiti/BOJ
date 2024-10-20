import math
for i in range(1,int(input())+1):
    a,b=map(int,input().split())
    res = 1-math.ceil(a**(1/3))+math.floor(b**(1/3))
    print(f"Case #{i}: {res}")