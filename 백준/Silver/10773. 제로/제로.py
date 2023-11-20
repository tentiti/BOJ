import sys
k = int(input())
# sum = 0
nums = []
for i in range(k):
    this = int(sys.stdin.readline())
    if this == 0:
        nums = nums[:-1]
    else:
        nums.append(this)
print(sum(nums))