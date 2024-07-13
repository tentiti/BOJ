for i in range(int(input())):
    t = input()
    n, m = map(int, input().split())
    s = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    if s[-1] >= b[-1]:
        print('S')
    else:
        print('B')