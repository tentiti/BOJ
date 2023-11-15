n, m = map(int, input().split())
cards = list(map(int, input().split()))
# print(cards)

maxSum = -1

for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1,n):
            if cards[i]+cards[j]+cards[k] > maxSum and cards[i]+cards[j]+cards[k] <= m:
                maxSum = cards[i]+cards[j]+cards[k]
    
print(maxSum)