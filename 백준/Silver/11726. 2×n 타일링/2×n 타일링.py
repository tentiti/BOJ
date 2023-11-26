length = int(input())
timeArr = [1] * (length+2)
# timeArr[0] = 0
# timeArr[1] = 1
timeArr[2] = 2

if length == 1:
    print(1)
elif length == 2:
    print(2)
elif length == 3:
    print(3)
else:
    for i in range(3, len(timeArr)):
        timeArr[i] = timeArr[i-1] + timeArr[i-2]
        timeArr[i] %= 10007
    print(timeArr[-2])