rep = int(input())
ans = [0] * 12
ans[1] = 1
ans[2] = 2
ans[3] = 4

for i in range(4, 12):
    ans[i] = ans[i-1] + ans[i-2] + ans[i-3]

for i in range(rep):
    print(ans[int(input())])
