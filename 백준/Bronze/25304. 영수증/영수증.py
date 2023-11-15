sum_p = int(input())
rep = int(input())
sum_res = 0
for i in range(rep):
    a, b = map(int, input().split())
    sum_res += a*b
if sum_p==sum_res:
    print("Yes")
else:
    print("No")
