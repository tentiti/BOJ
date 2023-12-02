n, m = map(int, input().split())

numList = list(map(int, input().split()))
numList.sort()

res = []
used = [0 for i in range(n)]

def printer(v, level):
    if level == m:
        print(*res,sep=' ')
        # res.pop(-1)
        return
    else:
        for j in range(n):
            if not used[j]:
                used[j] = 1
                res.append(numList[j])
                printer(j, level+1)
                res.pop(-1)
                used[j] = 0

printer(-1, 0)
            