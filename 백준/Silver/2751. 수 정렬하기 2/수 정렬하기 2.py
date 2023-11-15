import sys

ans = []
num = int(input())

for i in range(num):
    ans.append(int(sys.stdin.readline()))
    
ans = sorted(ans)
for _ in ans:
    print(_)