n = int(input())
loc = [[0] * (n) for i in range(n)]
# print(loc)
for i in range(n):
    row = input()
    for j in range(n):
        loc[i][j] = row[j]

hearFound = False

# heart of the code
for i in range(n):
    for j in range(n):
        if loc[i][j] == '*':  # found head
            heart_y = i+2
            heart_x = j+1
            print(heart_y, heart_x)  # print heart (1 lower than head)
            hearFound = True
            break  # Break out of the inner loop
    if hearFound:
        break

# length of left arm
larmLength = loc[heart_y-1][:heart_x-1].count('*')
rarmLength = loc[heart_y-1][heart_x:].count('*')

# length of waist
waist = 0
for i in range(heart_y, n):
    if loc[i][heart_x-1] == '*':
        waist += 1

# length of legs
lll, rll = 0, 0
for i in range(heart_y, n):
    if loc[i][heart_x-2] == '*':
        lll += 1
    if loc[i][heart_x] == '*':
        rll += 1

print(larmLength, rarmLength, waist, lll, rll)
