k = int(input())
for i in range(1, k+1):
    print(i, end=" ")
    if i%6==0 or i==k:
        print("Go!", end=" ")
        