import sys
input = sys.stdin.readline

while True:
    num = int(input())
    if num == -1:
        break
    temp = []
    tempSum = 0
    for i in range(1, num):
        if num%i == 0:
            temp.append(i)
            tempSum += i
            if tempSum > num:
                break

    if tempSum == num:
        print("{} = ".format(num), end='')
        print(*temp, sep=' + ')
    else:
        print("{} is NOT perfect.".format(str(num)))