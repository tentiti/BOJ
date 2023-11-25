n = int(input())
s = int(input())
m = input()
# q = 'I'
i = 0
count = 0
answer = 0
# for i in range(n):
#     q += 'OI'

#단순
# for i in range(n, s-n):
#     # print(m[i-n:i+n+1])
#     if m[i-n:i+n+1] == q:
#         count += 1
        
while i < (s - 1):
    if m[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == n:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)