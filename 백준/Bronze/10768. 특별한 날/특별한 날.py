m = int(input())
d = int(input())

if m> 2 or (m==2 and d>18): print("After")
elif m<2 or d<18: print("Before")
else:
    print("Special")