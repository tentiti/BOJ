selec1 = [] #여기서 3
selec2 = [] #여기서 1

for i in range(4):
    selec1.append(int(input()))
for i in range(2):
    selec2.append(int(input()))

selec1.sort(reverse=True)
selec2.sort(reverse=True)

print(sum(selec1[:3])+selec2[0])