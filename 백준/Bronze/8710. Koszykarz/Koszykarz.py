a, b, c = map(int, input().split())
if (b-a)%c:
    print((b-a)//c+1)
else:
    print((b-a)//c)