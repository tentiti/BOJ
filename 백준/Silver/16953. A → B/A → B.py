from collections import deque

a, b = map(int, input().split())

accessible = {}

def bfs(a):
    queue = deque()
    queue.append(a)
    while queue:
        v = queue.popleft()
        c1 = v*10 + 1
        c2 = 2*v
        if c1 <= b:
            if c1 in accessible.keys():
                accessible[c1] = min(accessible[v] + 1, accessible[c1])
            else:
                accessible[c1] = accessible[v]+1
            queue.append(c1)
        if c2 <= b:
            if c2 in accessible.keys():
                accessible[c2] = min(accessible[v] + 1, accessible[c2])
            else:
                accessible[c2] = accessible[v]+1
            queue.append(c2)

accessible[a] = 0
bfs(a)

if b in accessible.keys():
    print(accessible[b]+1)
else:
    print(-1)