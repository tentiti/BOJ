import math
n = int(input())

cnt = 0
temp = 0

while True:
    temp += 1
    if str(temp).find("666") != -1:
        cnt += 1
    if cnt == n:
        break
    
print(temp)

# if n == 1:
#     print(666)
# else:
#     print(cnt, temp)
#     print(str(cnt)[0:temp+1] + "666" + str(cnt)[temp+1:-1])