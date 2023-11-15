a, b, N = map(int,input().split())

for i in range(N):
    a = (a%b)*10
    answer = a//b

print(answer)