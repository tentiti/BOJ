import sys
sys.setrecursionlimit(10**6)


def winner(s, b, s_start, b_start):
    if b[b_start] <= s[s_start]:
        b_start += 1
    else:
        s_start += 1

    if (s_start == n) and (b_start == m):
        print('C')
    elif b_start == m:
        print('S')
    elif s_start == n:
        print('B')
    else:
        # print(s, b, s_start, b_start)
        winner(s, b, s_start, b_start)


for i in range(int(input())):
    t = input()
    n, m = map(int, input().split())
    s = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    # print(s, b)
    winner(s, b, 0, 0)
