a, b = input().split()

if int(a[::-1]) > int(b[::-1]):
    print(int(a[::-1]))
else:
    print(int(b[::-1]))