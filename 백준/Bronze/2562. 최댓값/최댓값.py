nums = [0]*9

for i in range(9):
  nums[i] = int(input())

loc = 0
max = nums[0]

for i in range(1, 9):
  if nums[i]>max:
    loc = i
    max = nums[i]

print(max)
print(loc+1)