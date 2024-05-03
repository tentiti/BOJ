for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    if b+c+d < 55:
        print(a, b+c+d, 'FAIL')
    elif min(b/35, c/25, d/40) < 0.3:
        print(a, b+c+d, 'FAIL')
    else:
        print(a, b+c+d, 'PASS')