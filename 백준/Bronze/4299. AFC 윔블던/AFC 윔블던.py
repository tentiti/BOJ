hap, cha = map(int, input().split())

x = (hap-cha)//2

if x*2+cha == hap and x>=0:
    print(x+cha, x)
else:
    print(-1)