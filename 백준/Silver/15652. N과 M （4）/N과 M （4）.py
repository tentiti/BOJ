n, m = map(int, input().split())

nums = [i for i in range(n+1)]

visited = [0]*(n+1)

list = []
created = []

def backTracking(result):
    if(len(result)) == m:
        print(*result)
        return
    
    for i in range(1, n+1):
        if (len(result) == 0 or i >= result[-1]):
            result.append(i)
            created.append(result)
            backTracking(result)
        # visited[i] = False
            result.pop()
    
backTracking([])