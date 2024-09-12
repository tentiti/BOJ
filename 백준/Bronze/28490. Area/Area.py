maxVal=0
for i in range(int(input())):
    a,b=map(int,input().split())
    maxVal=max(maxVal, a*b)
print(maxVal)