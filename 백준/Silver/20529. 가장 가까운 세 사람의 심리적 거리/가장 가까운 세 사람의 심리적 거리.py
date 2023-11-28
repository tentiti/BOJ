import sys
input = sys.stdin.readline

testCase = int(input())
for i in range(testCase):
    peopleCount = int(input())
    people = tuple(input().split())
    
    if peopleCount >= 48:
        print(0)
        continue
    elif peopleCount >= 32:
        print(2)
        continue

    minDist = 16
    
    for j in range(peopleCount):
        for k in range(j+1, peopleCount):
            for l in range(k+1, peopleCount):
                tempDist = 0
                for m in range(4):
                    if people[k][m] != people[j][m]:
                        # print("found!")
                        tempDist += 1
                    if people[l][m] != people[j][m]:
                        # print("found!")
                        tempDist += 1
                    if people[l][m] != people[k][m]:
                        # print("found!")
                        tempDist += 1
                if tempDist < minDist:
                    minDist = tempDist
    
    print(minDist)
                        