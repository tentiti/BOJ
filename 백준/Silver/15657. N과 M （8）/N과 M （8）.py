# import sys
# sys.setrecursionlimit(10**3)

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

res = []
printed = []
visited = [0 for i in range(len(nums))]
lastPrinted = ''
def dfs(depth):
    global lastPrinted
    if depth == m:
        printed.append(res[:])
        return
    for i in range(len(nums)):
        if len(res)==0 or nums[i] >= res[-1]:
            visited[i] = 1
            res.append(nums[i])
            dfs(depth+1)
            res.pop()
            visited[i] = 0
            # lastDigit = -1

dfs(0)

printed = sorted(list(set(map(tuple, printed))))

for _ in printed:
    print(*_)