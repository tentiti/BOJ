points = int(input())
xP = []
yP = []

for i in range(points):
    a, b = map (int, input().split())
    xP.append(a)
    yP.append(b)

xP.append(xP[0])
yP.append(yP[0])

val1 = 0
val2 = 0
for i in range(points):
    val1 += xP[i]*yP[i+1]
    val2 += xP[i+1]*yP[i]

print(1/2*abs(val1-val2))