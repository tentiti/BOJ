from collections import deque
def bfs(org, target):
    global already
    considered = []
    queue = deque()
    queue.append((org, ''))
    temp = (org, '')
    while temp[0] != target:
        temp = queue.popleft()
        temp_r = temp[0]
        temp_m = temp[1]
        if temp_r == target:
            return temp_m
        #D
        d = temp_r*2%10000
        if already[d] == 0:
            queue.append((d, temp_m+'D'))
            already[d] = 1
        #S
        s = (temp_r-1)%10000
        if already[s] == 0:
            queue.append((s, temp_m+'S'))
            already[s] = 1
        #L, R
        l = (temp_r%1000)*10+temp_r//1000
        if already[l] == 0:
            queue.append((l, temp_m+'L'))
            already[l] = 1
        r = (temp_r%10)*1000+temp_r//10
        if already[r] == 0:
            queue.append((r, temp_m+'R'))
            already[r] = 1
    
testCase = int(input())

for i in range(testCase):
    already = [0 for i in range(10000)]
    org, target = map(int, input().split())
    already[int(org)] = 1
    print(bfs(org, target))