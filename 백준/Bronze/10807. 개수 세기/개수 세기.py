num = int(input())
arr = input().split()
v = input()
res = 0
for i in range(num):
  if arr[i]==v:
    res+=1
print(res)