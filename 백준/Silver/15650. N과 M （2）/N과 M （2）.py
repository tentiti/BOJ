n, m = map(int, input().split())

import itertools

arr = [i+1 for i in range(n)]

ans = itertools.combinations(arr, m)

for _ in ans:
    print(*_)