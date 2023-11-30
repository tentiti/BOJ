houseCount = int(input())

priceArr = []

for i in range(houseCount):
    rPrice, gPrice, bPrice = map(int, input().split())
    priceArr.append([rPrice, gPrice, bPrice])
    

budgetArr = []
#첫번째 칸 - 그냥 칠하면 됨
budgetArr.append(priceArr[0])

#나를 R로 칠하기 위해 필요한 비용 = min(내 전을 B, 내 전을 G)
for i in range(1, houseCount):
    priceR = min(budgetArr[i-1][1], budgetArr[i-1][2]) + priceArr[i][0]
    priceG = min(budgetArr[i-1][0], budgetArr[i-1][2]) + priceArr[i][1]
    priceB = min(budgetArr[i-1][1], budgetArr[i-1][0]) + priceArr[i][2]
    budgetArr.append([priceR, priceG, priceB])

print(min(budgetArr[-1]))   
        
    