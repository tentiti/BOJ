#queue 쓰기
from collections import deque
n = int(input())
deque = deque([i+1 for i in range(n)])

while len(deque)>1:
    deque.popleft()
    move_mnum = deque.popleft()
    deque.append(move_mnum)

print(deque[0])