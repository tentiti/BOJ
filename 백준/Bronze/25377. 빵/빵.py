ans = 10001
for i in range(int(input())):
    a,b=map(int,input().split())
    if a<=b: ans=min(ans, b)
if ans == 10001:
    print(-1)
else:
    print(ans)