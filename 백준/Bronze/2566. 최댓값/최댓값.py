arr = []
for i in range(9):
    arr.append(list(map(int, input().split())))

x, y =0, 0
max = -1
for i in range(9):
    for j in range(9):
        if arr[i][j] > max:
            x = i
            y = j
            max = arr[i][j]

print(max)
print(x+1, y+1)