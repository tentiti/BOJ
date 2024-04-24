for i in range(int(input())):
    a, b = map(int, input().split())
    if not a%2 and not b%2: # 2 4
        print(int(a*b/2))
    elif not a%2 and b%2: # 2 3
        print(b*(a//2))
    elif a%2 and not b%2: # 3 2
        print(a*(b//2))
    else: # 3 3
        print(a*((b-1)//2)+a//2)
