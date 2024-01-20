n, m = map(int, input().split())

numList = list(map(int, input().split()))
numList.sort()

res = []
used = [0 for i in range(n)]
printed = []

def printer(v, level):
    if level == m:
        me = str(res)
        if me not in printed:
            print(*res, sep=' ')
            printed.append(me)
        return
    else:
        for j in range(n):
            if (used[j] == 0 and len(res) == 0) or (res[-1] <= numList[j] and used[j] == 0):
                used[j] = 1
                res.append(numList[j])
                printer(j, level+1)
                res.pop(-1)
                used[j] = 0

printer(-1, 0) #dfs
            