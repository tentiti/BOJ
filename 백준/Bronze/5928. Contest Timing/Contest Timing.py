d, h, m = map(int, input().split())
if d<11 or (d==11 and h<11) or (d==11 and h==11 and m<11): print(-1)
else:
    print((d-11)*1440+(h-11)*60+m-11)