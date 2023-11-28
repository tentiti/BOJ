stairCount = int(input())
stairs = []
maxScore = []
for i in range(stairCount):
    stairs.append(int(input()))
    maxScore.append(0)
    
if stairCount <= 2:
    print(sum(stairs))
elif stairCount == 3:
    print(max(stairs[0], stairs[1])+stairs[2])
else:
    maxScore[0] = stairs[0]
    maxScore[1] = stairs[0] + stairs[1]
    maxScore[2] = max(stairs[0], stairs[1])+stairs[2]

    #나를 밟는다면, 어떻게 올 수 있나요?
    #내 전 계단에서 오는 경우 : -3 -1 0 or 내 전전 계단에서 오는 경우: -2 0
    for i in range(3, stairCount):
        maxScore[i] = max(maxScore[i-3]+stairs[i-1]+stairs[i], maxScore[i-2]+stairs[i])

    print(maxScore[-1])