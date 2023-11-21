n, b = input().split()
dec = 0
#3진법 231 10진법으로 변환하기:
# 2*3^2 + 3*3^1 + 1*3^0

for i in range(1, len(n)+1):
    if ord(n[-i]) > 57:
        tempVal = ord(n[-i]) - 55
    else:
        tempVal = int(n[-i])
    dec += tempVal * (int(b) ** (i-1))

print(dec)