heights=[]
for i in range(9):
    heights.append(int(input()))

heights.sort()

loc1, loc2 = 0,0
for i in range(9):
    if loc1: break
    for j in range(i):
        temp = 0
        temp += sum(heights[0:j])
        temp += sum(heights[j+1:i])
        temp += sum(heights[i+1:9])
        if temp == 100:
            loc1 = j
            loc2 = i
            break

for i in range(9):
    if i != loc1 and i != loc2:
        print(heights[i])