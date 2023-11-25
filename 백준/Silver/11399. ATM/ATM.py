n = int(input())
times = sorted(list(map(int, input().split())))
# print(times)
answer = 0
for i in range(n):
    answer += times[i] * (n-i)

    
print(answer)