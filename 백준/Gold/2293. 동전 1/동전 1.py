n, k = map(int, input().split())
moneys = []
for i in range(n):
    moneys.append(int(input()))
moneys.sort()
    
#아 이거 그 로프자르기랑 똑같은거네
dp = [0 for i in range(k+1)]
dp[0] = 1
for c in moneys:
    for i in range(c, k+1):
        dp[i] += dp[i-c]

print(dp[k])