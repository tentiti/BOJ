import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())

numList = list(map(int, input().split()))
numList.sort()

res = []
used = [0 for i in range(n)]
printed = []

def printer(level):
    if level > 1:
        if res[-1] < res[-2]:
            return
    if level == m:
        if str(res) not in printed:
            print(*res, sep=' ')
            printed.append(str(res))
        return
    for j in numList:
        res.append(j)
        # print(res)
        printer(level+1)
        res.pop(-1)

printer(0) #dfs