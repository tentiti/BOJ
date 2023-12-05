import itertools

n, m = map(int, input().split())

chickenStore = []
household = []

mapArr = []

for i in range(n):
    temp = list(map(int, input().split()))
    mapArr.append(temp)

for i in range(n):
    for j in range(n):
        if mapArr[i][j] == 1:
            household.append([i, j])
        elif mapArr[i][j] == 2:
            chickenStore.append([i, j])

#치킨집을 최대 m개 고르는 경우의 수
chickenStoreIndex = [i for i in range(len(chickenStore))]
savedChickenIndexes = list(itertools.combinations(chickenStoreIndex, min(len(chickenStoreIndex), m)))

#그 모든 경우의 수에 대해 도시의 치킨 거리 구하기:
minDist = [0 for i in range(len(household))]
minDistMap = 10**9
for i in savedChickenIndexes: #각각의 경우의 수에 대해서
    minDist = [0 for i in range(len(household))]
    #각각의 집에 대해서,
    for j in range(len(household)):
        minDist[j] = min([abs(household[j][0]-chickenStore[k][0])+abs(household[j][1]-chickenStore[k][1]) for k in i])
    minDistMap = min(minDistMap, sum(minDist))

print(minDistMap)