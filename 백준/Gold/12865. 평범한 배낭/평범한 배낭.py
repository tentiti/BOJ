n, k = map(int, input().split())
inventory = [[0,0]]
for i in range(n):
    inventory.append(list(map(int, input().split())))

choice = [[0]*(k+1) for i in range(n+1)]

for i in range(1, n+1): #item 관점
    weight = inventory[i][0]
    value = inventory[i][1]
    for j in range(1, k+1): #무게 관점
        if j < weight:
            choice[i][j] = choice[i-1][j]
        else:
            choice[i][j] = max(value + choice[i-1][j-weight], choice[i-1][j])

print(choice[n][k])