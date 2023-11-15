n = input()

normalLength = 0
compValue = 0
numCount = [0 for i in range(10)]

for  i in range(len(n)):
    if int(n[i]) == 6 or int(n[i]) == 9:
        if numCount[6] + numCount[9]>= normalLength * 2:
            normalLength += 1
            numCount[int(n[i])] += 1
        else:
            numCount[int(n[i])] += 1
    else:
        if numCount[int(n[i])] >= normalLength:
            normalLength += 1
            numCount[int(n[i])] += 1
        else:
            numCount[int(n[i])] += 1

print(normalLength)