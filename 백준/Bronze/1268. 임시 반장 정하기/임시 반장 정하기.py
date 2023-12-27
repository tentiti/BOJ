studentCount = int(input())
data = []
for i in range(studentCount):
    data.append(list(map(int, input().split())))

matchingTable = [[0 for i in range(studentCount)] for i in range(studentCount)]

for i in range(studentCount): #각 학생에 대해
    for j in range(studentCount): #다른 학생들에 대해 
        for k in range(5): #각 학년에 대해
            if data[i][k] == data[j][k]:
                matchingTable[i][j] = 1
                
matchingTableSum = [sum(matchingTable[i]) for i in range(studentCount)]
print(matchingTableSum.index(max(matchingTableSum))+1)