#N, M 입력받고 배열 생성
w, h = map(int, input().split())
arr = [[0 for i in range(h)] for j in range(w)]

for i in range(w):
    line = input()
    for j in range(h):
        arr[i][j] = line[j]
        
min = 64
color = []
for i in range(w-7):
    for j in range(h-7):
        temp1 = 0
        temp2 = 0
        if arr[i][j] == "W":
            color = ["W", "B"]
        else:
            color = ["B", "W"]
        for x in range(i, i+8):

            for y in range(j, j+8):
                if arr[x][y] != color[(x+y-i-j)%2]:
                    temp1 += 1
                else:
                    temp2 +=1

        if temp2 < temp1:
            temp1 = temp2
        if temp1 < min:
            min = temp1

print(min)